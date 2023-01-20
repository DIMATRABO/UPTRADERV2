# Configuration parameters
params = {
    "base_currency": "USDT",  # The base currency that the bot will traid on 
    "parts": ["BTC-USDT", "ETH-USDT", "XRP-USDT"],  # List of parts to be monitored
    "min_price": {"BTC-USDT": 0, "ETH-USDT": 0, "XRP-USDT": 0},  # Minimum price for each part
    "stop_order_id": {"BTC-USDT": None, "ETH-USDT": None, "XRP-USDT": None},
    "percent_increase": 0.5,  #% Percentage increase that triggers a buy
    "funds_percentage": 50,  #% Percentage of funds to be used in the buy
    "stop_loss_percentage": 1, #% Stop loss percentage
    "take_profit_percentage": 2 ,#% Take profit percentage
    "stop": False,  # Whether or not the bot should stop running
    "time_step": 1 # the time to wait in seconds befor recalling the loop 
}

def load_config():
    return params
