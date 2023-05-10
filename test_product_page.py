from .pages.product_page import ProductPage
import pytest
import time


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])


def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    product_page = ProductPage(browser, link)   
    product_page.open() 
    product_page.press_button_add_to_basket()
    product_page.solve_quiz_and_get_code()
    time.sleep(5)
    product_page.should_be_correct_name_in_message()
    product_page.should_be_basket_total_value_equal_product_price()


