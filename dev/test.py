#Importation des addons
import os
import requests
import sys
from bs4 import BeautifulSoup

#instantiation des variables requests et beautifulsoup
url = "https://www.facebook.com"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#lancement de la fonction equalizer
equalizer=("")

recherche=soup.find_all('div')

equalizer.append(recherche),

resultat={"site"=url,"visit"=recherche.lenght }
