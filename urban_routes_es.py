import data
import time
from localizadores import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# Clase de prueba para verificar las funcionalidades de la aplicación de UrbanRoutes
class TestUrbanRoutes:
    driver = None


    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    # Verifica que se pueda establecer correctamente una ruta en UrbanRoutes
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        self.driver.implicitly_wait(5)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from  # Asegura que la dirección de origen es correcta
        assert routes_page.get_to() == address_to  # Asegura que la dirección de destino es correcta

    # Verifica que se pueda seleccionar la tarifa "Comfort" correctamente
    def test_set_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_fee()
        assert routes_page.check_comfort_active() == True  # Asegura que la tarifa "Comfort" está activada

    # Verifica que se pueda agregar un número de teléfono correctamente
    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)
        assert routes_page.get_add_number_text() == phone_number  # Asegura que el número de teléfono es correcto

    # Verifica que se pueda agregar correctamente una tarjeta de crédito
    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        code_number = data.card_code
        routes_page.set_credit_card(card_number, code_number)
        assert routes_page.get_pp_text() == "Tarjeta"  # Asegura que la tarjeta ha sido añadida
        assert routes_page.get_pp_icon() == "card"  # Asegura que el ícono de la tarjeta es correcto

    # Verifica que se pueda agregar un mensaje para el conductor
    def test_write_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        driver_message = data.message_for_driver
        routes_page.set_comment_driver(driver_message)
        assert routes_page.get_input_comment() == data.message_for_driver  # Asegura que el mensaje se ha añadido correctamente
        WebDriverWait(self.driver, 5)

    # Verifica que se pueda solicitar una manta correctamente
    def test_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_switch()
        assert routes_page.get_blanket_switch_state() == True  # Asegura que la manta ha sido seleccionada

    # Verifica que se pueda añadir helado al pedido
    def test_add_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_icecream()
        assert routes_page.get_icecream_count() == "2"  # Asegura que se han añadido dos helados

    # Verifica que se pueda iniciar la búsqueda de un conductor
    def test_find_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_smart_button()
        assert routes_page.get_order_section_status() == True  # Asegura que la búsqueda de un conductor se ha iniciado
        WebDriverWait(self.driver, 5)

    # Verifica que la información del conductor se muestra correctamente después de la búsqueda
    def test_wait_driver_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.get_driver_information() == True  # Asegura que la información del conductor es visible
        WebDriverWait(self.driver, 5)
        time.sleep(10)

    def teardown_class(cls):
        cls.driver.quit()
