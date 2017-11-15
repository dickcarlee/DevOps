# # @author liruohao
# # @create 2017-11-7
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


class DevopsDUAppManageTest(BaseCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = DevopsDashboardPage()

    # @unittest.skip('pass')
    def test_page_display(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAppManage)
        self.assert_text('应用管理', self.page.header)
        self.assert_element(self.page.tableBody)

    # @unittest.skip('pass')
    def test_table_order_desc(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAppManage)
        try:
            time0 = self.get_text(self.page.tableTrAppManageTime0)
            time1 = self.get_text(self.page.tableTrAppManageTime1)
            assert time0 > time1
        except:
            time0 = self.get_text(self.page.tableTrAppManageTime0)
            assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time0)

    # @unittest.skip('pass')
    def test_table_detail(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAppManage)
        try:
            _linkText = self.get_text(self.page.tableTrName0)
            _clientId = self.get_text(self.page.tableTrAppClientId)
            self.click_link_text(_linkText)
            time.sleep(0.2)
            _detailText = self.get_text(self.page.header)
            assert '应用详情' in _detailText
            self.assert_text(_clientId, self.page.detailPath)
        except:
            self.assert_element(self.page.iconNoData)

    # @unittest.skip('pass')
    def test_new_config(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAppManage)
        self.click(self.page.btnAddApp)
        _now = str(int(time.time()))
        for i in range(2):
            time.sleep(0.5)
            _element = self.find_visible_elements(self.page.inputModalAutoComplete)[i]
            _element.click()
            _element.send_keys(Keys.ENTER)
        for i in range(-2, 0):
            time.sleep(0.5)
            _element = self.find_visible_elements(self.page.selectModal)[i]
            _element.click()
            _element.send_keys(Keys.ENTER)
        self.update_text_value(self.page.modalInputAppName, 'Name' + _now)
        self.click(self.page.btnModalAccept)
        self.assert_element_not_visible(self.page.modalInputAppName)

    # @unittest.skip('pass')
    def test_search(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAppManage)
        _name = self.get_text(self.page.tableTrName0)[0:1]
        self.update_text_value(self.page.inputKeywordSearch, _name)
        self.click(self.page.btnSearch)
        try:
            assert _name in self.get_text(self.page.tableTrName1)
        except:
            assert _name in self.get_text(self.page.tableTrName0)


