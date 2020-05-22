import os,sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.dispaly_page import DisplayPage
import time

class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def test_mobile_display_input(self):
        self.display_page.click_show()
        self.display_page.click_return_key()

    def teardown(self):
        self.driver.quit()