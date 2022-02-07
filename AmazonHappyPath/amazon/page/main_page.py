from selenium.webdriver.common.by import By
from amazon.base.page_base import BaseClass


class MainPage():
    """Ana Sayfada ki yapılıcak adımlar ile alakalı fonksiyonları barındırır"""

    SEARCH_TEXT = "samsung"
    SEARCH_BAR = (By.CSS_SELECTOR, "input[id='twotabsearchtextbox']")  # 0
    SIGN_IN_BTN = (By.CSS_SELECTOR, ".nav-line-1-container")  # 0
    SEARCH_IN_BTN = (By.CSS_SELECTOR, ".nav-right")  # 0

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def navigate_to_search(self):
        """Search alanına yazılan metni sayfada arar"""

        self.methods.write_to_text(self.SEARCH_BAR, self.SEARCH_TEXT, 0)
        self.methods.clicked(self.SEARCH_IN_BTN, 0)

    def navigate_to_login_page(self):
        """Giriş yapma sayfasına yönlendirilir"""

        self.methods.clicked(self.SIGN_IN_BTN, 0)
