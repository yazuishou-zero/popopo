import os,sys

import pytest

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.search_page import SearchPage
from base.base_yml import yml_with_file

class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.search_page = SearchPage(self.driver)

    @pytest.mark.parametrize("content2",yml_with_file("search_data")["test_search"])
    def test_search(self,content2):
        #点击放大镜
        self.search_page.click_search()
        #输入文字
        self.search_page.input_content(content2)
        #点击返回
        self.search_page.click_back()































