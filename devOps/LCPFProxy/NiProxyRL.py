from __future__ import annotations

import importlib

from typing import * # type: ignore

from LCPFProxy import NiProxy

if TYPE_CHECKING:
    from .NiProxy import LocalIdentifiableProxy, NLIContainer, NliList, LocalIdentifiableProxy
    import rich.repr

# pyright : reportPrivateUsage=false

def _containerContent( self:LocalIdentifiableProxy, containerName:str ):
    container = getattr(self, containerName, None)
    if container is not None:
        assert isinstance(container, NiProxy.NLIContainer), f"Expected NLIContainer for {containerName}, got {type(container)}"
        if len(container):
            yield containerName, dict(container.data)

def NliList__rich_repr__(self:NliList) -> rich.repr.Result:
    
    if self.type == self.__class__.__name__:
        yield None, (self.name, self.localId)
    else:
        yield None, (self.name, self.localId, self.type)

    yield from _containerContent(self,"containers")
    yield from _containerContent(self,"children")
    for tag,val in self.items.data.items():
        yield tag, val

    if self._enableDbgOut is not False:
        yield "enableDbgOut", self._enableDbgOut

    if 'recurse' in self._kwds:
        yield "recurse", self._kwds['recurse']

def NLIContainer__rich_repr__(self:NLIContainer) -> rich.repr.Result:
    for tag,val in self.data.items():
        yield tag, val

def LocalIdentifiableProxy__rich_repr__(self:LocalIdentifiableProxy) -> rich.repr.Result:
    
    if self.type == self.__class__.__name__:
        yield None, (self.name, self.localId)
    else:
        yield None, (self.name, self.localId, self.type)

    yield from _containerContent(self,"containers")
    yield from _containerContent(self,"children")
    yield from _containerContent(self,"items")

    if self._enableDbgOut is not False:
        yield "enableDbgOut", self._enableDbgOut

    if 'recurse' in self._kwds:
        yield "recurse", self._kwds['recurse']

    if self.settings is not None:
        yield "settings", self.settings

def LocalIdentifiableProxy_sak(self:LocalIdentifiableProxy, *args:Any, **kwds:Any) -> Any:
    pass

def LocalIdentifiableProxy_rl(self:LocalIdentifiableProxy) -> Any:
    from . import NiProxyRL
    importlib.reload( NiProxyRL)
    pass
