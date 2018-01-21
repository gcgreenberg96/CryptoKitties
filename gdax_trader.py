import gdax
import time
# Python docs: https://github.com/danpaquin/gdax-python
# GDAX docs: https://docs.gdax.com/?python#rate-limits

# Always convert numbers to strings when making a request with values

sandbox_api_key = "41bafe8b3899d0f3d6c3ae5b28952636"
sandbox_secret = "J9Ga2gM03QGTpREb+uXzIVNVxDgEJVo970tee5gq78mUAOl8JiC2TMO0qAV5na25KIuMcEymR43OM8kCxn3JqA=="
sandbox_passphrase = "lefley"

def login_public():
    return gdax.PublicClient() # public clients have basic usage

def login_authenticated(key, b64secret, passphrase):
    # currently in sandbox mode
    return gdax.AuthenticatedClient(key, b64secret, passphrase, api_url="https://api-public.sandbox.gdax.com") # these params are given once gdax account is configured with api

class myWebsocketClient(gdax.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.gdax.com/"
        self.products = ["BTC-USD"]
        self.message_count = 0
        print("Lets count the messages!")
    def on_message(self, msg):
        self.message_count += 1
        if 'price' in msg and 'type' in msg:
            print ("Message type:", msg["type"],
                   "\t@ {:.3f}".format(float(msg["price"])))
    def on_close(self):
        print("-- Goodbye! --")



auth_client = login_authenticated(sandbox_api_key, sandbox_secret, sandbox_passphrase)
account = auth_client.get_accounts()
print(account)

wsClient = myWebsocketClient()
wsClient.start()
print(wsClient.url, wsClient.products)
#while (wsClient.message_count < 500):
#    print ("\nmessage_count =", "{} \n".format(wsClient.message_count))
#    time.sleep(1)
wsClient.close()
