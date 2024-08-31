# Urban Routes Test Automation

## Descripción del Proyecto
Este proyecto consiste en la automatización de pruebas para la aplicación web de UrbanRoutes. UrbanRoutes es una plataforma de transporte que permite a los usuarios solicitar taxis, seleccionar tarifas, agregar métodos de pago, y más. El propósito de este proyecto es verificar la funcionalidad principal de la aplicación utilizando pruebas automatizadas con Selenium WebDriver.

## Tecnologías y Técnicas Utilizadas
- Lenguaje de Programación: Python
- Herramienta de Automatización: Selenium WebDriver
- Framework de Pruebas: Pytest
- Navegador Utilizado: Google Chrome
- Patrón de Diseño: Page Object Model (POM)

## Estructura del Proyecto
- `data.py`: Contiene los datos de prueba que se utilizan en los scripts, como direcciones y números de teléfono.
- `localizadores.py`: Define los localizadores y métodos de interacción para los elementos de la página utilizando el patrón Page Object Model (POM). Aquí se encapsulan los selectores de los elementos de la UI y las acciones que se pueden realizar en ellos.
- `helpers.py`: Contiene funciones auxiliares, como la obtención del código de confirmación. Estas funciones se usan para realizar operaciones repetitivas o que se reutilizan en múltiples pruebas, facilitando así el mantenimiento del código.
- `main.py`: Contiene las pruebas automatizadas, organizadas en métodos dentro de la clase `TestUrbanRoutes`. Este archivo es el corazón del proyecto, donde se integran los localizadores y datos para validar las funcionalidades de UrbanRoutes.
- `urban_routes_es.py`: Este archivo ya no es necesario y se ha consolidado en `main.py` para evitar duplicación y mejorar la eficiencia del código.

## Instrucciones para Ejecutar las Pruebas

### Prerrequisitos
1. Python 3.x debe estar instalado en tu sistema.
2. Instala las dependencias del proyecto utilizando el siguiente comando:
   ```sh
   pip install -r requirements.txt
   
### Ejecución de las Pruebas
Para ejecutar las pruebas, utiliza el siguiente comando en la terminal:
pytest
Este comando ejecutará todas las pruebas definidas en el archivo main.py.



