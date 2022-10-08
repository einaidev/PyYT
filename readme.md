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
api.channel.name
api.video.title
api.video.thumbnail
api.video.likes
api.video.views
api.video.date

```