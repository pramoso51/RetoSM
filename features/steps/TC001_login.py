from multiprocessing import context
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from features.environment import *

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

@given('Se verifica la disponiblidad del sitio web')
def step_impl(context):
  driver.get('https://www.saucedemo.com/')
  assert "Swag Labs" in driver.title
  driver.implicitly_wait(1)
  pass

@when('Se ingresan credenciales con usuario: {strUser} y contraseña: {strConstrasena}')
def step_impl(context, strUser: str, strConstrasena: str):
  driver.find_element(By.ID, "user-name").send_keys(strUser)  # Elemento Usuario
  driver.find_element(By.ID, "password").send_keys(strConstrasena)    # Elemento Contraeñas
  driver.find_element(By.ID, "login-button").click()                  # Boton de Ingreso
  pass
  
@then('Verificar si son credenciales correctas')
def step_impl(context):
  driver.find_element(By.ID, "react-burger-menu-btn").click()
  driver.find_element(By.ID, "logout_sidebar_link").click()
  if (driver.find_element(By.ID, "login-button").is_displayed):
    driver.quit
    pass
  else:
    AssertionError("Error en Login")
    driver.quit
  

