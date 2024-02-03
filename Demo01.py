from selenium import webdriver

chromedriver_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

driver = webdriver.Chrome(chromedriver_path)

driver.get("https://baidu.com/")

ele = driver.find_element('#kw')

ele.send_keys('你好')