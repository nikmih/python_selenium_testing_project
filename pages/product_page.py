from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code() 
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is not presented after product was added to the basket"
    
    def is_not_succcess_message_presented(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented"
    
    def is_not_succcess_message_disappeared(self): 
        assert not self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is dissapeared"
    
