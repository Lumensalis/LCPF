from __future__ import annotations


import weakref, json, requests, importlib
from collections import OrderedDict
from typing import *

from . import NiProxySessionRL

if TYPE_CHECKING:
    from .Controller import ControllerProxy
    from .NiProxyRL import *

#############################################################################

def neverNoneDeref[T]( tRef:weakref.ReferenceType[T]) -> T:
    rv = tRef()
    assert rv is not None
    return rv

#############################################################################

class NLIProxyCmdResponse(TypedDict, total=False):
    session:str
    error:str|None
    result:NotRequired[Any]


#############################################################################

class NliProxySession(object):
    def __init__(self, controller: ControllerProxy, copy:Optional[NliProxySession]=None) -> None:
        self.__controller = weakref.ref(controller)
        self.sessionUuid:str|None = copy.sessionUuid if copy is not None else None
        self.remoteReload:bool = copy.remoteReload if copy is not None else True
        self._proxyQueryCache:dict[tuple[str|None,int|None], dict[str, Any]] =  \
            copy._proxyQueryCache.copy() if copy is not None and not copy.remoteReload else {}
        self.proxiesByPath:dict[str, LocalIdentifiableProxy] = {}
        self.proxiesById:dict[int, LocalIdentifiableProxy] = {}

        NiProxySessionRL.NliProxySession_loadProxies()


    @property
    def controller(self) -> ControllerProxy:
        return neverNoneDeref(self.__controller)
    
    def rl(self) -> None:
        NiProxySessionRL.NliProxySession_rl(self)

    def clearProxyCache(self) -> None:
        self._proxyQueryCache.clear()
        self.proxiesByPath.clear()
        self.proxiesById.clear()

    def postProxyCmd( self, cmd:str, *positionalArgs:Any, **kwds:Any) -> NLIProxyCmdResponse:
        return  NiProxySessionRL.NliProxySession_postProxyCmd( self, cmd, *positionalArgs, **kwds)

    def proxy( self, path:Optional[str] = None, localId:Optional[int]=None,recurse:int=12,debug=False ) -> LocalIdentifiableProxy:
        return NiProxySessionRL.NliProxySession_proxy(self, path=path, localId=localId, recurse=recurse, debug=debug)

    def newSession(self) -> NliProxySession:
        return NiProxySessionRL.NliProxySession_newSession(self)


#############################################################################
class SessionSpecific(object):
    def __init__(self, session: NliProxySession) -> None:
        self.__session = weakref.ref(session)

    @property
    def session(self) -> NliProxySession:
        s = self.__session()
        assert s is not None
        return s


#############################################################################

#from .NiProxyRL import *

