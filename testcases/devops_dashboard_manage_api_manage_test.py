# @author liruohao
# @create 2017-11-2

import os, sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from seleniumbase import BaseCase
from pages.devops_login_page import DevopsLoginPage
from pages.devops_dashboard_page import DevopsDashboardPage
import unittest
import time
import re


class DevopsDMApiManageTest(BaseCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = DevopsDashboardPage()

    # @unittest.skip('pass')
    def test_page_display(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAPIManage)
        self.assert_text('API网关配置', self.page.header)
        self.assert_element(self.page.tableBody)

    # @unittest.skip('pass')
    def test_table_order_desc(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAPIManage)
        try:
            time0 = self.get_text(self.page.tableTrApiTime0)
            time1 = self.get_text(self.page.tableTrApiTime1)
            assert time0 > time1
        except:
            time0 = self.get_text(self.page.tableTrApiTime0)
            assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time0)

    # @unittest.skip('pass')
    def test_table_detail(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAPIManage)
        try:
            _linkText = self.get_text(self.page.tableTrName0)
            _pathTable = self.get_text(self.page.tableTrPath)
            self.click_link_text(_linkText)
            time.sleep(0.1)
            _detailText = self.get_text(self.page.header)
            assert 'API配置详情' in _detailText
            self.assert_text(_pathTable, self.page.detailPath)
        except:
            self.assert_text(self.page.iconNoData)

    # @unittest.skip('pass')
    def test_new_config(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAPIManage)
        self.click(self.page.btnAddAPI)
        _now = str(int(time.time()))
        self.update_text_value(self.page.modalInputApiName, 'Name' + _now)
        self.update_text_value(self.page.modalInputApiGatePath, '/gatePath')
        self.update_text_value(self.page.modalInputApiSubPath, '/subPath')
        self.update_text_value(self.page.modalInputApiPath, '/apiPath')
        self.find_visible_elements(self.page.inputModalAutoComplete)[0].send_keys('ServName' + _now)
        self.click(self.page.modalDivSelect)
        self.find_visible_elements(self.page.modalDivOption)[-1].click()
        self.click(self.page.btnModalAccept)
        self.assert_element_not_visible(self.page.modalInputApiName)

    # @unittest.skip('pass')
    def test_search(self):
        DevopsLoginPage().login(self)
        self.click(self.page.menuAPIManage)
        _name = self.get_text(self.page.tableTrName0)[0:1]
        self.update_text_value(self.page.inputKeywordSearch, _name)
        self.click(self.page.btnSearch)
        try:
            assert _name in self.get_text(self.page.tableTrName1)
        except:
            assert _name in self.get_text(self.page.tableTrName0)


