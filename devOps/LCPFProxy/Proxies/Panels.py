
from __future__ import annotations
from typing import *

from LCPFProxy.NiProxySession import NliProxySession

from LCPFProxy.NiProxy import LocalIdentifiableProxy, NLIProxyBaseDict


#############################################################################

class ControlPanel(LocalIdentifiableProxy):
    pass        

class PanelControl(LocalIdentifiableProxy):
    def __init__(self,  session: NliProxySession, **kwds: Unpack[NLIProxyBaseDict]) -> None:
        super().__init__(session,**kwds)

    def getControlValue(self) -> Any:
        return self.act('remoteGet')

    def setControlValue(self, value: Any) -> Any:
        return self.act('remoteSet', value=value)

class PanelTrigger(LocalIdentifiableProxy):

    def fire(self) -> Any:
        return self.act('remoteFire')



#############################################################################
