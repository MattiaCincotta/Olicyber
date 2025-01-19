from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

# Specifica il percorso di geckodriver
service = Service('/usr/local/bin/geckodriver')
driver = webdriver.Firefox(service=service)

# Apri il sito
driver.get("http://easynotes.challs.olicyber.it/add")

# Usa By.CSS_SELECTOR per selezionare il pulsante con classe 'btn btn-primary'
button_selector = '.btn.btn-primary'
button = driver.find_element(By.CSS_SELECTOR, button_selector)

# Clicca il pulsante 1000 volte
for i in range(1000):
    print(i)
    button.click()


