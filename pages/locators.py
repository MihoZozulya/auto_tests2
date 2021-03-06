from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")

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
    VIEW_BASKET = (By.CSS_SELECTOR, ".hidden-xs a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p > a")
    PRODUCT_IS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3 a")
