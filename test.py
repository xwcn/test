from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
print("hello, test!")

driver = webdriver.Remote(
	command_executor='http://selenium-hub:4444/wd/hub',
	desired_capabilities=DesiredCapabilities.CHROME)

print("Driver is created!")

driver.get("http://www.python.org")
print(driver.title)
assert "Python" in driver.title
driver.close()
