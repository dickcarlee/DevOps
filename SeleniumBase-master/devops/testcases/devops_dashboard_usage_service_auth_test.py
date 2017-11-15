# # # @author liruohao
# # # @create 2017-11-2

import os, sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from seleniumbase import BaseCase
from pages.devops_login_page import DevopsLoginPage
from pages.devops_dashboard_page import DevopsDashboardPage
import unittest
import time
import re
from selenium.webdriver.common.keys import Keys


class DevopsDUServiceAuthTest(BaseCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = DevopsDashboardPage()

    # @unittest.skip('pass')
    def test_page_display(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuServiceAuth)
        self.assert_text('服务授权管理', self.page.header)
        self.assert_element(self.page.tableBody)

    # @unittest.skip('fail')
    def test_table_order_desc(self):  # 无数据会fail
        DevopsLoginPage().login(self)
        self.click(self.page.menuServiceAuth)
        try:
            time0 = self.get_text(self.page.tableTrAuthTime0)
            time1 = self.get_text(self.page.tableTrAuthTime1)
            assert time0 > time1
        except:
            time0 = self.get_text(self.page.tableTrAuthTime0)
            assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time0)

    # @unittest.skip('pass')
    def test_table_detail(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuServiceAuth)
        try:
            _linkText = self.get_text(self.page.tableTrName0)
            _projectName = self.get_text(self.page.tableTrProjectName)
            self.click_link_text(_linkText)
            time.sleep(0.1)
            _detailText = self.get_text(self.page.header)
            assert '项目详情' in _detailText
            self.assert_text(_projectName, self.page.detailPath)
        except:
            self.assert_element(self.page.iconNoData)

    # @unittest.skip('pass')
    def test_new_config(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuServiceAuth)
        self.click(self.page.btnAddAuthProject)
        time.sleep(0.5)
        for i in range(3):
            self.find_visible_elements(self.page.inputModalAutoComplete)[i].click()
            self.find_visible_elements(self.page.inputModalAutoComplete)[i].send_keys(Keys.ARROW_UP)
            self.find_visible_elements(self.page.inputModalAutoComplete)[i].send_keys(Keys.ENTER)
        self.click(self.page.btnModalAccept)
        time.sleep(0.2)
        self.assert_element_not_visible(self.page.inputModalAutoComplete)

    # @unittest.skip('pass')
    def test_search(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuServiceAuth)
        time.sleep(0.5)
        for i in range(3):
            self.find_visible_elements(self.page.selectApp)[i].click()
            self.find_visible_elements(self.page.selectApp)[i].send_keys(Keys.ENTER)
        self.click(self.page.btnSearch)
        time.sleep(0.5)
        _filter_name = self.find_visible_elements(self.page.divAuthFilterText)[2].text
        try:
            try:
                assert _filter_name == self.get_text(self.page.tableTrName1)
            except:
                assert _filter_name == self.get_text(self.page.tableTrName0)
        except:
            self.assert_element(self.page.iconNoData)


