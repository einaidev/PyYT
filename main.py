from requests_ import *

class Main:
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
r = Main("https://www.youtube.com/watch?v=BaI0tiwrKYk").start
print("Thumbnail: {0}\nTitle: {1}\nViews: {2}\nChannel: {3}\nLikes: {4}\nDate: {5}".format(r.video.thumbnail, r.video.title, r.video.views, r.channel.name, r.video.likes, ", ".join(r.video.date)))