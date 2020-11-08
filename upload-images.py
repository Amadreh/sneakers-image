#!/usr/bin/env python3
import json
import types
import urllib.request

with open('sneakers.json') as file:
    data = json.loads(file.read(), object_hook=lambda d: types.SimpleNamespace(**d))
    for sneaker in data.Products:
        url = sneaker.media.smallImageUrl
        path = url.rsplit('/',1)[1]
        destination = path.rsplit('?',1)[0]
        urllib.request.urlretrieve(url, destination)