from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
 
class ProductPageLocators():
    BTN_ADDBSKT = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME =  (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")
    BASKET_TOTAL_VALUE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1)")
    BTN_VIEWBSKT = (By.CSS_SELECTOR, ".basket-mini a")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")

    
class BasketPageLocators():
    BASKET_FORMS_WITH_PRODUCTS = (By.CSS_SELECTOR, "#basket_formset")
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    