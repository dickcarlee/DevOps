# @author liruohao
# @create 2017-10-31
from seleniumbase import BaseCase


class DevopsLoginPage:
    url = 'http://172.17.123.177:8080/'
    btnLogin = 'button.login-form-button'
    navigation = 'div.ant-menu-submenu-title'
    menuServiceInsertManage = "//a[contains(.,'服务接入配置')]"
    menuServiceMange = "//span[contains(.,'服务配置')]"
    inputUserName = 'input#userName'

    def login(self, _driver):
        _driver.maximize_window()
        _driver.open(self.url)
        _driver.update_text(self.inputUserName, 'pt')
        _driver.click(self.btnLogin)


