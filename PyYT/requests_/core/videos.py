from bs4 import BeautifulSoup as bs
import requests,json
from typing import *
from exceptions import *
from requests_.models import *

class Video:
    def __init__(self, session, url) -> None:
        self.session:requests.Session = session
        self.url:str = url
    
    def __call__(self) -> videoInfo:
        rounds = 0
        r = self.session.get(self.url)
        s = bs(r.text, "html.parser")
        # print((s.find_all("script")[-5].getText().split("="))[0].__len__(),(s.find_all("script")[-5].getText().split("="))[0])
        for i in s.find_all("script"):
            if "var ytInitialData" in i.getText():
                if r.status_code == 200:
                    rounds +=1
                    j = json.loads("".join("".join(i.getText().split("=")[1:]).split(";")[:-1]))
                    return videoInfo(intialdata=j)
                else:
                    raise PageNotFound404("{0} video dont found".format(self.url))
        if round == 0: return videoInfo()