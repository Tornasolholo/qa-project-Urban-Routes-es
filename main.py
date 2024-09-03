import data
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from localizadores import UrbanRoutesPage
import time
from helpers import retrieve_phone_code

#no estoy usando time.sleep(10) en mi codigo


class TestUrbanRoutes:
    driver = None

    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.driver.implicitly_wait(5)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_fee()
        assert routes_page.check_comfort_active() == True #este codigo asegura que la tarifa esta activa

    def check_comfort_active(self):
        try:
            comfort_active_element = self.driver.find_element(By.CLASS_NAME, "tcard active")
            tcard_title = comfort_active_element.find_element(By.CLASS_NAME, "tcard-title").text
            return tcard_title == "Comfort"
        except:
            return False
        
    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)
        assert routes_page.get_add_number_text() == phone_number

    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        code_number = data.card_code
        routes_page.set_credit_card(card_number, code_number)
        assert routes_page.get_pp_text() == "Tarjeta"
        assert routes_page.get_pp_icon() == "card"

    def test_write_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        driver_message = data.message_for_driver
        routes_page.set_comment_driver(driver_message)
        assert routes_page.get_input_comment() == data.message_for_driver

    def test_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_switch()
        assert routes_page.get_blanket_switch_state() == True

    def test_add_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_icecream()
        assert routes_page.get_icecream_count() == "2"

    def test_find_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_smart_button()
        assert routes_page.get_order_section_status() == True

    def test_wait_driver_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.get_driver_information() == True  # Asegura que la información del conductor es visible
        WebDriverWait(self.driver, 5)
        time.sleep(5)


    def teardown_class(cls):
        cls.driver.quit()



