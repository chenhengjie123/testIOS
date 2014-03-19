from selenium import webdriver
import time

driver = webdriver.Chrome();
driver.get('http://www.baidu.com');

time.sleep(5);
print ('browser will be closed');
driver.quit(); # or driver.close()
print ('browser is closed');
