import config, monitor, logging, time


# Configure logging
logging.basicConfig(filename='bot_errors.log', level=logging.ERROR)

# Initialize variables
config_params = config.load_config()
stop = False



def initialize_min_prices(config_params):
    
    for part in config_params["parts"]:

        current_price = monitor.get_price(part)
        config_params["min_price"][part] = current_price
        
    return config_params


# Implement the stop function
def stop_function_called():
    return config_params["stop"] == "stop"

# Log any errors
def log_error(e):
    logging.error(e)




initialize_min_prices(config_params)
# Run the while loop
while not stop:

    try:
        # Start monitoring prices
        monitor.start_monitoring(config_params)
        
    except Exception as e:
        # Log any errors that occur
        log_error(e)
    # Check if the stop function has been called
    if stop_function_called():
        stop = True
    time.sleep(config_params["time_step"])
    