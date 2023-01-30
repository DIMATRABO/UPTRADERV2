import config, monitor, time



# Initialize variables
config_params = config.load_config()
stop = False



def initialize_min_prices(config_params):
    
    for part in config_params["parts"]:

        current_price = monitor.get_price(part)
        config_params["min_price"][part] = current_price
        
    return config_params







initialize_min_prices(config_params)
# Run the while loop
while True:

    try:
        # Start monitoring prices
        monitor.start_monitoring(config_params)
        
    except Exception as e:
        # Log any errors that occur
        print(e)
  
    time.sleep(config_params["time_step"])
    