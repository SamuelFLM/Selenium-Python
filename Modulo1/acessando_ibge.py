from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep



service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.ibge.gov.br/")


#Multiplos elementos
noticias = driver.find_elements(By.CLASS_NAME, 'home-noticia-data')

for noticia in noticias:
    print(noticia.text + "\n")


#Pegando tags

links = driver.find_elements(By.TAG_NAME, "a")

#Pegando atributo da tag
for link in links:
    print(link.get_attribute('href'))

input('')