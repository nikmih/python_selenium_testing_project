from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_elements(*ProductPageLocators.ALLERTS_SUCCESS_LIST)[0].text  , "Prodict was not added"