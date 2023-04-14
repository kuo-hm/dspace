from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure the webdriver to run in headless mode
options = webdriver.ChromeOptions()
chromedriver_path = 'chromedriver'

# Initialize the webdriver
driver = webdriver.Chrome(chromedriver_path, chrome_options=options)


# Navigate to the login page
driver.get('https://sbn.inpt.ac.ma/home')

# Wait for the login dropdown to appear
wait = WebDriverWait(driver, 30)
print('Waiting for the login dropdown to appear...')
login_dropdown = wait.until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/ds-app/ds-themed-root/ds-root/div/div/ds-themed-header-navbar-wrapper/ds-header-navbar-wrapper/div/ds-themed-header/ds-header/header/ds-themed-navbar/ds-navbar/nav/div/ds-themed-auth-nav-menu/ds-auth-nav-menu/ul/li/div/a')))
login_dropdown.click()

# Wait for the login form to appear
wait.until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/ds-app/ds-themed-root/ds-root/div/div/ds-themed-header-navbar-wrapper/ds-header-navbar-wrapper/div/ds-themed-header/ds-header/header/ds-themed-navbar/ds-navbar/nav/div/ds-themed-auth-nav-menu/ds-auth-nav-menu/ul/li/div/div/ds-log-in/div/ds-log-in-container/ds-log-in-password/form/input[1]')))

# Enter the email and password
email_field = driver.find_element(
    By.XPATH, '/html/body/ds-app/ds-themed-root/ds-root/div/div/ds-themed-header-navbar-wrapper/ds-header-navbar-wrapper/div/ds-themed-header/ds-header/header/ds-themed-navbar/ds-navbar/nav/div/ds-themed-auth-nav-menu/ds-auth-nav-menu/ul/li/div/div/ds-log-in/div/ds-log-in-container/ds-log-in-password/form/input[1]')
password_field = driver.find_element(
    By.XPATH, '/html/body/ds-app/ds-themed-root/ds-root/div/div/ds-themed-header-navbar-wrapper/ds-header-navbar-wrapper/div/ds-themed-header/ds-header/header/ds-themed-navbar/ds-navbar/nav/div/ds-themed-auth-nav-menu/ds-auth-nav-menu/ul/li/div/div/ds-log-in/div/ds-log-in-container/ds-log-in-password/form/input[2]')
email_field.send_keys('admin@inpt.ac.ma')
password_field.send_keys('xVX8XQ8HNbi9')

# Submit the login form
submit_button = driver.find_element(
    By.XPATH, '/html/body/ds-app/ds-themed-root/ds-root/div/div/ds-themed-header-navbar-wrapper/ds-header-navbar-wrapper/div/ds-themed-header/ds-header/header/ds-themed-navbar/ds-navbar/nav/div/ds-themed-auth-nav-menu/ds-auth-nav-menu/ul/li/div/div/ds-log-in/div/ds-log-in-container/ds-log-in-password/form/button')
submit_button.click()

# Wait for the redirect to complete
wait.until(EC.url_changes(driver.current_url))
# Wait for the page to load
# get the page screenshot
driver.save_screenshot('screenshot.png')
print('Screenshot saved to screenshot.png')
# print the
