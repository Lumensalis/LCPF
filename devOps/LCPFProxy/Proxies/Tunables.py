from __future__ import annotations

from typing import *

from LCPFProxy.NiProxy import LocalIdentifiableProxy, NLIProxyBaseDict
from ..NiProxySession import NliProxySession, SessionSpecific

import rich.repr

#############################################################################
    

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
    localId: int
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

#@rich.repr.auto
class InactiveSetting(object):
    def __init__(self, kwds:InactiveSettingDict) -> None:
        kwds = kwds.copy()
        self.cls = kwds.pop('cls')
        self.name = kwds.pop('name')
        self.default = kwds.pop('default')
        k2:dict[str,Any] = kwds.pop('kwds') # type: ignore
        assert k2.pop('name', self.name ) == self.name
        assert k2.pop('startingValue', self.default) == self.default
        self.onChange = k2.pop('onChange',None) # ty
        self.kwds = k2 

    def __rich_repr__(self)  -> rich.repr.Result:
        yield "name", self.name
        yield "cls", self.cls
        yield "default", self.default
        if len(self.kwds): yield "kwds", self.kwds


class TunableSettings(SessionSpecific):
    def __init__(self, session: NliProxySession, settings: SettingsDict) -> None:
        super().__init__(session)
        #print(f"TunableSettings: {settings}")
        self.active =  [self._getActive(asd) for asd in settings['active']]
        self.inactive = [InactiveSetting(d) for d in settings['inactive']]
        assert len(settings) == 2
        

    def _getActive(self, kwds: ActiveSettingDict) -> TunableSetting:
        existing = self.session.proxiesById.get(kwds['localId'],None)
        if existing is not None and isinstance(existing, TunableSetting):
            existing.updateFromASD(kwds)
            return existing
        else:
            makeKwds:NLIProxyBaseDict = {
                'name': kwds['name'],
                'type': kwds['cls'],
                'localId': kwds['localId'],
                #'containers': kwds.get('containers', []),
                #'children': kwds.get('children', []),
                #'items': kwds.get('items', []),
                #'recurse': kwds.get('recurse', {}),
                #'enableDbgOut': kwds.get('enableDbgOut', False),
                #'settings': kwds.get('settings', {})
            }
            rv = LocalIdentifiableProxy.make(self.session, **makeKwds)
            
            assert isinstance(rv, TunableSetting), f"Expected TunableSetting, got {type(rv)}"
            rv.updateFromASD(kwds)
            return rv

    def __rich_repr__(self) -> rich.repr.Result:
        yield from TunablesRL.TunableSettings__rich_repr__(self)

#############################################################################

class TunableSetting(LocalIdentifiableProxy) :
    def updateFromASD(self, kwds: ActiveSettingDict) -> None:
        assert self.name == kwds['name']
        assert self.localId == kwds['localId']
        self.value = kwds['value']
        self.settings = kwds

class SecondsSetting(TunableSetting):
    pass

class ZeroToOneSetting(TunableSetting):
    pass

class PlusMinusOneSetting(TunableSetting):
    pass

#############################################################################

from LCPFProxy.Proxies import TunablesRL

#############################################################################
