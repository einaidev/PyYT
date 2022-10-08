from .videos import *
from .channel import *

class videoInfo:
    def __init__(self, **args) -> None:
        self.ytintialdata = args["intialdata"]
        chnnl = {
            "name": self.ytintialdata["playerOverlays"]["playerOverlayRenderer"]["videoDetails"]["playerOverlayVideoDetailsRenderer"]["subtitle"]["runs"][0]["text"]
        }
        self.vd = {
            "thumbnail": "https://i.ytimg.com/vi/{0}/hqdefault.jpg".format(self.ytintialdata["currentVideoEndpoint"]["watchEndpoint"]["videoId"]),
            "title": self.ytintialdata["playerOverlays"]["playerOverlayRenderer"]["videoDetails"]["playerOverlayVideoDetailsRenderer"]["title"]["simpleText"],
            "views": self.ytintialdata["playerOverlays"]["playerOverlayRenderer"]["videoDetails"]["playerOverlayVideoDetailsRenderer"]["subtitle"]["runs"][-1]["text"].split(" ")[0],
            "likes": self.ytintialdata["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][0]["videoPrimaryInfoRenderer"]["videoActions"]["menuRenderer"]["topLevelButtons"][0]["toggleButtonRenderer"]["defaultText"]["accessibility"]["accessibilityData"]["label"].split(" ")[0],
            "date": [self.ytintialdata["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][0]["videoPrimaryInfoRenderer"]["dateText"]["simpleText"],
        self.ytintialdata["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][0]["videoPrimaryInfoRenderer"]["relativeDateText"]["accessibility"]["accessibilityData"]["label"] ]

        }
        self.channelName = Channel(name = chnnl["name"])


    def __repr__(self) -> str:
        alls = []
        for x in self.__class__.__dict__:
            if "property" in str(self.__class__.__dict__[x]):
                alls.append("{0!r} = {1}".format(x, self.__class__.__dict__[x]))
        return "<{0} {1}>".format(self.__class__.__name__, ", ".join(alls))
    
    @property
    def video(self) -> VideoProperty:
        return VideoProperty(self.vd)

    @property
    def channel(self,) -> Channel:
        return self.channelName