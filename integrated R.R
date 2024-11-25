# Integrated R Script

# Load required libraries
library(quantmod)
require(kiteconnect3)
library(reticulate)

# Define paths and API details
path_name <- dirname(rstudioapi::getSourceEditorContext()$path)
api_key <- "6xc2aj0w2xd02o6s"
api_secret <- "tohzo4r8iqmov9sh93r1lh9ibr69kxhe"

# Create connection object
kite <- create_connection_object(list(api_key=api_key, api_secret=api_secret))

# Get the login URL and save it to a file
login_url <- get_login_url(kite)
writeLines(login_url, "request_token_url.txt")

# Run the Python script to automate login and extract tokens
use_condaenv(condaenv = 'my_env', required = TRUE)  # Replace 'my_env' with your actual conda environment name
source_python("automate_zerodha_login.py")

# Read the request token from the file
request_token <- readLines("request_token.txt")

# Set the request token
kite <- set_request_token(kite, request_token)

# Fetch the access token
kite <- fetch_access_token(kite)

# Save the access token
saveRDS(kite, paste0(path_name, "/kite_access_token.rds"))

# Load the saved access token
kite <- readRDS(paste0(path_name, "/kite_access_token.rds"))

# Fetch orders
orders <- get_orders(kite)
print(orders)

# Place an order (example)
order_id <- place_order(kite, exchange="NSE", tradingsymbol="RELIANCE", transaction_type="BUY", quantity=1, order_type="MARKET", product="CNC")
print(order_id)

# Fetch positions
positions <- get_positions(kite)
print(positions)

# Fetch holdings
holdings <- get_holdings(kite)
print(holdings)

# Fetch market quotes
quotes <- get_quote(kite, c("NSE:TCS", "BSE:TCS"))
print(quotes)

# Fetch historical price data (example)
historical_data <- get_historical_price(kite, "NSE:RELIANCE", "2023-01-01", "2023-12-31", "day")
print(historical_data)

# Fetch instruments
instruments <- get_instruments(kite, "NSE")
print(instruments)

# Save data or further operations as needed
saveRDS(orders, paste0(path_name, "/orders.rds"))
saveRDS(positions, paste0(path_name, "/positions.rds"))
saveRDS(holdings, paste0(path_name, "/holdings.rds"))
saveRDS(quotes, paste0(path_name, "/quotes.rds"))
saveRDS(historical_data, paste0(path_name, "/historical_data.rds"))
saveRDS(instruments, paste0(path_name, "/instruments.rds"))
