from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_correct_book(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_TO_ADD_PRODUCT_TO_BASKET), "don't product in basket"
        name_book_in_alert = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_ALERT)
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        assert name_book_in_alert.text == name_book.text, "don't correct product in basket"

    def should_be_correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_TO_SUMM_IN_BASKET), "don't message to price for product in basket"
        summ_in_basket = self.browser.find_element(*ProductPageLocators.SUMM_IN_BASKET)
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        assert summ_in_basket.text == price_book.text, "don't correct price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Message is presented, but should be disappeared"
