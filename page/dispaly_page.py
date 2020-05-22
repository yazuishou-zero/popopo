import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class DisplayPage(BaseAction):
    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    search_button = By.ID, "com.android.settings:id/search"
    search_edit_text = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.click(self.display_button)

    def click_show(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'亮度')]").click()

    def click_return_key(self):
        for i in range(3):
            self.driver.press_keycode(4)
            time.sleep(1)

    """
        # dispaly_button = By.XPATH, "//*[contains(@text,'显示')]"
        # dispaly_button = By.ID, "com.android.settings:id/title"
        # dispaly_button = By.XPATH, "//*[contains(@text,'显示')]"
        # variability_button = By.XPATH, "//*[contains(@text,'亮度')]"


        def __init__(self, driver):
            BaseAction.__init__(self,driver)
            self.driver = driver
            BaseAction.click(driver.find_element_by_xpath("//*[contains(@text,'显示')]"))
            # self.driver.find_element(By.XPATH,self.dispaly_button).click()
            # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
    """