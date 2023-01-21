# Configuration parameters
params = {
    "base_currency": "USDT",  # The base currency that the bot will traid on 
    "parts": ["BTC-USDT", "ETH-USDT", "XRP-USDT" , "AXS-USDT"],  # List of parts to be monitored
    "min_price": {"BTC-USDT": 99999, "ETH-USDT": 99999, "XRP-USDT": 99999 , "AXS-USDT":99999},  # Minimum price for each part
    "max_price": {"BTC-USDT": 0, "ETH-USDT": 0, "XRP-USDT": 0 , "AXS-USDT":0},  # Minimum price for each part
    "is_bought": {"BTC-USDT": False, "ETH-USDT": True, "XRP-USDT": False , "AXS-USDT": False},
    "percent_increase": 0.1,  #% Percentage increase that triggers a buy
    "percent_decrease": 0.1,  #% Percentage decrease that triggers a buy
    "funds_percentage": 10,  #% Percentage of funds to be used in the buy
    "time_step": 4 #s  the time to wait in seconds befor recalling the loop 
}

def load_config():
    return params
