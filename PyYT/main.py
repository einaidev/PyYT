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
r = Main("https://www.youtube.com/watch?v=BaI0tiwrKYk").start
print("Thumbnail: {0}\nTitle: {1}\nViews: {2}\nChannel: {3}\nLikes: {4}\nDate: {5}\nEmbed: {6}\n\nDescription:\n{7}\n\nGenre: {8}\nChannel Url: {9}\nDuration: {10}\nId: {11}\nComments Size: {12}\nAllowed Regions: {13}".format(
    r.video.thumbnail,
    r.video.title,
    r.video.views,
    r.channel.name,
    r.video.likes,
    ", ".join(r.video.date),
    r.video.embed,
    r.video.description,
    r.video.genre,
    r.channel.url,
    r.video.duration,
    r.video.id,
    r.video.comments.size,
    r.video.allowedRegions,))