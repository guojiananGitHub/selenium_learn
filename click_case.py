from selenium import webdriver
from login import login

#   輸入帳號密碼並登錄
login('guojianan', '123456')

#   /html/body/div[3]/ul/li/div[1]/div[1]/ul/li[1]/ul/li[2]/a/em
#   /html/body/div[3]/ul/li/div[1]/div[1]/ul/li[1]/ul/li[2]/a/em/i
driver = webdriver.Chrome()
a = driver.find_element_by


