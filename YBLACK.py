
import pychromecast
from pychromecast.controllers.youtube import YouTubeController

CAST_NAME = "Xbox_One"

chromecasts = pychromecast.get_chromecasts()
if len(chromecasts) == 0: 
    print("NO CHROMO")
else:
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == CAST_NAME)
    cast.wait()
    yt = YouTubeController()
    cast.register_handler(yt)

