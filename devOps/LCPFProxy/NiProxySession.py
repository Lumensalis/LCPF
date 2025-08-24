from __future__ import annotations

import re
import weakref, json, requests, importlib
from collections import OrderedDict
from typing import *

from . import NiProxySessionRL

if TYPE_CHECKING:
    from .Controller import ControllerProxy
    from .NiProxyRL import *

#############################################################################

class NLIProxyCmdResponse(TypedDict, total=False):
    session:str
    error:str|None
    result:NotRequired[Any]


class NliProxySession(object):
    def __init__(self, controller: ControllerProxy) -> None:
        self.__controller = weakref.ref(controller)
        self.sessionUuid:str|None = None
        self.remoteReload:bool = True
        self.proxiesByPath:dict[str, LocalIdentifiableProxy] = {}
        self.proxiesById:dict[int, LocalIdentifiableProxy] = {}

        NiProxySessionRL.NliProxySession_loadProxies()


    @property
    def controller(self) -> ControllerProxy:
        return self.__controller()
    
    def rl(self) -> None:
        NiProxySessionRL.NliProxySession_rl(self)

    def postProxyCmd( self, cmd:str, **kwds:Any) -> NLIProxyCmdResponse:
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
    
    def proxy( self, path:Optional[str] = None, localId:Optional[int]=None,recurse:int=12,debug=False ) -> LocalIdentifiableProxy:
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
        
        response = self.postProxyCmd( "query", path= path, localId= localId, recurse=recurse, debug=debug )
        import LCPFProxy.NiProxy
        #import LCPFProxy.NiProxyRL
        #importlib.reload(LCPFProxy.NiProxyRL)
        #importlib.reload(LCPFProxy.NiProxy)
        result = response.get('result', None)
        assert result is not None, f"proxy command failed: {response.get('error', 'unknown error')}"
        rv = LCPFProxy.NiProxy.LocalIdentifiableProxy.make(self,**result) 
        if path is not None:
            self.proxiesByPath[path] = rv

        assert rv.localId is not None
        assert rv.localId not in self.proxiesById
        self.proxiesById[rv.localId] = rv
        return rv

    def newSession(self) -> NliProxySession:
        return NiProxySessionRL.NliProxySession_newSession(self)

from .NiProxyRL import *

