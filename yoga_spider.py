from selenium import webdriver

url1 = 'https: // www.24hourfitness.com/utility/classes /?clubid = 00352'

driver = webdriver.Chrome()
driver.get(url1)
print driver.title