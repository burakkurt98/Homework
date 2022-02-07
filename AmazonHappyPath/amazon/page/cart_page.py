from selenium.webdriver.common.by import By
from amazon.base.page_base import BaseClass


class CartPage():
    """Kart Sayfasında işlemler gerçekleştirir"""

    DELETE_BTN = (By.CSS_SELECTOR, ".a-button-input.a-declarative")  # 1
    PRODUCT_NAME = (By.CSS_SELECTOR, ".a-row.a-size-small")  # 0
    DELETE_TEXT = (By.CSS_SELECTOR, "span[data-action='reg-item-delete-undo']")  # 0

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def delete_item_from_cart(self):
        """Seçilen ürün silinir"""

        self.methods.window_scroll_page(100)
        self.methods.clicked(self.DELETE_BTN, 1)

    def get_cart_product_name(self):
        """WEBSİTESİ ÜZERİNDEN İSTENEN METİNLERİ ALMAK İÇİN KULLANILIR"""

        return self.methods.get_text(self.PRODUCT_NAME, 0)

    def get_delete_text(self):
        """WEBSİTESİ ÜZERİNDEN İSTENEN METİNLERİ ALMAK İÇİN KULLANILIR"""

        return self.methods.get_text(self.DELETE_TEXT, 0)
