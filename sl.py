from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(executable_path="./geckodriver")
driver = webdriver.Firefox(service=service)

driver.get("https://dev.to")