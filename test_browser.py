import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver


@pytest.mark.usefixtures("test_launchbrowser")
class firstclass:
    def test_e2e(test_launchbrowser):
        lst = test_launchbrowser.find_elements(By.XPATH, "//input[@type='checkbox']")
        for i in lst:
            if i.get_attribute("value") == "option3":
                i.click()
            assert i.is_selected()
            break
        for j in lst:
            print(j.get_attribute("value"))
