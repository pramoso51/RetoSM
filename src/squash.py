# from src.main import incrementor 
# from selenium import webdriver
# import time

# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome('./chromedriver')

# driver.implicitly_wait(30)
# driver.set_page_load_timeout(60)
# driver.get('https://qavbox.github.io/demo')
# assert "QAVBOX" in driver.title
# time.sleep(3)
# driver.find_element(By.LINK_TEXT, "SignUp Form").click()
# driver.save_screenshot("./screenshots/test.png")
# time.sleep(3)
# driver.quit

# @Given("nuevo incremento de {stride}")
# def given_incrementor (context, stride: str):
#   context.incrementor = incrementor(int(stride))
  
# @When("we increment {num}")
# def when_increment (context, num: str):
#   context.result = context.incrementor(int(num))

# @When("We should see {results}")  
# def then_increment (context, results):
#  assert(context.result == results)

