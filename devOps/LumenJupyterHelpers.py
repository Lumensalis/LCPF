from __future__ import annotations

# pyright: reportUnusedImport=false

import importlib
import re
from typing import Any, Optional, TypeAlias, Callable, Dict 
import requests, sys, os.path

#############################################################################

def reloadLumenJupyterHelpers():
    import LumenJupyterHelpers
    importlib.reload(LumenJupyterHelpers)


class ResponseWrapper(object):
    def __init__(self, response: requests.Response):
        self.response = response

    def json(self) -> Any:
        return self.response.json()

    def text(self) -> str:
        return self.response.text
    def __repr__( self ):
        try:
            return f"ResponseWrapper({self.response.status_code}) : {self.json()}"
        except Exception as e:
            return f"ResponseWrapper(Error: {e}) : {self.response}"

class ControllerProxy(object):
    def __init__(self, ip:str, port:int=5000):
        self.ip = ip
        self.port = port
        self.url = f"http://{ip}:{port}"
    
    def post( self, urlPart:str, **kwds:Any) -> ResponseWrapper:
        response = requests.post(f"{self.url}/{urlPart}", json=kwds)
        return ResponseWrapper(response)

    def cmd(self, cmd:str, **kwds:Any) -> ResponseWrapper:
        return self.post(f"cmd/{cmd}", cmd=cmd, **kwds)

    def sak(self, **kwds:Any) -> ResponseWrapper:
        return self.post(f"sak", **kwds)

    def sakRL(self, **kwds:Any) -> ResponseWrapper:
        return self.post(f"sakReload", **kwds)

#############################################################################
