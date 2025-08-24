from __future__ import annotations
from typing import TYPE_CHECKING

from LCPFProxy.NiProxy import LocalIdentifiableProxy
from ..NiProxySession import NliProxySession, SessionSpecific

if TYPE_CHECKING:
    
    import rich.repr
    from .Tunables import TunableSettings

import rich
from .Tunables import TunableSettings

#############################################################################

def TunableSettings__rich_repr__(self:TunableSettings) -> rich.repr.Result:
    yield "active", self.active
    yield "inactive", self.inactive

#############################################################################
