import main
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Clase que maneja la interacción con la página de UrbanRoutes
class UrbanRoutesPage:
    # Definición de los localizadores que se usarán para encontrar elementos en la aplicación UrbanRoutes
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi = (By.CLASS_NAME, 'button.round')
    comfort_card = (By.XPATH, '//img[@alt="Comfort"]')
    set_comfort_category = (By.XPATH, '//button[@data-for="tariff-card-4"]')
    add_phone_number_button = (By.XPATH, '//div[@class="np-button"]')
    add_phone_number_text = (By.XPATH, '//div[@class="np-text"]')
    add_number = (By.XPATH, '//div[@class="np-input"]/div')
    write_number = (By.ID, 'phone')
    phone_number_button = (By.CLASS_NAME, "button.full")
    code_number_field = (By.ID, 'code')
    confirmation_code_button = (By.CSS_SELECTOR, '.section.active>form>.buttons>:nth-child(1)')
    add_payment_method = (By.CSS_SELECTOR, '.pp-button.filled')
    add_credit_card = (By.CSS_SELECTOR, '.pp-row.disabled')
    input_credit_card_number = (By.ID, 'number')
    input_credit_card_code = (By.XPATH, '//div[@class="card-code-input"]/input')
    submit_credit_card_button = (By.XPATH, '//div[@class="pp-buttons"]/button[@type="submit"]')
    close_payment_button = (By.CSS_SELECTOR, '.payment-picker.open>.modal>.section.active>button')
    payment_text = (By.CLASS_NAME, 'pp-value-text')
    payment_icon = (By.XPATH, '//div[@class="pp-value-container"]/img')
    add_comment_message = (By.ID, 'comment')
    comment_text = (By.CSS_SELECTOR, '.tariff-picker.shown>.form>:nth-child(3)>div')
    blanket_switch_button = (By.CLASS_NAME, 'r-sw')
    blanket_switch_state = (By.CSS_SELECTOR, '.r-sw > div > input')
    counter_icecream = (By.CSS_SELECTOR, '.r-group-items>:nth-child(1)>div>.r-counter>div>.counter-value')
    add_icecream_button = (By.CSS_SELECTOR, '.r-group-items>:nth-child(1)>div>.r-counter>div>.counter-plus')
    smart_button_call = (By.CLASS_NAME, 'smart-button-wrapper')
    order_section = (By.XPATH, '//div[@class="order-body"]')
    card_license_plate = (By.XPATH, '//div[@class="order-number"]')
    def __init__(self, driver):
        self.driver = driver

    # Para ingresar la dirección "From"
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    # Para ingresar dirección "To"
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    # Obtener la dirección "From" que se ha ingresado
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    # Obtener la dirección "To" que se ha ingresado
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Para definir la ruta ingresada con las direcciones "From" y "To"
    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    # Hacer click en el botón "pedir un taxi"
    def click_taxi_button(self):
        self.driver.find_element(*self.call_taxi).click()

    # Para seleccionar la categoría "Comfort"
    def click_comfort_button(self):
        self.driver.find_element(*self.comfort_card).click()

    # Verificar si la categoría "Comfort" está activa
    def check_comfort_active(self):
        return self.driver.find_element(*self.set_comfort_category).is_displayed()

    # Para seleccionar la tarifa "Comfort"
    def set_comfort_fee(self):
        self.click_taxi_button()
        self.click_comfort_button()
        self.check_comfort_active()

   # Para agregar un número de teléfono
    def click_add_number(self):
        self.driver.find_element(*self.add_phone_number_button).click()

    # Hacer clic en el campo para ingresar el número de teléfono
    def click_input_number_field(self):
        self.driver.find_element(*self.add_number).click()

    # Ingresar el número de teléfono
    def set_number_input(self, number):
        self.driver.find_element(*self.write_number).send_keys(number)

    # Para hacer clic en el botón para confirmar el número de teléfono
    def click_full_phone_number_button(self):
        self.driver.find_element(*self.phone_number_button).click()

    # Ingresar el código de confirmación
    def set_code_phone(self):
        self.driver.find_element(*self.code_number_field).send_keys(main.retrieve_phone_code(self.driver))
    def click_confirmation_code_button(self):
        self.driver.find_element(*self.confirmation_code_button).click()

    # Obtener el texto del número de teléfono agregado
    def get_add_number_text(self):
        return self.driver.find_element(*self.add_phone_number_text).text

    # Para configurar "agregar número de teléfono"
    def set_phone_number(self, number):
        self.click_add_number()
        self.click_input_number_field()
        self.set_number_input(number)
        self.click_full_phone_number_button()
        self.set_code_phone()
        self.click_confirmation_code_button()

    # Para agregar un "Método de pago"
    def click_add_payment(self):
        self.driver.find_element(*self.add_payment_method).click()
    def click_add_card(self):
        self.driver.find_element(*self.add_credit_card).click()
    def set_credit_card_number(self, card_number):
        self.driver.find_element(*self.input_credit_card_number).send_keys(card_number)
    def set_credit_code_number(self, code_number):
        self.driver.find_element(*self.input_credit_card_code).send_keys(code_number)
    def click_submit_credit_card(self):
        self.driver.find_element(*self.input_credit_card_number).click()
        self.driver.find_element(*self.submit_credit_card_button).click()
    def close_payment_method(self):
        self.driver.find_element(*self.close_payment_button).click()

    # Para configurar "Agregar método de pago"
    def set_credit_card(self, card_number, code_number):
        self.click_add_payment()
        self.click_add_card()
        self.set_credit_card_number(card_number)
        self.set_credit_code_number(code_number)
        self.click_submit_credit_card()
        self.close_payment_method()

    # Obtener el texto del método de pago actual
    def get_pp_text(self):
        return self.driver.find_element(*self.payment_text).text

    # Obtener el icono del método de pago actual
    def get_pp_icon(self):
        return self.driver.find_element(*self.payment_icon).get_attribute("alt")

# Para agregar un comentario al conductor
    def click_comment_field(self):
        self.driver.find_element(*self.comment_text).click()

    def write_comment(self, message):
        self.driver.find_element(*self.add_comment_message).send_keys(message)

    # Para configurar "agregar un comentario al conductor"
    def set_comment_driver(self, message):
        self.click_comment_field()
        self.write_comment(message)

    # Comprueba que se ingresó un comentario
    def get_input_comment(self):
        return self.driver.find_element(*self.add_comment_message).get_property('value')

# Para pedir manta y pañuelos
    def click_blanket_switch(self):
        self.driver.find_element(*self.blanket_switch_button).click()

    def get_blanket_switch_state(self):
        return self.driver.find_element(*self.blanket_switch_state).is_selected()

# Para pedir helado (2)
    def click_add_icecream(self):
        self.driver.find_element(*self.add_icecream_button).click()
        self.driver.find_element(*self.add_icecream_button).click()

    # Obtiene la cantidad de helados que se ha seleccionado
    def get_icecream_count(self):
        return self.driver.find_element(*self.counter_icecream).text

    # Para hacer click en el botón para ordenar el taxi
    def click_smart_button(self):
        self.driver.find_element(*self.smart_button_call).click()

    def get_order_section_status(self):
        return self.driver.find_element(*self.order_section).is_displayed()

# Para esperar a que aparezca la información del conductor
    def get_driver_information(self):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(self.card_license_plate))
        return self.driver.find_element(*self.card_license_plate).is_displayed()
