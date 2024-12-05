from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()

options.add_argument("start-maximized")  # Start with a maximized window
options.add_argument("--disable-popup-blocking")  # Allow popups
options.add_argument("--incognito")  # Use incognito mode

 # Additional options to help avoid detection
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")  # Mimic a regular user


# Set up WebDriver
service = Service("C:\\Windows\\WebDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)


try:
    # Step 1: Navigate to the ixigo login page
    print("Step: Navigating to the ixigo login page...")
    driver.get("https://www.ixigo.com/login")
    time.sleep(3)
    
    # Step 2: Wait for the iframe to load
    print("Step: Waiting for iframe to load...")
    wait = WebDriverWait(driver, 20)
    iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='googleLogin']//iframe")))
    # print("Iframe located:", iframe)

    # print(driver.page_source) 

    # Step 3: Switch to the iframe
    print("Step: Switching to iframe...")
    driver.switch_to.frame(iframe)
    
    # Step 4: Locate and click the Google Sign-In button
    print("Step: Locating Google Sign-In button...")
    google_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div/div[2]/span[1]")))
    # print("Google button located:", google_button)

    
    print("Step: Clicking Google Sign-In button...")
    google_button.click()


    # Step 5: Handle new window or tab
    print("Step: Handling new window/tab...")
    original_window = driver.current_window_handle  # Store the ID of the original window

    time.sleep(5)

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))  # Ensure the new window/tab opens

    # Switch to the new window or tab
    new_window = [window for window in driver.window_handles if window != original_window][0]
    driver.switch_to.window(new_window)
    # print("Switched to new window:", new_window)

    time.sleep(5)

    # Step 6: Handle Google Sign-In in the new window
    print("Step: Performing actions in the new Google Sign-In window...")
    
    # Wait for the email input field to appear
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
    print("Email input located.")
    email_input.send_keys("<__YOUR_EMAIL_HERE__>")  # Replace with your test email
    email_input.send_keys(Keys.RETURN)


    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")))
    print("password input located.")
    password_input.send_keys("<__YOUR_PASSWORD_HERE__>")  # Replace with your test password
    password_input.send_keys(Keys.RETURN)
    time.sleep(10)


    name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div/div/div/div/div[2]/div/div[3]/div/div/input")))
    phonenumber_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div/div/div/div/div[2]/div/div[4]/span[2]/input")))

    print("filling out details")
    name_field.send_keys("<__YOUR_NAME_HERE__>")
    phonenumber_field.send_keys("<__YOUR_PHONE_NUMBER_HERE__>")

    time.sleep(15)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    print("Step: Closing the browser...")
    driver.quit()
