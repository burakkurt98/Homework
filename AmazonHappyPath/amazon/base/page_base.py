from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseClass(object):
    """Base class de  kullanılacak fonksiyonları çagiriyoruz"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 35)

    def wait_for_element(self, selector, index):
        """Bir elementin bulunması için gerekli websitesinin API sinin yüklenmesini bekliyor"""

        if index >= 0:
            return self.wait.until(ec.presence_of_all_elements_located(selector))[int(index)]
        return self.wait.until(ec.presence_of_all_elements_located(selector))

    def clicked(self, selector, index):
        """Bir elementin bulunması ve tıklanması işlevini yerine getirir"""

        self.wait_for_element(selector, index).click()

    def write_to_text(self, selector, text, index):
        """Elementi bulup gerekli metni yazdırmak"""

        web_element = self.wait_for_element(selector, index)
        web_element.send_keys(text)

    def window_scroll_page(self, yCoordinate):
        """Sayfa da kaydırma işlemini gerçekleştirir"""

        self.driver.execute_script("window.scrollTo(0, " + str(yCoordinate) + ")")

    def get_text(self, selector, index):
        """istenen metni almak için kullanılır"""

        element = self.wait.until(ec.presence_of_all_elements_located(selector))[int(index)]
        return element.text
