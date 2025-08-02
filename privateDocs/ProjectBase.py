
#############################################################################
# Project base class
class ProjectBase(object):
    def __init__(self,verbose:bool = False) -> None:
        self.verbose = verbose

    def sayAtStartup(self, message: str) -> None:
        if self.verbose:
            print(message)

    def sayWhileRunning(self, message: str) -> None:
        if self.verbose:
            print(message)
    
    def setup(self) -> None:
        raise NotImplementedError("Setup method must be implemented in the subclass")

    def loop(self) -> None:
        raise NotImplementedError("Loop method must be implemented in the subclass")

    def run(self) -> None:
        self.setup()
        self.sayAtStartup("starting mail loop")
        while True:
            self.loop()
