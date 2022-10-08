class VideoProperty:
    def __init__(self, args) -> None:
        self.args = args

    @property
    def thumbnail(self) -> str:
        return self.args["thumbnail"]
    
    @property
    def title(self,) -> str:
        return self.args["title"]
    
    @property
    def views(self,) -> str:
        return self.args["views"]

    @property
    def likes(self,) -> str:
        return self.args["likes"]
    
    @property
    def date(self,) -> list:
        return self.args["date"]