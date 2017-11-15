# @author liruohao
# @create 2017-11-1

import os, sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from seleniumbase import BaseCase
from pages.devops_login_page import DevopsLoginPage
from pages.devops_platform_page import DevopsPlatformPage
import time
import unittest
import re


class DevopsPlatformSysConfigTest(BaseCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = DevopsPlatformPage()

    # @unittest.skip('pass')
    def test_sys_config_render(self):
        DevopsLoginPage().login(self)
        self.click(self.page.btnPlatform)
        self.click(self.page.menuSysConfig)
        self.assert_element(self.page.TableBody, timeout = 3)

    # @unittest.skip('pass')
    def test_sys_config_order_desc(self):
        DevopsLoginPage().login(self)
        self.click(self.page.btnPlatform)
        self.click(self.page.menuSysConfig)
        try:
            time0 = self.get_text(self.page.tableTdSysConfigTime0)
            time1 = self.get_text(self.page.tableTdSysConfigTime1)
            assert time0 > time1
        except:
            time0 = self.get_text(self.page.tableTdSysConfigTime0)
            assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time0)

    # @unittest.skip('pass')
    def test_sys_config_new_config(self):
        DevopsLoginPage().login(self)
        self.click(self.page.btnPlatform)
        self.click(self.page.menuSysConfig)
        self.click(self.page.btnNewSys)
        _now = str(int(time.time()))
        self.update_text_value(self.page.inputName, 'Name' + _now)
        self.update_text_value(self.page.inputAccountName, 'Account' + _now)
        self.update_text_value(self.page.textareaAccessIps, '1.2.3.4')
        self.update_text_value(self.page.textareaDescription, 'autoTestBy:LRH' + _now)
        self.click(self.page.btnModelAccept)
        self.assert_element_not_visible(self.page.inputName)

    # @unittest.skip('pass')
    def test_sys_config_freeze(self):
        DevopsLoginPage().login(self)
        self.click(self.page.btnPlatform)
        self.click(self.page.menuSysConfig)
        time.sleep(0.5)
        self.click(self.page.btnFreeze)
        self.click(self.page.btnModelAccept)



