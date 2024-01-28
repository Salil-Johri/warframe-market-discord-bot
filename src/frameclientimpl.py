import json
from interfaces.iframeclient import IFrameClient
class FrameHttpClientImpl(IFrameClient):
    def __init__(self, getter, url):
        self.url = url
        self.getter = getter
    
    def get_items(self, item):
        data_to_get = item.lower().replace(" ", "_")
        url_get = self.url + "/items/" + data_to_get + "/orders"
        print("retrieving item " + data_to_get)
        r = self.getter.get(url_get)
        print(url_get)
        return json.loads(r.text)['payload']
