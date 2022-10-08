import requests,json
from typing import *
from .models import *
from exceptions import *
from .core import *

class Send:
    def __init__(self,url,type):
        self.type = type
        self.url = url
        self.session = requests.session()
    def __call__(self) -> videoInfo:
        if self.type == "video":
            return Video(self.session,self.url)()