# Initial R Script

# Load required libraries
shared_library_path <- "/Volumes/Macintosh HD-1/Library/Frameworks/R.framework/Versions/4.2/Resources/library"
library(quantmod)
library(kiteconnect3)

# Define API key and secret
api_key <- "6xc2aj0w2xd02o6s"
api_secret <- "tohzo4r8iqmov9sh93r1lh9ibr69kxhe"

# Create connection object
kite = create_connection_object(list(api_key=api_key, api_secret=api_secret))

# Generate login URL
login_url = get_login_url(kite)
print(login_url) # Print the login URL to the console

# Save the login URL to a file
write(login_url, file = "request_token_url.txt")
