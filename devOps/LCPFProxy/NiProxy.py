from __future__ import annotations

from re import S
import weakref, json, requests, importlib
from collections import OrderedDict
from typing import *


if TYPE_CHECKING:
    from .NiProxySession import NliProxySession
    import rich.repr

#############################################################################

from . import NiProxyRL

class InteractableSpecDict( TypedDict):
    kindMatch:str
    name:str
    startingValue:  Any
    min: NotRequired[Any]
    max: NotRequired[Any]
    kind: str
    description: str

class ActiveSettingDict( TypedDict):
    spec: InteractableSpecDict
    active: dict[str, Any]
    cls: str
    name: str
    value: Any

class InactiveSettingDict( TypedDict):
    cls: str
    name: str
    default: Any
    kwds: dict[str, Any]


class SettingsDict( TypedDict):
    active: list[ActiveSettingDict]
    inactive: list[InactiveSettingDict]


class TunableSettings:
    def __init__(self, settings: SettingsDict) -> None:
        self.active = settings['active']
        self.inactive = settings['inactive']
        assert len(settings) == 2

    def __rich_repr__(self) -> rich.repr.Result:
        yield "active", self.active
        yield "inactive", self.inactive

class NLIProxyBaseDict(TypedDict, total=False):
    name: Required[str]
    type: Required[str]
    localId: Required[int]
    containers: NotRequired[list[NLIProxyBaseDict]]
    children: NotRequired[list[NLIProxyBaseDict]]
    items: NotRequired[list[NLIProxyBaseDict]]
    recurse: NotRequired[dict[str, int]]
    enableDbgOut: NotRequired[bool]
    settings: NotRequired[SettingsDict]

class NLIProxyCmdResponse(TypedDict, total=False):
    session:str
    error:str|None
    result:NotRequired[ NLIProxyBaseDict    ]

class NLIProxyMeta(type):
    '''meta class which registers proxy types'''
    
    NLIProxyClasses:ClassVar[dict[str,type]] = {}
    def __new__(cls:type, *args:Any) -> type:
        obj = super().__new__(cls, *args)
        NLIProxyMeta.NLIProxyClasses[obj.__name__] = obj
        return obj


