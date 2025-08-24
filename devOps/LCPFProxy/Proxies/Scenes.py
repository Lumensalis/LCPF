
from LCPFProxy.NiProxy import LocalIdentifiableProxy

#############################################################################

class Scene(LocalIdentifiableProxy):
    pass


class SceneRule(LocalIdentifiableProxy):
    pass

class SceneManager(LocalIdentifiableProxy):
    
    @property
    def currentScene(self): 
        return self.__currentScene
        
    @currentScene.setter
    def currentScene(self, scene:Scene|str):
        self.setScene(scene)

#############################################################################
