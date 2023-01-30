# Configuration parameters
params = {
    "base_currency": "USDT",  # The base currency that the bot will traid on 
    "parts": ["AXS-USDT"],  # List of parts to be monitored
    "min_price": { "AXS-USDT":99999},  # Minimum price for each part
    "max_price": { "AXS-USDT":0},  # Minimum price for each part
    "is_bought": {"AXS-USDT":False},
    "percent_increase": 0.1,  #% Percentage increase that triggers a buy
    "percent_decrease": 0.1,  #% Percentage decrease that triggers a buy
    "funds_percentage": 10,  #% Percentage of funds to be used in the buy
    "time_step": 4 #s  the time to wait in seconds befor recalling the loop 
}

def load_config():
    return params
