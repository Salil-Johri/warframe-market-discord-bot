import interfaces

class FrameBotImpl(IFrameRepo):
    def __init__(self, frame_client, url):
        self.frame_client = frame_client
    
    def get_item_price(self, item_name) -> str:

