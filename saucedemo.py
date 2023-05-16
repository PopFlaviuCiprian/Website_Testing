from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SauceDemo(unittest.TestCase):
    USER_NAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, "password")
    PRESS_LOGIN = (By.XPATH, "//input[@type='submit']")
    CLICK_ON_FIRST_PRODUCT = (By.XPATH,'//div[@class="inventory_item_name"]')
    ADD_FIRST_PRODUCT_TO_CHART = (By.ID, 'add-to-cart-sauce-labs-backpack')
    REMOVE_PRODUCT_FROM_CHART = (By.ID, "remove-sauce-labs-backpack")
    PRESS_LEFT_MENU = (By.ID, 'react-burger-menu-btn')
    PRESS_LOGOUT_BTN = (By.ID, "logout_sidebar_link")
    DROPDOWN_FILTER = (By.XPATH, "//select[@class='product_sort_container']")
    CHECKOUT_BTN = (By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button']")
    VERIFY_CART = (By.ID, "shopping_cart_container")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        self.driver.close()

    def test_valid_login(self):
        self.driver.find_element(*self.USER_NAME_INPUT).send_keys("standard_user")
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('secret_sauce')
        self.driver.find_element(*self.PRESS_LOGIN).click()
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")

    def test_invalid_login(self):
        self.driver.find_element(*self.USER_NAME_INPUT).send_keys('invalid_user')
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('password')
        self.driver.find_element(*self.PRESS_LOGIN).click()
        error_message = self.driver.find_element(By.CSS_SELECTOR, '[data-test="error"').text
        self.assertEqual(error_message, "Epic sadface: Username and password do not match any user in this service")

    def test_login_only_password_input(self):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('password')
        self.driver.find_element(*self.PRESS_LOGIN).click()
        error_message = self.driver.find_element(By.CSS_SELECTOR, '[data-test="error"').text
        self.assertEqual(error_message, "Epic sadface: Username is required")

    def test_add_product_to_chart(self):
        self.driver.find_element(*self.USER_NAME_INPUT).send_keys("standard_user")
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('secret_sauce')
        self.driver.find_element(*self.PRESS_LOGIN).click()
        self.driver.find_element(*self.CLICK_ON_FIRST_PRODUCT).click()
        self.driver.find_element(*self.ADD_FIRST_PRODUCT_TO_CHART).click()
        self.assertTrue(self.driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]').is_displayed())
        chart_badge = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        assert chart_badge.text == "1"

    def test_remove_product_from_chart(self):
        self.driver.find_element(*self.USER_NAME_INPUT).send_keys("standard_user")
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('secret_sauce')
        self.driver.find_element(*self.PRESS_LOGIN).click()
        self.driver.find_element(*self.CLICK_ON_FIRST_PRODUCT).click()
        self.driver.find_element(*self.ADD_FIRST_PRODUCT_TO_CHART).click()
        self.driver.find_element(*self.REMOVE_PRODUCT_FROM_CHART).click()
        chart_badge = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        assert chart_badge.text == ""

    def test_filter_functionality(self):
        self.driver.find_element(*self.USER_NAME_INPUT).send_keys("standard_user")
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('secret_sauce')
        self.driver.find_element(*self.PRESS_LOGIN).click()
        self.driver.find_element(*self.DROPDOWN_FILTER).click()
        price_low_to_high = self.driver.find_element(By.XPATH, "//option[@value='lohi']").click()
        sort_product_az = self.driver.find_element(By.XPATH, "//option[@value='az']").click()
        sort_product_za = self.driver.find_element(By.XPATH, "//option[@value='za']").click()
        price_hi_to_low = self.driver.find_element(By.XPATH, "//option[@value='hilo']").click()
        products = self.driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")

    def test_add_to_chart_than_checkout_btn(self):
        self.driver.find_element(*self.USER_NAME_INPUT).send_keys("standard_user")
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('secret_sauce')
        self.driver.find_element(*self.PRESS_LOGIN).click()
        self.driver.find_element(*self.CLICK_ON_FIRST_PRODUCT).click()
        self.driver.find_element(*self.ADD_FIRST_PRODUCT_TO_CHART).click()
        self.driver.find_element(*self.VERIFY_CART).click()
        self.driver.find_element(*self.CHECKOUT_BTN).click()

    def test_add_product_to_chart_than_continue_shopping(self):
        self.driver.find_element(*self.USER_NAME_INPUT).send_keys("standard_user")
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('secret_sauce')
        self.driver.find_element(*self.PRESS_LOGIN).click()
        self.driver.find_element(*self.CLICK_ON_FIRST_PRODUCT).click()
        self.driver.find_element(*self.ADD_FIRST_PRODUCT_TO_CHART).click()
        self.driver.find_element(*self.VERIFY_CART).click()
        self.driver.find_element(*self.CONTINUE_SHOPPING_BTN).click()


    def test_logout_functionality(self):
        self.driver.find_element(*self.USER_NAME_INPUT).send_keys("standard_user")
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('secret_sauce')
        self.driver.find_element(*self.PRESS_LOGIN).click()
        self.driver.find_element(*self.PRESS_LEFT_MENU).click()
        self.driver.find_element(*self.PRESS_LOGOUT_BTN).click()
        self.assertTrue(self.driver.current_url, 'https://www.saucedemo.com/')




