import interfaces

class FrameBotImpl(IFrameRepo):
    
    def __init__(self, http_client, url):
        self.http_client = http_client
    
    def get_item_price(self, item_name) -> str:

