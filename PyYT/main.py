from requests_ import *

class Main:
    """
    this is an api developed to facilitate access to youtube,
    in order to see information about videos, playlist channels
    later we will add more functions like downloading
    videos and among other functions    
    """
    def __init__(self, url,type="video") -> None:
        self.url = url
        self.type = type
        self.types = ["video"]
        if self.type in self.types:
            if self.type == "video":
                self.r = Send(self.url,self.type)
    
    @property
    def start(self) -> videoInfo:
        r = self.r()
        return r
