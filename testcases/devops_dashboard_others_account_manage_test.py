# @author liruohao
# @create 2017-11-13
import os
import sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from seleniumbase import BaseCase
from pages.devops_dashboard_page import DevopsDashboardPage
from pages.devops_login_page import DevopsLoginPage
import unittest
import time
from selenium.webdriver.common.keys import Keys
import re


class DevopsDOAccountManageTest(BaseCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = DevopsDashboardPage()

    # @unittest.skip('pass')
    def test_page_display(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAccountManage)
        self.assert_text('业务方账号', self.page.header)
        self.assert_element(self.page.tableBody)

    # @unittest.skip('pass')
    def test_table_order_desc(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAccountManage)
        try:
            time0 = self.get_text(self.page.tableTrAccountTime0)
            time1 = self.get_text(self.page.tableTrAccountTime1)
            assert time0 > time1
        except:
            time0 = self.get_text(self.page.tableTrAccountTime0)
            assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time0)

    # @unittest.skip('pass')
    def test_new_config(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAccountManage)
        self.click(self.page.btnAddAccount)
        _now = str(int(time.time()))
        self.find_element(self.page.inputModalAutoComplete).click()
        self.find_element(self.page.inputModalAutoComplete).send_keys(Keys.ENTER)
        self.update_text_value(self.page.modalInputAccountName, 'Name' + _now)
        self.click(self.page.modalButtonAccountGenerate)
        self.click(self.page.btnModalAccept)
        self.assert_element_not_visible(self.page.modalInputAccountName)

    # @unittest.skip('pass')
    def test_search(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAccountManage)
        _name = self.get_text(self.page.tableTrName0)[0:1]
        self.update_text_value(self.page.inputKeywordSearch, _name)
        self.click(self.page.btnSearch)
        try:
            assert _name in self.get_text(self.page.tableTrName1)
        except:
            assert _name in self.get_text(self.page.tableTrName0)


