from __future__ import annotations

import re
import weakref, json, requests, importlib
from collections import OrderedDict
from typing import *

if TYPE_CHECKING:
    from .Controller import ControllerProxy
    from .NiProxySession import NliProxySession
    from .NiProxyRL import *

#############################################################################

def NliProxySession_loadProxies() -> None:
    from LCPFProxy.Proxies import Tunables, Panels, Scenes, Shields, TerrainTronics

def NliProxySession_rl(self:NliProxySession) -> None:
    from LCPFProxy.Proxies import Tunables, Panels, Scenes, Shields, TerrainTronics
    from LCPFProxy import NiProxySession
    from LCPFProxy import NiProxyRL
    from LCPFProxy import NiProxy
    importlib.reload(NiProxySession)
    importlib.reload(NiProxyRL)
    importlib.reload(NiProxy)
    importlib.reload(Tunables)
    importlib.reload(Panels)
    importlib.reload(Scenes)
    importlib.reload(Shields)
    importlib.reload(TerrainTronics)


def NliProxySession_newSession(self:NliProxySession) -> NliProxySession:
    self.rl()
    from LCPFProxy import NiProxySession
    return NiProxySession.NliProxySession(self.controller)
