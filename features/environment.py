from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def before_all(context):
    print('*************** Hook BeforeAll ***************')
    context.usuario = "pramos"

def after_all(context):
  print('*************** Hook AfterAll ***************')
  print(context.usuario)