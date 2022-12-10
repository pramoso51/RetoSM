# Reto: SquashMakeres QA

## _¿En que consiste el reto?_

El reto se basará en hacer la toma de requerimientos propuestos y automatizar esas pruebas E2E en la web dada. Para ello se necesitará crear un repositorio online en el servicio que se prefiera (Gitlab, Github...) donde se subirá el código resultante
de la prueba.
Como se realizará en Python y Selenium, antes de empezar deberá asegurarse de que lo tiene instalado y accesible para programar.
La prueba consiste en documentar y automatizar las features en la web:

- https://www.saucedemo.com/

## Features

- Login y Logout
- Hacer compra de varios artículos

### Ejecución

_Nota:_ El proyecto puede ejecutarse con Headless True o False

```sh
behave
```

```sh
behave -f html -o behave-report.html
```

_Reportes_: Con ALLURE

```sh
brew install allure
behave -f allure_behave.formatter:AllureFormatter –o my_allure
allure serve my_allure
```

Levantar Allure:

```sh
allure serve my_allure
```

## Librerías y Configuración Instaladas

`python3 -m venv .venv`
`source .venv/bin/activate `
`pip3 install -U selenium`

Se creo el archivo _behave.ini_ para poder exportar el reporte a html.
Reporte: behave-report.html

## IDE

- Visual Studio Code

## Soporte de Ejecución

en carpeta: soporte*resultados
screenshots - imagen de login en carpeta: \_screenshots*

## IDEAL

Lo ideal es programarlo con POM (Page Object Model) pero mi expereiencia es full javascript pero esta interesante
el sejercicio para python. Es de meterme mas a la sintaxis del lenguaje y se logra algo bien trabajado. ;)
