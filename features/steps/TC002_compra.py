import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait # you can place it on the top
from features.environment import *

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

@given('Se va realizar una compra')
def step_impl(context):
  driver.get("https://www.saucedemo.com/")
  driver.set_window_size(1920, 1055)
  driver.find_element(By.ID, "login_credentials").click()
  driver.find_element(By.ID, "login_credentials").click()
  element = driver.find_element(By.ID, "login_credentials")
  actions = ActionChains(driver)
  actions.double_click(element).perform()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
  driver.find_element(By.CSS_SELECTOR, ".login_password").click()
  driver.find_element(By.CSS_SELECTOR, ".login_password").click()
  driver.find_element(By.CSS_SELECTOR, ".login_password").click()
  element = driver.find_element(By.CSS_SELECTOR, ".login_password")
  actions = ActionChains(driver)
  actions.double_click(element).perform()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
  old_url = driver.current_url
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
  WebDriverWait(driver, 10).until(lambda driver: old_url != driver.current_url 
      and driver.execute_script("return document.readyState == 'complete'"))
  pass

@when('Se carga el carrito de compras')
def step_impl(context):
  # driver.find_element(By.ID, "user-name").send_keys("standard_user")  # Elemento Usuario
  # driver.find_element(By.ID, "password").send_keys("strConstrasena")  # Elemento Contraeñas
  # driver.find_element(By.ID, "login-button").click()                  # Boton de Ingreso
  pass

@then('Se procesa compra')
def step_impl(context):
  # here you are redirected to another page (e.g. clicked a link or submited a form)
  
  #element = driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]")
  #actions = ActionChains(driver)
  #actions.move_to_element(element).perform()
  # driver.get("https://www.saucedemo.com/inventory.html")
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
  # element = driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]")
  # actions = ActionChains(driver)
  # actions.move_to_element(element).perform()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
  driver.find_element(By.LINK_TEXT, "3").click()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-fleece-jacket\"]").click()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("Pablo")
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("Ramos")
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("01017")
  driver.find_element(By.CSS_SELECTOR, ".checkout_buttons").click()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
  driver.find_element(By.CSS_SELECTOR, ".complete-header").click()
  driver.find_element(By.CSS_SELECTOR, ".complete-header").click()
  driver.find_element(By.CSS_SELECTOR, ".complete-header").click()
  elements = driver.find_elements(By.CSS_SELECTOR, ".complete-header")
  assert len(elements) > 0
  driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()
  
  # element = driver.find_element(By.CSS_SELECTOR, ".back-to-products")
  # actions = ActionChains(driver)
  # actions.click(element).perform()
  
  # element = driver.find_element(By.ID, "react-burger-menu-btn")
  # actions = ActionChains(driver)
  # actions.move_to_element(element).perform()

  # driver.find_element(By.ID, "react-burger-menu-btn").click()
  # driver.find_element(By.ID, "logout_sidebar_link").click()
  
  # driver.close()
  pass

driver.quit