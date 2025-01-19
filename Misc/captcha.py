from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import requests
from io import BytesIO

service = Service('/usr/local/bin/geckodriver')  # Specifica il percorso di geckodriver
driver = webdriver.Firefox(service=service)  # Inizializza il driver per Firefox

def startSelenium():
    driver.get("http://captcha.challs.olicyber.it/")  # Apri il sito

    # Ottieni il sorgente della pagina
    return driver.page_source

def insertValue(value):
    try:
        # Aggiungi un'attesa esplicita per assicurarti che l'elemento sia presente e interattivo
        #wait = WebDriverWait(driver, 10)
        #text_field = wait.until(EC.presence_of_element_located((By.ID,identificatore)))
        #text_field = wait.until(EC.element_to_be_clickable((By.ID, identificatore)))
        name = 'risposta'
        
        text_field = driver.find_element(By.NAME, name)
        
        # Inserisci del testo nel campo di testo
        text_field.send_keys(value)

        
        submit = driver.find_element(By.XPATH, '//*[@id="next"]')
        submit.click()
        
        print(f"Valore '{value}' inserito correttamente nel campo con ID '{name}'.")

    except TimeoutException:
        print(f"Timeout: L'elemento con ID '{name}' non è stato trovato entro il tempo specificato.")
    except NoSuchElementException:
        print(f"Errore: L'elemento con ID '{name}' non è stato trovato nella pagina.")
    except ElementNotInteractableException:
        print(f"Errore: L'elemento con ID '{name}' non è interattivo.")
    except Exception as e:
        print(f"Errore durante l'inserimento del valore: {e}")
        

def getText():
    """
    Ottiene il testo da un'immagine presente in una pagina web e lo inserisce in un campo di input.

    :param driver: Oggetto WebDriver di Selenium.
    :param img_xpath: XPath dell'immagine nella pagina web.
    :param input_name: Nome del campo di input dove inserire il testo estratto.
    :param tesseract_cmd_path: Percorso del binario Tesseract OCR.
    :return: Testo estratto dall'immagine.
    """
    tesseract_cmd_path = r'/usr/bin/tesseract'
    img_xpath = '/html/body/div/img'
    # Configura il percorso di Tesseract
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd_path

    # Trova l'immagine e ottieni l'URL
    img_element = driver.find_element(By.XPATH, img_xpath)
    img_url = img_element.get_attribute('src')

    # Scarica l'immagine
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))

    # Utilizza Tesseract per ottenere il testo dall'immagine
    text = pytesseract.image_to_string(img).strip()

    return text


def main():
    startSelenium()
    i = 0
    while(True):
        i +=1
        print(f'indice {i}')
        value = getText()
        insertValue(value)
        
if __name__ == "__main__":
    main()