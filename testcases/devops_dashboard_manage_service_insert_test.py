# # @author liruohao
# # @create 2017-11-2

import os, sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from seleniumbase import BaseCase
from pages.devops_login_page import DevopsLoginPage
from pages.devops_dashboard_page import DevopsDashboardPage
import unittest
import time
import re

class DevopsDMServiceInsertTest(BaseCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = DevopsDashboardPage()

    # @unittest.skip('pass')
    def test_page_display(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuServiceInsertManage)
        self.assert_text('服务接入配置', self.page.header)
        self.assert_element(self.page.tableBody)

    # @unittest.skip('pass')
    def test_table_order_desc(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuServiceInsertManage)
        try:
            time0 = self.get_text(self.page.tableTrTime0)
            time1 = self.get_text(self.page.tableTrTime1)
            assert time0 > time1
        except:
            time0 = self.get_text(self.page.tableTrTime0)
            assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time0)


    # @unittest.skip('pass')
    def test_table_detail(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuServiceInsertManage)
        try:
            _linkText = self.get_text(self.page.tableTrName0)
            _ipTable = self.get_text(self.page.tableTrIP)
            self.click_link_text(_linkText)
            time.sleep(0.1)
            _detailText = self.get_text(self.page.header)
            assert '服务接入配置详情' in _detailText
            self.assert_text(_ipTable, self.page.detailIP)
        except:
            self.assert_element(self.page.iconNoData)


    # @unittest.skip('pass')
    def test_new_service(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuServiceInsertManage)
        self.click(self.page.btnAddService)
        _now = str(int(time.time()))
        self.update_text_value(self.page.modalInputServiceInsertServerName, 'Name' + _now)
        self.find_element(self.page.modalRadioServiceInsertNeedBalance)
        self.click(self.page.modalRadioServiceInsertNeedBalance)
        self.update_text_value(self.page.modalTextareaServiceInsertServerIP, '1.2.3.4')
        self.update_text_value(self.page.modalTextareaServiceInsertDescription, 'autoTestBy:LRH' + _now)
        self.click(self.page.btnModalAccept)
        self.assert_element_not_visible(self.page.modalInputServiceInsertServerName)

    # @unittest.skip('pass')
    def test_search(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuServiceInsertManage)
        _name = self.get_text(self.page.tableTrName0)[0:1]
        self.update_text_value(self.page.inputKeywordSearch, _name)
        self.click(self.page.btnSearch)
        try:
            assert _name in self.get_text(self.page.tableTrName1)
        except:
            assert _name in self.get_text(self.page.tableTrName0)


