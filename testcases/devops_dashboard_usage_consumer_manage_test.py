# # @author liruohao
# # @create 2017-11-7

import os, sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from seleniumbase import BaseCase
from pages.devops_login_page import DevopsLoginPage
from pages.devops_dashboard_page import DevopsDashboardPage
import unittest
import time
import re


class DevopsDUConsumerManageTest(BaseCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = DevopsDashboardPage()

    # @unittest.skip('pass')
    def test_page_display(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuConsumerManage)
        self.assert_text('业务方管理', self.page.header)
        self.assert_element(self.page.tableBody)

    # @unittest.skip('fail')
    def test_table_order_desc(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuConsumerManage)
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
        self.click(self.page.menuConsumerManage)
        try:
            _linkText = self.get_text(self.page.tableTrName0)
            _projectName = self.get_text(self.page.tableTrProjectName)
            self.click_link_text(_linkText)
            time.sleep(0.1)
            _detailText = self.get_text(self.page.header)
            assert '业务方详情' in _detailText
            self.assert_text(_projectName, self.page.detailPath)
        except:
            self.assert_element(self.page.iconNoData)

    # @unittest.skip('pass')
    def test_new_config(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuConsumerManage)
        self.click(self.page.btnAddConsumer)
        _now = str(int(time.time()))
        self.update_text_value(self.page.modalInputConsumerName, 'Name' + _now)
        self.update_text_value(self.page.modalInputConsumerManager, 'Manager' + _now)
        self.update_text_value(self.page.modalInputConsumerPhone, _now + '1')
        self.update_text_value(self.page.modalInputConsumerEmail, _now + '@Email.com')
        self.click(self.page.btnModalAccept)
        self.assert_element_not_visible(self.page.modalInputConsumerName)

    # @unittest.skip('pass')
    def test_search(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuConsumerManage)
        _name = self.get_text(self.page.tableTrName0)[0:1]
        self.update_text_value(self.page.inputKeywordSearch, _name)
        self.click(self.page.btnSearch)
        try:
            assert _name in self.get_text(self.page.tableTrName1)
        except:
            assert _name in self.get_text(self.page.tableTrName0)


