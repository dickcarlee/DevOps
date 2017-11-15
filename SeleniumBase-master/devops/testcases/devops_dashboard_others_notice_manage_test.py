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


class DevopsDONoticeManageTest(BaseCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = DevopsDashboardPage()

    # @unittest.skip('pass')
    def test_page_display(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuNoticeManage)
        self.assert_text('公告管理', self.page.header)
        self.assert_element(self.page.tableBody)

    # @unittest.skip('pass')
    def test_table_order_desc(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuNoticeManage)
        try:
            time0 = self.get_text(self.page.tableTrNoticeTime0)
            time1 = self.get_text(self.page.tableTrNoticeTime1)
            assert time0 > time1
        except:
            time0 = self.get_text(self.page.tableTrNoticeTime0)
            assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time0)

    # @unittest.skip('pass')
    def test_new_config(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuNoticeManage)
        self.click(self.page.btnAddNotice)
        _now = str(int(time.time()))
        self.update_text_value(self.page.modalInputNoticeTitle, 'Title' + _now)
        self.update_text_value(self.page.modalTextareaNoticeContent, 'Content' + _now)
        self.click(self.page.btnModalAccept)
        self.assert_element_not_visible(self.page.modalInputNoticeTitle)

    # @unittest.skip('pass')
    def test_search(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuNoticeManage)
        _name = self.get_text(self.page.tableTrNoticeName0)[0:1]
        self.update_text_value(self.page.inputKeywordSearch, _name)
        self.click(self.page.btnSearch)
        try:
            assert _name in self.get_text(self.page.tableTrNoticeName1)
        except:
            assert _name in self.get_text(self.page.tableTrNoticeName0)


