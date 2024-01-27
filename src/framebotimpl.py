import requests
from interfaces.iframerepo import IFrameRepo
from frameclientimpl import FrameHttpClientImpl
class FrameBotImpl(IFrameRepo):
    def __init__(self, frame_client):
        self.frame_client = frame_client
    
    def get_item_price(self, item_name) -> str:
        json_price = self.frame_client.get_items(item_name)
        # need to sort based on price now
        price_array = []
        #first, only get sellers prices
        for order in json_price["orders"]:
            if order['order_type'] == 'sell' and self._is_user_online(order['user']):
                price_array.append(order["platinum"])
        return sorted(price_array)[0]
    
    def _is_user_online(self,user):
        return user["status"] == "online"
