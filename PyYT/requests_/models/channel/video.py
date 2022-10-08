class Channel:
    def __init__(self,**args) -> None:
        self.args = args

    @property
    def name(self) -> str:
        return self.args["name"]