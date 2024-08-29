# Urban Routes Test Automation

## Descripción del Proyecto

Este proyecto consiste en la automatización de pruebas para la aplicación web de UrbanRoutes. UrbanRoutes es una plataforma de transporte que permite a los usuarios solicitar taxis, seleccionar tarifas, agregar métodos de pago, y más. El propósito de este proyecto es verificar la funcionalidad principal de la aplicación utilizando pruebas automatizadas con Selenium WebDriver.

## Tecnologías y Técnicas Utilizadas

- **Lenguaje de Programación**: Python
- **Herramienta de Automatización**: Selenium WebDriver
- **Framework de Pruebas**: Pytest
- **Navegador Utilizado**: Google Chrome
- **Patrón de Diseño**: Page Object Model (POM)

## Instrucciones para Ejecutar las Pruebas

### Prerrequisitos

1. **Python 3.x** debe estar instalado en tu sistema.
2. Instala las dependencias del proyecto utilizando el siguiente comando:
   ```bash
   pip install -r requirements.txt


3. Google Chrome debe estar instalado, junto con el ChromeDriver correspondiente a tu versión de Chrome.

Ejecución de Pruebas
1. Clona el repositorio en tu máquina local.
git clone <url-del-repositorio>
cd urban-routes-test

2. Para ejecutar todas las pruebas, utiliza el siguiente comando:
pytest
Este comando ejecutará todas las pruebas definidas en el archivo urban_routes_es.py.


Estructura del Proyecto
data.py: Contiene los datos de prueba que se utilizan en los scripts, como direcciones y números de teléfono.
localizadores.py: Define los localizadores y métodos de interacción para los elementos de la página utilizando el patrón Page Object Model (POM).
main.py: Contiene funciones auxiliares, como la obtención del código de confirmación.
urban_routes_es.py: Contiene las pruebas automatizadas, organizadas en métodos dentro de la clase TestUrbanRoutes.
