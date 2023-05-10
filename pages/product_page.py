from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.press_button_add_to_basket()
        self.should_be_correct_name_in_message()
        self.should_be_basket_total_value_equal_product_price()
        self.solve_quiz_and_get_code()
    
    def press_button_add_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADDBSKT)
        btn_add_to_basket.click()
        
        
    def should_be_correct_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, "Product_name does not match product_name_in_message"
       

    def should_be_basket_total_value_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_value = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_VALUE).text
        assert product_price == basket_total_value, "Price incorrect in the basket"   
    
    