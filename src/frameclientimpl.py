from apiclient import APIClient

class FrameClientImpl(APIClient):
    def __int__(self, url):
        self.url = url
    
    def get_items(self, item, extension) -> str:
        data_to_get = item.lower().replace(" ", "_")
        url_get = self.url + data_to_get + "/orders"
        return self.get(url_get)


client = FrameClientImpl("https://api.warframe.market/v1")

client.get_items("Mirage Prime Systems", "/items")