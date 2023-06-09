from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

path = '/Users/.../chromedriver'  # your path goes here
service = Service(executable_path=path)
website =  # your link goes here
driver = webdriver.Chrome(service=service)

fields = ['Name', 'Email', 'Address', 'Phone number', 'Comments']
data = ['Frank', 'frank@example.com', '123 St', '987654321', 'Hello World']
my_form = dict(zip(fields, data))

driver.get(website)
time.sleep(3)

for field, data in my_form.items():
    text_input = driver.find_element(by='xpath',
                                     value=f'//div[contains(@data-params, "{field}")]//textarea | '
                                           f'//div[contains(@data-params, "{field}")]//input')
    text_input.send_keys(data)

submit_button = driver.find_element(by='xpath', value='//div[@role="button"]//span[text()="Submit"]')
submit_button.click()

time.sleep(1)
driver.quit()
