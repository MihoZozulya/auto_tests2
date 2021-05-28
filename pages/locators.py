from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK_IN_ALERT = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2) > strong")
    MESSAGE_TO_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2)")
    SUMM_IN_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong")
    MESSAGE_TO_SUMM_IN_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1)")
    NAME_BOOK = (By.CSS_SELECTOR, "h1")
    PRICE_BOOK = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
