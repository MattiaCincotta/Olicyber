import requests
from bs4 import BeautifulSoup
import re

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException


service = Service('/usr/local/bin/geckodriver')  # Specifica il percorso di geckodriver
driver = webdriver.Firefox(service=service)  # Inizializza il driver per Firefox
    
def startSelenium():
    driver.get("http://infinite.challs.olicyber.it")  # Apri il sito

    # Ottieni il sorgente della pagina
    return driver.page_source


def parse_page_content(html): #questa funzione prende come parametro l'html e lo rende più facilemente manipolabile 
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        if soup:
            paragraphs = soup.find_all('p')
            return paragraphs
    return None

def question(paragraph):

    # Controlla le parole chiave nel testo estratto
    if paragraph[0:6] == "Quante":
        return 1  # Domanda grammatica
    elif paragraph[0:6] == "Quanto":
        return 2  # Domanda matematica
    else:
        return 3  # Domanda sui colori
    
def extract_words_between_quotes(sentence): #mi serve per le domande di grammatica per trovare la lettera e la parola tra doppi apici, mi ritorna una lista con i 2
    pattern = r'"([^"]*)"'
    matches = re.findall(pattern, sentence)
    if len(matches) >= 2:
        return matches[:2]
    else:
        return None

def grammatic(word, letter):    #mi serve per contare quante volte la lettera è presente nella parola
    count = 0
    for char in word:
        if char.lower() == letter.lower():
            count += 1
    return count

def math(sentence):     #mi serve per trovare i numeri da sommare e fare la somma
    pattern = r'\b\d+\b'
    numbers = re.findall(pattern, sentence)
    result = int(numbers[0]) + int(numbers[1])
    return result


def find_last_word(sentence):   #mi serve per i colori per trovare il colore da cliccare
    last_question_mark_index = sentence.rfind('?')
    if last_question_mark_index == -1:
        return None
    substring_before_question_mark = sentence[:last_question_mark_index]
    words = substring_before_question_mark.split()
    if words:
        last_word = words[-1]
        return last_word
    return None

def insertValue(value, identificatore):
    try:
        # Aggiungi un'attesa esplicita per assicurarti che l'elemento sia presente e interattivo
        #wait = WebDriverWait(driver, 10)
        #text_field = wait.until(EC.presence_of_element_located((By.ID,identificatore)))
        #text_field = wait.until(EC.element_to_be_clickable((By.ID, identificatore)))
        
        text_field = driver.find_element(By.NAME, identificatore)
        
        # Inserisci del testo nel campo di testo
        text_field.send_keys(value)

        
        submit = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']")
        submit.click()
        
        print(f"Valore '{value}' inserito correttamente nel campo con ID '{identificatore}'.")

    except TimeoutException:
        print(f"Timeout: L'elemento con ID '{identificatore}' non è stato trovato entro il tempo specificato.")
    except NoSuchElementException:
        print(f"Errore: L'elemento con ID '{identificatore}' non è stato trovato nella pagina.")
    except ElementNotInteractableException:
        print(f"Errore: L'elemento con ID '{identificatore}' non è interattivo.")
    except Exception as e:
        print(f"Errore durante l'inserimento del valore: {e}")

def clickButton(buttonID):
    
    # Trova il bottone tramite ID e clicca
    button = driver.find_element(By.ID, buttonID)  # Sostituisci con l'ID del tuo bottone
    button.click()

def main():
    
    
    page_source= startSelenium()
    count = 0
    while(True):
        page_source = driver.page_source
        print(page_source)
        count+=1
        print(count)
        # Usa BeautifulSoup per analizzare il contenuto HTML
        paragraphs = parse_page_content(page_source)
        
        # Estrai il testo dall'oggetto BeautifulSoup
        paragraphs = paragraphs[0].get_text()
        
        print(paragraphs)
        
        questionType = question(paragraphs)
        
        if questionType == 1:                   #grammatica
            words = extract_words_between_quotes(paragraphs)    
            result = grammatic(words[1], words[0])  
            #print(words[0], words[1]) 
            #print (result)
            insertValue(result, "letter")
        elif questionType == 2:                 #matematica
            result = math(paragraphs)
            #print(result)
            insertValue(result, "sum")
        else:                                   #colori
            color = find_last_word(paragraphs)
            #print(color)
            clickButton(color)
    
    
    
    
if __name__ == "__main__":
    main()