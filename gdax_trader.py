import gdax
import time
import tensorflow
# Python docs: https://github.com/danpaquin/gdax-python
# GDAX docs: https://docs.gdax.com/?python#rate-limits

# Always convert numbers to strings when making a request with values

BTC = "BTC-USD"
ETH = "ETH-USD"
COIN = ETH

sandbox_api_key = "41bafe8b3899d0f3d6c3ae5b28952636"
sandbox_secret = "J9Ga2gM03QGTpREb+uXzIVNVxDgEJVo970tee5gq78mUAOl8JiC2TMO0qAV5na25KIuMcEymR43OM8kCxn3JqA=="
sandbox_passphrase = "lefley"

class realTimeWebsocketClient(gdax.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.gdax.com/"
        self.products = [COIN]
        self.message_count = 0
    def on_message(self, msg):
        self.message_count += 1
        if 'price' in msg and 'type' in msg:
            print ("Message type:", msg["type"],"\t@ {:.3f}".format(float(msg["price"])))
    def on_close(self):
        print("-- Goodbye! --")

def printRealTimePrices(count):
    wsClient = realTimeWebsocketClient()
    wsClient.start()
    print(wsClient.url, wsClient.products)
    while(wsClient.message_count < count):
        pass
    wsClient.close()

def login(key, b64secret, passphrase):
    # currently in sandbox mode
    return gdax.AuthenticatedClient(key, b64secret, passphrase, api_url="https://api-public.sandbox.gdax.com") # these params are given once gdax account is configured with api

def printAccounts(auth_client):
    print("\nAccount Data: \n")
    print(auth_client.get_accounts())

def tradeOrHODL():
    #---------- TODO ------------
    # make decision on whether to hold or trade
    return HODL
    return COIN

def trade(auth_client,product):
    #---------- TODO ------------
    pass

def getDeltas(delta_time,total_time):
    deltas = []
    if (delta_time > total_time) or (delta_time % total_time != 0):
        print ("Invalid time inputs")
        return deltas
    #---------- TODO ------------
    # Get newest deltas from gdax
    return deltas

def trainNeuralNetwork():
    #---------- TODO ------------
    pass

def testNeuralNetwork(deltas):
    #---------- TODO ------------
    # feed deltas to neural network, return expected price change
    predicted_delta = 0
    return predicted_delta

def main():
    auth_client = login(sandbox_api_key, sandbox_secret, sandbox_passphrase)

    while True:

        deltas = getDeltas(5,24*60) # passing time as minutes
        prediction = testNeuralNetwork(deltas)
        should_hold = tradeOrHODL(prediction)

        if (should_hold != HODL):
            trade(auth_client, COIN)

        sleep(5*60) # trade every 5 min


main()
