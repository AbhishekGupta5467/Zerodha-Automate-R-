from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import os
from urllib.parse import unquote
import pandas as pd
import pyotp

# Zerodha credentials provided by your client
user_id = "KNM560"  # Replace with your user ID
password = "Abhishek7421@"  # Replace with your password
pin = "your_2FA_PIN"  # Replace with your 2FA PIN

# Path to your GeckoDriver
GECKODRIVER_PATH = r"D:\geckodriver.exe"

# Full path to the request token URL file
REQUEST_TOKEN_URL_FILE = r"D:\BIKASH\iNTERACTIVE BROKER API\request_token_url.txt"

# Configure Firefox options
firefox_options = FirefoxOptions()
firefox_options.add_argument("--disable-notifications")
# Uncomment the next line to run Firefox in headless mode
# firefox_options.add_argument("--headless")

# Initialize the WebDriver (Firefox) with explicit service configuration
service = FirefoxService(executable_path=GECKODRIVER_PATH)
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open Zerodha login page
driver.get("https://kite.zerodha.com/")

# Enter user ID
user_id_field = driver.find_element(By.ID, "userid")
user_id_field.send_keys(user_id)

# Enter password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)

# Click on the login button
login_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div/form/div[4]/button')
login_button.click()

# Enter 2FA PIN
time.sleep(2)  # Wait for 2FA page to load
pin_field = driver.find_element(By.ID, "pin")
pin_field.send_keys(pin)
continue_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div/form/div[3]/button')
continue_button.click()

# Read the request token URL from the file
with open(REQUEST_TOKEN_URL_FILE, "r") as file:
    request_token_url = file.read().strip()

print(f"Request Token URL: {request_token_url}")

# Open the request token URL
driver.get(request_token_url)

# Wait for the request token to be present in the URL (assuming it redirects)
time.sleep(10)  # Adjust the sleep time if needed to wait for the URL to change

# Get the new URL from the browser
new_url = driver.current_url
print(f"New URL: {new_url}")

# Extract the request token from the URL
try:
    if "request_token=" in new_url:
        request_token = new_url.split("request_token=")[1].split("&")[0]
        # Save the request token to a file
        with open("request_token.txt", "w") as file:
            file.write(request_token)
        print("Request token saved successfully.")
    else:
        print("Request token not found in the URL. Please check the URL format.")
except IndexError:
    print("Request token not found in the URL. Please check the URL format.")

# Source the entoken from the Zerodha page (example code)
try:
    driver.get("https://kite.zerodha.com/dashboard")
    time.sleep(5)  # Adjust the sleep time to ensure the dashboard loads

    # Example: Find the entoken from the page source or cookies
    cookies = driver.get_cookies()
    for cookie in cookies:
        if cookie['name'] == 'enctoken':
            entoken = cookie['value']
            with open("entoken.txt", "w") as file:
                file.write(entoken)
            print("Entoken saved successfully.")
            break
except Exception as e:
    print(f"Error sourcing entoken: {e}")

# Load URLs from Excel file
excel_file = '/Volumes/R code stocks/2. Zerodha_Derivative/Urls.xlsx'
df = pd.read_excel(excel_file, sheet_name='Sheet1', header=None)
getlist = df[0].tolist()

# Process each URL
for i in range(len(getlist)):
    driver.get(getlist[i])
    time.sleep(5)  # Increase the waiting time here
    iframe = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//iframe[@id='chart-iframe']")))
    driver.switch_to.frame(iframe)
    
    e = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//cq-toggle[@class='ciq-DT tableview-ui']//span")))
    e.click()
    
    name = getlist[i].split("/")[-2]
    decoded_name = unquote(name)
    locals()[decoded_name.replace(' ', '_')] = pd.read_html(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//table[@class='header-fixed']"))).get_attribute('outerHTML'))[0]
    
    e.click()
    driver.switch_to.default_content()

# Save data to TSV files
save_folder11 = os.path.join('/Volumes/', 'R code stocks/2. Zerodha_Derivative/Renko_zerodha_index_NIFTY50_c.tsv')
save_folder12 = os.path.join('/Volumes/', 'R code stocks/2. Zerodha_Derivative/Renko_zerodha_index_NIFTYBANK_c.tsv')

save_folder21 = os.path.join('/Volumes/', 'R code stocks/2. Zerodha_Derivative/Renko_zerodha_index_NIFTY50_p.tsv')
save_folder22 = os.path.join('/Volumes/', 'R code stocks/2. Zerodha_Derivative/Renko_zerodha_index_NIFTYBANK_p.tsv')

# Assuming `NIFTY_50` and `NIFTY_BANK` are dataframes obtained from the above URLs
prev_nifty = pd.read_csv(save_folder11, sep='\t')
prev_nifty.to_csv(save_folder21, sep='\t', index=False)

prev_niftybank = pd.read_csv(save_folder12, sep='\t')
prev_niftybank.to_csv(save_folder22, sep='\t', index=False)

NIFTY_50.to_csv(save_folder11, sep='\t', index=False)
NIFTY_BANK.to_csv(save_folder12, sep='\t', index=False)

# Keep the browser session open
print("Browser session will remain open. Do not close this window to keep the session active.")
input("Press Enter to terminate the session (only when necessary).")

# Close the browser when done (if required)
# driver.quit()
