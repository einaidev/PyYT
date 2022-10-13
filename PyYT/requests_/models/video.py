from bs4 import BeautifulSoup as bs

from .channel import *
from .videos import *


class videoInfo:
    def __init__(self, **args) -> None:
        """Video info| 
        this is the module responsible for submitting youtube responses.
        video title, description, thumbnail and other things
        """
        self.bs4: bs = args["bs4"]
        self.ytintialdata = args["intialdata"]
        chnnl = {
            "name": self.ytintialdata["playerOverlays"]["playerOverlayRenderer"]["videoDetails"]["playerOverlayVideoDetailsRenderer"]["subtitle"]["runs"][0]["text"],
            "url": self.bs4.find("div").find_all_next("link", itemprop="url")[1]["href"]
        }

        self.vd = {
            "thumbnail": "https://i.ytimg.com/vi/{0}/hqdefault.jpg".format(self.ytintialdata["currentVideoEndpoint"]["watchEndpoint"]["videoId"]),
            "title": self.ytintialdata["playerOverlays"]["playerOverlayRenderer"]["videoDetails"]["playerOverlayVideoDetailsRenderer"]["title"]["simpleText"],
            "views": self.ytintialdata["playerOverlays"]["playerOverlayRenderer"]["videoDetails"]["playerOverlayVideoDetailsRenderer"]["subtitle"]["runs"][-1]["text"].split(" ")[0],
            "likes": self.ytintialdata["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][0]["videoPrimaryInfoRenderer"]["videoActions"]["menuRenderer"]["topLevelButtons"][0]["toggleButtonRenderer"]["defaultText"]["accessibility"]["accessibilityData"]["label"].split(" ")[0],
            "date": [self.ytintialdata["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][0]["videoPrimaryInfoRenderer"]["dateText"]["simpleText"],
                     self.ytintialdata["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][0]["videoPrimaryInfoRenderer"]["relativeDateText"]["accessibility"]["accessibilityData"]["label"]],
            "embed": "https://www.youtube.com/embed/{0}".format(self.ytintialdata["currentVideoEndpoint"]["watchEndpoint"]["videoId"]),
            "description": "".join([x["text"] for x in self.ytintialdata["engagementPanels"][1]["engagementPanelSectionListRenderer"]["content"]["structuredDescriptionContentRenderer"]["items"][1]["expandableVideoDescriptionBodyRenderer"]["descriptionBodyText"]["runs"]]),
            "genre": self.bs4.find("meta", itemprop="genre")["content"],
            "allowedRegions": [x for x in self.bs4.find("div").find_next("meta", itemprop="regionsAllowed")["content"].split(",")],
            "duration": self.bs4.find("div").find_next("meta", itemprop="duration")["content"].replace("PT", "").replace("H", ":").replace("M", ":").replace("S", ""),
            "id": self.ytintialdata["currentVideoEndpoint"]["watchEndpoint"]["videoId"],
            "commentsSize": self.ytintialdata["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"][2]["itemSectionRenderer"]["contents"][0]["commentsEntryPointHeaderRenderer"]["commentCount"]["simpleText"],
            # "comments": self.bs4.find("div", id="contents")
        }
        self.channelName = Channel(chnnl)

    def __repr__(self) -> str:
        alls = []
        for x in self.__class__.__dict__:
            if "property" in str(self.__class__.__dict__[x]):
                alls.append("{0!r} = {1}".format(
                    x, self.__class__.__dict__[x]))
        return "<{0} {1}>".format(self.__class__.__name__, ", ".join(alls))

    @property
    def video(self) -> VideoProperty:
        """Video

        return video astributes
        """
        return VideoProperty(self.vd)

    @property
    def channel(self,) -> Channel:
        """Channel

        return channel atributes
        """
        return self.channelName
