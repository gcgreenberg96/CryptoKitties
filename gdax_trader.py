import gdax
from time import sleep
from datetime import datetime, timedelta
import tensorflow
# Python docs: https://github.com/danpaquin/gdax-python
# GDAX docs: https://docs.gdax.com/?python#rate-limits

# Always convert numbers to strings when making a request with values

BTC = "BTC-USD"
ETH = "ETH-USD"
COIN = ETH
HODL = "HODL"

#sandbox_api_key = "41bafe8b3899d0f3d6c3ae5b28952636"
#sandbox_secret = "J9Ga2gM03QGTpREb+uXzIVNVxDgEJVo970tee5gq78mUAOl8JiC2TMO0qAV5na25KIuMcEymR43OM8kCxn3JqA=="
#sandbox_passphrase = "lefley"
api_key = ""
api_secret = ""
api_passphrase = ""

# WebsocketClient and first function are only needed for seeing real time data, not needed for trader
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

def tradeOrHODL(prediction):
    #---------- TODO ------------
    # make decision on whether to hold or trade
    return HODL
    return COIN

def trade(auth_client,prediction):
    if prediction < 0: # prediction says price will go down
        auth_client.sell(price = '',
                         size = '',
                         product_id = COIN)
    else: # prediction says price will go up
        auth_client.buy(price = '',
                         size = '',
                         product_id = COIN)

def getDeltas(auth_client):
    deltas = []
    five_min_prices = []

    end_time = str(datetime.now().isoformat()) # Get the current time in ISO 8601
    start_time = str((datetime.now() - timedelta(days = 1)).isoformat()) # Subtract 24 hours from end_time
    time_slice = 300 # represents 5 minutes (see gdax docs)
    five_min_prices = auth_client.get_product_historic_rates(COIN, start = start_time, end = end_time, granularity = time_slice)

    for i in range(len(five_min_prices)):
        if (i > 0): # skip first price (no previous price to compare from)
            deltas[i-1] = five_min_prices[i] - five_min_prices[i-1] # create deltas

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
    auth_client = login(api_key, api_secret, api_passphrase)

    while True:

        deltas = getDeltas(auth_client) # passing time as minutes
        prediction = testNeuralNetwork(deltas)
        should_hold = tradeOrHODL(prediction)

        if (should_hold != HODL):
            trade(auth_client, prediction)

        sleep(5*60) # trade every 5 min


main()
