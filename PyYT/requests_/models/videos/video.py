from .comments import Comments


class VideoProperty:
    def __init__(self, args) -> None:
        self.args = args

    @property
    def thumbnail(self) -> str:
        """Thumbnail
        
        Return video thumbnail link
        """
        return self.args["thumbnail"]
    
    @property
    def title(self,) -> str:
        """Title
        
        Return video title
        """
        return self.args["title"]
    
    @property
    def views(self,) -> str:
        """Views
        
        Return video views
        """
        return self.args["views"]

    @property
    def likes(self,) -> str:
        """Likes
        
        Return video likes
        """
        return self.args["likes"]
    
    @property
    def date(self,) -> list:
        """Date
        
        Return video upload date (type: list)
        """
        return self.args["date"]

    @property
    def embed(self,) -> str:
        """Embed
        
        Return video embed
        """
        return self.args["embed"]

    @property
    def description(self,) -> str:
        """Description
        
        Return video description
        """
        return self.args["description"]
    
    @property
    def genre(self,) -> str:
        """Genre
        
        Return video genre
        """
        return self.args["genre"]
    
    @property
    def allowedRegions(self, ) -> list:
        """AllowedRegions
        
        Return video allowed regions
        """
        return self.args["allowedRegions"]

    @property
    def duration(self,) -> str:
        """Duration
        
        Return video duration
        """      
        return self.args["duration"]
    
    @property
    def id(self,) -> str:
        """id
        
        Return video id
        """   
        return self.args["id"]
    
    @property
    def comments(self,) -> Comments:
        """Comments
        
        Return video comments attributes
        """ 
        return Comments(self.args)