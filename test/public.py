class Login():

    def user_login(self,driver,username,password):
        print(driver.current_url)
        #定位其中的iframe并切进去
        driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        #登录
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_id("dologin").click()
        #从frame中切回主文档
        #driver.switch_to_default_content()
        driver.switch_to.default_content()
        


    def user_logout(self,driver):
        print(driver.current_url)
        #退出
        driver.find_element_by_link_text("退出").click()
        driver.quit()