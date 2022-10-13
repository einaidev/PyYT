class Comments:
    def __init__(self, args) -> None:
        self.args = args

    @property
    def size(self):
        """Size
        
        Return video comments size
        """   
        return self.args["commentsSize"]
    