from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import time

# Constants
login_url = "https://pro.zoopla.co.uk/professional/sign-in/"
data_page_url = "https://pro.zoopla.co.uk/reports/leads/email/looking-to-rent/?category=residential"
output_file = "zoopla_leads.xlsx"

# Your login credentials
username = ""  
password = ""           

# Path to ChromeDriver
chrome_driver_path = "/Users/fahad_ishaq1/Downloads/Images/Images_Website"  # Update if necessary

def login_and_download_excel():
    # Set up Chrome WebDriver
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds

    try:
        # Navigate to the login page
        driver.get(login_url)

        # Fill out the login form
        wait.until(EC.element_to_be_clickable((By.NAME, 'username'))).send_keys(username)
        wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(password + Keys.RETURN)
        
        # Wait for the login process to complete
        time.sleep(5)  # Adjust time if necessary

        # Navigate to the data page
        driver.get(data_page_url)

        # Refresh the page
        driver.refresh()
        time.sleep(3)  # Wait for page to load

        # Wait for the download link to be clickable
        download_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Download Excel")]')))
        
        # Get the URL of the Excel file
        excel_url = download_link.get_attribute('href')
        
        # Download the Excel file using requests
        session = requests.Session()
        for cookie in driver.get_cookies():
            session.cookies.set(cookie['name'], cookie['value'])
        
        response = session.get(excel_url)
        if response.status_code == 200:
            with open(output_file, 'wb') as file:
                file.write(response.content)
            print(f"Excel file downloaded successfully: {output_file}")
        else:
            print(f"Failed to download the file. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Quit the WebDriver
        driver.quit()

# Execute the function
login_and_download_excel()
