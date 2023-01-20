import kucoin_api , config, time 


config_params = config.load_config()

#print(kucoin_api.execute_buy_order("LUNC-USDT",191319, 0.0002))

#print(kucoin_api.get_tick_size("LUNC-USDT"))

#precision = kucoin_api.get_precision("LUNC")
#price = kucoin_api.get_price("LUNC-USDT")
#available = kucoin_api.get_available_funds("USDT")
#print(precision)
#print(price)
#print(available)
#print(round(available / price , precision))

#print( kucoin_api.set_stop_loss_take_profit("LUNC-USDT" , 0.00011, 0.0002 , 191319))



#print(100/kucoin_api.get_base_min_size("BTC-USDT"))
#print(precision)

#current_timestamp = int(time.time())

#print(kucoin_api.get_klines("BTC-USDT","5min" , str( current_timestamp -( 15 * 60 )) ,str(current_timestamp)))


#print(kucoin_api.get_prices(config_params["parts"]))



"""

response = kucoin_api.set_stop_loss_take_profit("XRP-USDT" , 0.2 , 0.4 , 0.536)
print(response)

print(kucoin_api.get_order_by_id(response["data"]["orderId"]))

config_params["stop_order_id"]["ETH-USDT"] = "vs8t6ou9eg1e32vq000lknj9"
print(monitor.stop_order_open("ETH-USDT" , config_params))

"""
print(kucoin_api.get_tick_size("ETH"))