from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def is_basket_empty(self):
        self.should_basket_empty_text_present()
        self.should_not_exist_items_list()

    def should_basket_empty_text_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), "'Basket is empty' text is not present"
        assert True
        
    def should_not_exist_items_list(self):
        assert not self.is_element_present(*BasketPageLocators.ITEMS_LIST), "There are items in basket"
        assert True
        
