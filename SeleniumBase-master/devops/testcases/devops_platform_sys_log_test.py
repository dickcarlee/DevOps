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


class DevopsPlatformLogTest(BaseCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = DevopsPlatformPage()

    # @unittest.skip('pass')
    def test_sys_config_render(self):
        DevopsLoginPage().login(self)
        self.click(self.page.btnPlatform)
        self.click(self.page.menuLog)
        self.assert_element(self.page.TableBody, timeout=3)

    # @unittest.skip('pass')
    def test_sys_config_order_desc(self):
        DevopsLoginPage().login(self)
        self.click(self.page.btnPlatform)
        self.click(self.page.menuLog)
        try:
            time0 = self.get_text(self.page.tableTdLogTime0)
            time1 = self.get_text(self.page.tableTdLogTime1)
            assert time0 > time1
        except:
            time0 = self.get_text(self.page.tableTdLogTime0)
            assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time0)

    # @unittest.skip('pass')
    def test_search(self):
        DevopsLoginPage().login(self)
        self.click(self.page.btnPlatform)
        self.click(self.page.menuLog)
        _name = self.get_text(self.page.tableTrLogName0)[0:1]
        self.update_text_value(self.page.inputKeywordSearch, _name)
        self.click(self.page.btnSearch)
        time.sleep(0.5)
        try:
            assert _name in self.get_text(self.page.tableTrLogName1)
        except:
            assert _name in self.get_text(self.page.tableTrLogName0)




