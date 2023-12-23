# import requests
# from bs4 import BeautifulSoup
# import os
# import shutil
# from time import sleep

# search_term = '"mine field" -urban -city'

# url = rf'https://www.google.no/search?q={search_term}&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&safe=active&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'

# page = requests.get(url).text

# soup = BeautifulSoup(page, 'html.parser')

# thumbnails = []

# for raw_img in soup.find_all('img'):
#     # Essayer de trouver des images en haute résolution
#     link = raw_img.get('data-src') or raw_img.get('data-lz-src') or raw_img.get('src')
    
#     if link and link.startswith("https://"):
#         thumbnails.append(link)

# # Fonction pour télécharger une image
# def download_image(image_url, folder_name, index):
#     response = requests.get(image_url, stream=True)
#     if response.status_code == 200:
#         file_path = os.path.join(folder_name, f"image_{index}.jpg")
#         with open(file_path, 'wb') as file:
#             response.raw.decode_content = True
#             shutil.copyfileobj(response.raw, file)
#             print(f"Image téléchargée : {file_path}")

# # Création du dossier pour les images
# folder_name = 'downloaded_images'
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)

# # Téléchargement des images
# for index, img_url in enumerate(thumbnails[:200]):
#     download_image(img_url, folder_name, index)
#     sleep(5)  # Pause pour éviter de surcharger le serveur


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import shutil
import os
import time

# Définir les termes de recherche et le chemin du WebDriver
search_term = '"mine field" -urban -city'
webdriver_path = '/path/to/chromedriver'  # Remplacez par votre chemin vers ChromeDriver

# Options pour Selenium WebDriver
options = Options()
options.headless = True  # Exécute le navigateur en mode headless (sans interface graphique)
service = Service(webdriver_path)

# Lancer Selenium WebDriver
driver = webdriver.Chrome(service=service, options=options)
driver.get(f'https://www.google.com/search?q={search_term}&tbm=isch')

# Attendre que la page charge
time.sleep(5)

# Utiliser BeautifulSoup pour analyser la page
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Trouver les URL des images
thumbnails = []
for img in soup.find_all('img'):
    src = img.get('src') or img.get('data-src')
    if src and src.startswith('http'):
        thumbnails.append(src)

# Fonction pour télécharger une image
def download_image(image_url, folder_name, index):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        file_path = os.path.join(folder_name, f'image_{index}.jpg')
        with open(file_path, 'wb') as file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, file)
            print(f'Image téléchargée : {file_path}')

# Création du dossier pour les images
folder_name = 'downloaded_images'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Téléchargement des images
for index, img_url in enumerate(thumbnails[:10]):  # Télécharge les 10 premières images
    download_image(img_url, folder_name, index)
    time.sleep(1)  # Pause pour éviter de surcharger le serveur
