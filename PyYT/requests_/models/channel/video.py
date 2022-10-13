class Channel:
    def __init__(self,args) -> None:
        self.args = args

    @property
    def name(self,) -> str:
        """Name
        
        Return channel url
        """
        return self.args["name"]
    
    @property
    def url(self,):
        """Url
        
        Return channel url
        """
        return self.args["url"]