# PyYT
>youtube lib for python3+

# Documentation
> First U need create a api instance
```py
import PyYT

api = PyYT.Main("url").start
# Main(url, type<optional, only video>)
```
> property
```py
...
# Api Responses (video type)
api.channel
api.video

# Propertys
#channel
api.channel.name # channel name

# video
api.video.thumbnail,
api.video.title,
api.video.views,
api.video.likes,
api.video.date
api.video.embed,
api.video.descapiiption,
api.video.genapie,
api.video.duapiation,
api.video.id,
api.video.comments.size,
api.video.allowedRegions

```