class LocalIdentifiableProxy(object, metaclass=NLIProxyMeta):
    NLIProxyClasses:ClassVar[dict[str,type]] = NLIProxyMeta.NLIProxyClasses

    containers: NLIContainer
    children: NLIContainer
    items: NLIContainer

    def __init__(self, session: NliProxySession, **kwds: Unpack[NLIProxyBaseDict]):
        self.__session = weakref.ref(session)
        self.name = kwds.get("name")
        self.type = kwds.get("type")
        self.localId = kwds.get("localId")
        self._kwds = kwds
        self._enableDbgOut:bool|None =  kwds.get("enableDbgOut",False)

        settings = kwds.get("settings", None)
        if settings is not None:
            settings = TunableSettings(settings)

        self.settings = settings

        self._addKids('containers', kwds.get("containers", None))
        self._addKids('children', kwds.get("children", None))
        self._addKids('items', kwds.get("items", None))
        self.recurse = kwds.get("recurse", None)


    @property
    def session(self) -> NliProxySession:
        return self.__session()

    def postProxyCmd( self, cmd: str, **kwargs: Any ) -> NLIProxyCmdResponse:
        print( f"{self.__class__.__name__}({self.localId}) postProxyCmd: {cmd} {kwargs}" )
        return self.session.postProxyCmd( cmd, localId=self.localId, **kwargs )

    @property
    def enableDbgOut(self) -> bool:
        if self._enableDbgOut is not None:
            return self._enableDbgOut  
        response = self.postProxyCmd("enableDbgOut")
        print( f"enableDbgOut response: {response}" )
        self._enableDbgOut = response.get('enableDbgOut')
        assert self._enableDbgOut is not None
        return self._enableDbgOut
    
    @enableDbgOut.setter
    def enableDbgOut(self, value: bool) -> None:
        self._enableDbgOut = None
        self.postProxyCmd("enableDbgOut", setValue=value)

    def inspect(self,**kwds:Any) -> Any:
        return self.postProxyCmd("inspect", **kwds)
    
    def tuning(self) -> Any:
        return self.postProxyCmd("tune")
    
    def tune(self, **kwds:Any ) -> Any:
        assert len(kwds) == 1
        return self.postProxyCmd("tune", setting=kwds.keys()[0], setValue=kwds.values()[0])

    def _addKids( self, tag:str, kids:list[NLIProxyBaseDict]|None ) -> None:
        if kids is None: kids=[]
        if tag not in self.__dict__:
            setattr(self, tag, NLIContainer(self.session, kids))
        else:
            existing = getattr(self, tag)
            for kid in kids:
                kk = LocalIdentifiableProxy.make(self.session,**kid)
                existing[kid['name']] = kk

    def __getattr__(self, name: str) -> Optional[LocalIdentifiableProxy]:
        
        rv = self.containers.get(name,None) or self.children.get(name,None) or self.items.get(name,None)
        if rv is None:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        return rv

    def _d_dir__(self) -> list[str]:
        return list(super().__dir__()) + list(self.containers.keys()) + list(self.children.keys()) + list(self.items.keys())
    
    def _ipython_key_completions_(self) -> list[str]:
        return list(self.containers.keys()) + list(self.children.keys()) + list(self.items.keys())
            
    def __repr__(self) -> str:
        rvParts:list[str] = [
            f"{self.type}(name={self.name}, localId={self.localId}"
        ]

        rvParts.append(f", _kwds={self._kwds}")
        rvParts.append(")")
        return "".join(rvParts)

    def __rich_repr__(self) -> rich.repr.Result:
        yield from NiProxyRL.LocalIdentifiableProxy__rich_repr__(self)

    def sak(self,*args:Any,**kwds:Any) -> Any:
        return NiProxyRL.LocalIdentifiableProxy_sak(self, *args, **kwds )

    def rl(self) -> Any:
        from . import NiProxyRL
        importlib.reload( NiProxyRL)
        #return NiProxyRL.LocalIdentifiableProxy_rl(self)

    @staticmethod
    def make(session: NliProxySession, **kwds: Unpack[NLIProxyBaseDict]) -> LocalIdentifiableProxy:
        type = kwds.get("type")
        cls = LocalIdentifiableProxy.NLIProxyClasses.get(type, LocalIdentifiableProxy)
        return cls(session, **kwds)

class NLIContainer(object):
     
        
    def __init__(self, session: NliProxySession, kids:Optional[list[NLIProxyBaseDict]]=None) -> None:
        super().__init__()
        self.__session = weakref.ref(session)
        self.data:OrderedDict[str, LocalIdentifiableProxy] = OrderedDict()
        if kids is None: return
        for kid in kids:
            name  = kid['name']
            self.data[name] = LocalIdentifiableProxy.make(self.session, **kid)

    @property
    def session(self) -> NliProxySession:
        return self.__session()
    
    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, name: str) -> Optional[LocalIdentifiableProxy]:
        return self.data.get(name)

    def __getattr__(self, name: str) -> Optional[LocalIdentifiableProxy]:
        try:
            return self.data[name]
        except KeyError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def get(self, name: str,*args) -> Optional[LocalIdentifiableProxy]|None:
        return self.data.get(name,*args)

    def _d_dir__(self) -> list[str]:
        return list(super().__dir__()) + list(self.data.keys())
    
    def _ipython_key_completions_(self) -> list[str]:
        return self.data.keys()

    def __rich_repr__(self) -> rich.repr.Result:
        yield from NiProxyRL.NLIContainer__rich_repr__(self)

class NliList(LocalIdentifiableProxy):
    def __rich_repr__(self) -> rich.repr.Result:
        yield from NiProxyRL.NliList__rich_repr__(self)

#############################################################################


#############################################################################
