'''
Date:201211
Funciones que correspondan al Scraping: reputación online, cool hunting y monitorización. 
'''
import pandas as pd #Instalado
import numpy as np #Instalado
import requests #Instalado
import bs4 as beautifulsoup #instalado

#Función que ayude a realizar scraping con el objetivo de conocer la reputación online del negocio/marca.


def requestWebPage(soup):
    res= requests.get(url)
    html = res.text
    return soup
url = 
soup = BeautifulSoup(html, "html.parser") #Para poder pasar del código html a Python y poder trabajar.
print(soup)

"--------------------"

tag = 
atributo = 
def sacarhipervinculos(hipervinculos):
lista_tag = soup.findAll(tag) #si quiero encontrar los hipervínculos
lista_tag
    for x in lista_tag:
        print(x)
    return hipervinculos
hipervinculos = (x.get(atributo))
print (hipervinculos)

"----------------------"

def visiting_web():
    from urllib.request import urlopen
    url = ""
    page = urlopen(url)
    soup = beautifulsoup(response.text, "html.parser")
    line_count = 1
    for one_a_tag in soup.findAll("a") #"a" tags are for links
        if line_count >= X #code empieza en x line
            link = one_a_tag["href"]
            download_url = "url" + link
            urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
        line_count +=1
pass


#Me tengo que instalar beautifulsoup (pte)

