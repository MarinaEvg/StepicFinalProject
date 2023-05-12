from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"


@pytest.mark.need_review
#@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)   
    product_page.open() 
    product_page.press_button_add_to_basket()
    product_page.solve_quiz_and_get_code()
    time.sleep(5)
    product_page.should_be_correct_name_in_message()
    product_page.should_be_basket_total_value_equal_product_price()
    
@pytest.mark.xfail    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link) 
    product_page.open() 
    product_page.press_button_add_to_basket()
    product_page.should_not_be_success_message_isnt_elmnt_present()
    
    
def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link) 
    product_page.open() 
    product_page.should_not_be_success_message_isnt_elmnt_present()

@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link) 
    product_page.open() 
    product_page.press_button_add_to_basket()
    product_page.should_not_be_success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    
@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    basket_page = page.go_to_basket_page_from_product_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()

  
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()
        
        
    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link) 
        product_page.open() 
        product_page.should_not_be_success_message_isnt_elmnt_present()
    
    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)   
        product_page.open() 
        product_page.press_button_add_to_basket()
#       product_page.solve_quiz_and_get_code()
        time.sleep(5)
        product_page.should_be_correct_name_in_message()
        product_page.should_be_basket_total_value_equal_product_price()
