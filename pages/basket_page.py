from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_is_empty()
        self.should_be_message_that_basket_is_empty()

    
    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMS_WITH_PRODUCTS), \
       "Basket is not empty, but should be empty"
       
    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), \
       "Message that basket is empty no, but should be"