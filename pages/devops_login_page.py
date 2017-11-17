# @author liruohao
# @create 2017-10-31
from seleniumbase import BaseCase
import time

class DevopsLoginPage:
    url = 'http://172.17.123.177:8080/'
    btnLogin = 'button.login-form-button'
    navigation = 'div.ant-menu-submenu-title'
    menuServiceInsertManage = "//a[contains(.,'服务接入配置')]"
    menuServiceMange = "//span[contains(.,'服务配置')]"
    inputUserName = 'input#userName'
    inputPassword = 'input#password'


    def login(self, _driver):
        _driver.maximize_window()
        _driver.open(self.url)
        _driver.update_text(self.inputUserName, 'pt')
        _driver.update_text(self.inputPassword, '123456')
        _driver.click(self.btnLogin)
        time.sleep(1)

