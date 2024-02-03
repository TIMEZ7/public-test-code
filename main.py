from selenium import webdriver

chromedriver_path = r"C:\Users\AppData\Local\Google\Chrome\Application\chromedriver.exe"

driver = webdriver.Chrome(chromedriver_path)

driver.get("https://baidu.com/")