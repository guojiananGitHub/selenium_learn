from selenium import webdriver


def login(login_name, login_password):
    #   啟動Chrome
    driver = webdriver.Chrome()

    #   訪問登陸頁
    url = 'http://192.168.50.15:9001/'
    driver.get(url)

    inputLogin_name = driver.find_element_by_id("txtUserName")
    inputLogin_password = driver.find_element_by_id("txtPassword")
    login = driver.find_element_by_id('btnLogin')
    inputLogin_name.send_keys(login_name)
    inputLogin_password.send_keys(login_password)
    login.submit()