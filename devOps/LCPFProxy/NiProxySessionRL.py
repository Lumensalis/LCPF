from __future__ import annotations

import re
import weakref, json, requests, importlib
from collections import OrderedDict
from typing import *

if TYPE_CHECKING:
    from .Controller import ControllerProxy
    from .NiProxySession import NliProxySession, NLIProxyCmdResponse
    from .NiProxyRL import *

#############################################################################

def NliProxySession_loadProxies() -> None:
    from LCPFProxy.Proxies import Tunables, Panels, Scenes, Shields, TerrainTronics

def NliProxySession_rl(self:NliProxySession) -> None:
    from LCPFProxy.Proxies import Tunables, TunablesRL, Panels, Scenes, Shields, TerrainTronics
    from LCPFProxy import NiProxySessionRL
    from LCPFProxy import NiProxySession
    from LCPFProxy import NiProxyRL
    from LCPFProxy import NiProxy

    importlib.reload(NiProxySessionRL)
    importlib.reload(NiProxySession)
    importlib.reload(NiProxyRL)
    importlib.reload(NiProxy)
    importlib.reload(TunablesRL)
    importlib.reload(Tunables)
    importlib.reload(Panels)
    importlib.reload(Scenes)
    importlib.reload(Shields)
    importlib.reload(TerrainTronics)


def NliProxySession_newSession(self:NliProxySession) -> NliProxySession:
    self.rl()
    from LCPFProxy import NiProxySession
    return NiProxySession.NliProxySession(self.controller, copy=self)


def NliProxySession_postProxyCmd( self:NliProxySession, cmd:str, **kwds:Any) -> NLIProxyCmdResponse:
    print( f"NliProxySession({self.sessionUuid}) postProxyCmd: {cmd} {kwds}" )
    response = self.controller.post(
        'proxyReload' if self.remoteReload else 'proxy',
        cmd=cmd, **kwds)
    jsonData:dict[str,Any] = response.json() # type: ignore
    session:Any = jsonData.get("session",None) #
    assert isinstance(session, str), f"Invalid session in response: {session} / {jsonData}"
    if self.sessionUuid is None:
        self.sessionUuid = session
    else:
        assert self.sessionUuid == session, f"Session UUID mismatch {self.sessionUuid} != {session}"
    return jsonData # type: ignore


def NliProxySession_proxy( self:NliProxySession, path:Optional[str] = None, localId:Optional[int]=None,recurse:int=12,debug=False ) -> LocalIdentifiableProxy:
    if path is None and localId is None:
        path = ''
    if path is not None:
        assert localId is None
        existing = self.proxiesByPath.get(path, None)
        if existing is not None:
            return existing
    else:
        assert localId is not None
        existing = self.proxiesById.get(localId,None)
        if existing is not None:
            return existing

    result:dict[str, Any]
    cacheKey = (path, localId)
    existingResult = self._proxyQueryCache.get(cacheKey, None)
    if debug: print( f"proxy cacheKey: {cacheKey} existingResult: {existingResult} remoteReload: {self.remoteReload}" )
    if existingResult is not None and self.remoteReload is False:
        result = existingResult
    else:
        response = self.postProxyCmd( "query", path= path, localId= localId, recurse=recurse, debug=debug )
        result = response.get('result', None)
        assert result is not None, f"proxy command failed: {response.get('error', 'unknown error')}"
        self._proxyQueryCache[cacheKey] = result

    import LCPFProxy.NiProxy
    
    rv = LCPFProxy.NiProxy.LocalIdentifiableProxy.make(self,**result) 
    if path is not None:
        self.proxiesByPath[path] = rv

    assert rv.localId is not None
    assert rv.localId not in self.proxiesById
    self.proxiesById[rv.localId] = rv
    return rv
