from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the login page
driver.get("https://www.example.com/login")

# Find the username and password inputs and enter the credentials
username = driver.find_element_by_name("username")
username.send_keys("your_username")
password = driver.find_element_by_name("password")
password.send_keys("your_password")

# Find the submit button and click it
submit_button = driver.find_element_by_xpath('//input[@type="submit"]')
submit_button.click()

# Wait for the page to load, then check if the user is logged in
# (e.g. by checking if the username is displayed on the page)
# Add your own logic here

# Close the browser window
driver.quit()