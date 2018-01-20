from time import sleep
import binance.client as bc
import tensorflow as tf


ETH = "ETH"
BTC = "BTC"
HODL = "HODL"
holding = ETH


def login():
	client = bc.Client("","")

def getBetterCoin():
	#...........NN magic
	#...........
	return HODL #or
	return BTC #or
	return ETH 

def tradeEtoB(Price):
	order = client.order_market_sell(
		symbol="ETHBTC",
		quantity=client.get_asset_balance(asset=ETH))
	return

def tradeBtoE():
	order = client.order_market_buy(
		symbol="ETHBTC",
		quantity=client.get_asset_balance(asset=BTC))
	return




def main():

	login()

	while True:

		should_hold = getBetterCoin()
		

		if ( holding == ETH and should_hold == BTC ):
				tradeEtoB()
		if ( holding == BTC and should_hold == ETH ):
				tradeBtoE()

		sleep(5*60)



