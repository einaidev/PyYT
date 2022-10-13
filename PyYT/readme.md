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
api.video.title #video title
api.video.thumbnail #video thumbnailg
api.video.likes #video likes count
api.video.views #video views
api.video.date #video upload date (list)

```