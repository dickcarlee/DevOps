# @author liruohao
# @create 2017-10-31

import os, sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from seleniumbase import BaseCase
from pages.devops_login_page import DevopsLoginPage
import time


class DevopsLoginTest(BaseCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = DevopsLoginPage()

    def test_login(self):
        self.page.login(self)
        self.assert_element(self.page.navigation, timeout=5)

    def test_login_menu_auto_unfold(self):
        self.page.login(self)
        self.maximize_window()
        self.assert_element(self.page.menuServiceInsertManage, timeout=3)

    def test_login_menu_fold(self):
        self.page.login(self)
        self.set_window_size(600, 800)
        self.assert_element_not_visible(self.page.menuServiceInsertManage, timeout=3)

