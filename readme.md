. **Install Google Chrome**:
   - Download and install Google Chrome from Google Chrome: https://www.google.com/chrome/

4. **Download ChromeDriver**:
   - Download the ChromeDriver that matches your Chrome version from ChromeDriver: https://sites.google.com/chromium.org/driver/downloads

## Step-by-Step Setup and Execution

### Step 1: Install R Libraries

Open RStudio and run the following commands to install the necessary R libraries:

1. Install `devtools` if not already installed:
   ```r
   install.packages("devtools")
Install quantmod:

e
install.packages("quantmod")
Install kiteconnect3 from GitHub:


devtools::install_github("prodipta/kiteconnect3")

Step 2: Install Python Libraries
Open a terminal or command prompt and run the following commands to install the necessary Python libraries:

Install selenium:


pip install selenium
pip install webdriver-manager



pip install webdriver-manager

Step 3: Create and Run Initial R Script
Create a file named initial_script.R with the provided R code content.
Run initial_script.R in RStudio to generate the request_token_url.txt file.

Step 4: Create and Run Python Script to Automate Login
Create a file named automate_zerodha_login.py with the provided Python code content.
Run automate_zerodha_login.py:
Open a terminal or command prompt.
Navigate to the directory where automate_zerodha_login.py is located.
Run the script: python automate_zerodha_login.py.
Follow the prompts to enter the 2FA PIN manually.

Step 5: Create and Run Final R Script
Create a file named final_script.R with the provided R code content.
Run final_script.R in RStudio to perform the desired operations using the access token.