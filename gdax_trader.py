import gdax
import time
# Python docs: https://github.com/danpaquin/gdax-python
# GDAX docs: https://docs.gdax.com/?python#rate-limits

# Always convert numbers to strings when making a request with values

BTC = "BTC-USD"
ETH = "ETH-USD"

sandbox_api_key = "41bafe8b3899d0f3d6c3ae5b28952636"
sandbox_secret = "J9Ga2gM03QGTpREb+uXzIVNVxDgEJVo970tee5gq78mUAOl8JiC2TMO0qAV5na25KIuMcEymR43OM8kCxn3JqA=="
sandbox_passphrase = "lefley"

class realTimeWebsocketClient(gdax.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.gdax.com/"
        self.products = [ETH]
        self.message_count = 0
    def on_message(self, msg):
        self.message_count += 1
        if 'price' in msg and 'type' in msg:
            print ("Message type:", msg["type"],"\t@ {:.3f}".format(float(msg["price"])))
    def on_close(self):
        print("-- Goodbye! --")

def login_public():
    return gdax.PublicClient() # public clients have basic usage

def login_authenticated(key, b64secret, passphrase):
    # currently in sandbox mode
    return gdax.AuthenticatedClient(key, b64secret, passphrase, api_url="https://api-public.sandbox.gdax.com") # these params are given once gdax account is configured with api

def printRealTimePrices(count):
    wsClient = realTimeWebsocketClient()
    wsClient.start()
    print(wsClient.url, wsClient.products)
    while(wsClient.message_count < count):
        pass
    wsClient.close()

def printAccounts(auth_client):
    print("\nAccount Data: \n")
    print(auth_client.get_accounts())

def getDeltas(delta_time,total_time):
    deltas = []
    if (delta_time > total_time) or (delta_time % total_time != 0):
        print ("Invalid time inputs")
        return deltas
    #...
    return deltas

auth_client = login_authenticated(sandbox_api_key, sandbox_secret, sandbox_passphrase)
printRealTimePrices(100)
