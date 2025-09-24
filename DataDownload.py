import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By

def downloadImages(url,folderName,num):
    response = requests.get(url)
    if response.status_code == 200:
        if not os.path.isdir(os.path.join(folderName,str(num)+'b.jpg')):
            with open(os.path.join(folderName,str(num)+'b.jpg'),'wb') as file:
                file.write(response.content)

chromeDriver = "C:\\Users\\marqu\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome()
squirrel_names = [  
    # North America
    "Eastern Gray Squirrel",
    "Fox Squirrel",
    "Red Squirrel",
    "Douglas Squirrel",
    "Abert's Squirrel",
    "Arizona Gray Squirrel",
    "Western Gray Squirrel",
    "Southern Flying Squirrel",
    "Northern Flying Squirrel",
    "Humboldt's Flying Squirrel",
    "Thirteen-lined Ground Squirrel",
    "California Ground Squirrel",
    "Rock Squirrel",
    "Franklin's Ground Squirrel",
    "Black-tailed Prairie Dog",
    "Columbian Ground Squirrel",
    "Uinta Ground Squirrel",
    "Golden-mantled Ground Squirrel",
    "Belding's Ground Squirrel",
    "Richardson's Ground Squirrel",
    "Yellow-bellied Marmot",
    "Olympic Marmot",
    "Hoary Marmot",
    "Woodchuck",
    "Alpine Marmot",
    "Arctic Ground Squirrel",

    # South America
    "Bolivian Squirrel",
    "Andean Squirrel",
    "Amazon Dwarf Squirrel",
    "Red-tailed Squirrel",
    "Guayaquil Squirrel",
    "Calabrian Squirrel",
    "Junin Squirrel",
    
    # Europe
    "Red Squirrel",
    "Siberian Flying Squirrel",

    # Asia
    "Indian Giant Squirrel",
    "Finlayson's Squirrel",
    "Pallas's Squirrel",
    "Hoary-bellied Squirrel",
    "Indian Giant Flying Squirrel",
    "Red Giant Flying Squirrel",
    "Japanese Giant Flying Squirrel",
    "Malayan Black Giant Squirrel",
    "Sunda Giant Squirrel",
    "Bornean Giant Squirrel",

    # Africa
    "African Giant Squirrel",
    "Slender-tailed Squirrel",
    "Red-legged Sun Squirrel",
    "Smith's Bush Squirrel",
    "Gambian Sun Squirrel",
    "African Striped Ground Squirrel",
    "Heliosciurus Squirrel",
    "Protoxerus Stangeri",
    "Xerus Inauris",

    # Misc/Other notable squirrels
    "Northern Palm Squirrel",
    "Prevost's Squirrel",
    "Red-and-white Squirrel",
    "Black Giant Squirrel",
    "Finlayson's Flying Squirrel",
    "Whiskered Flying Squirrel",
    "Red-cheeked Flying Squirrel",
    "Philippine Giant Flying Squirrel",
    "Red-and-white Giant Squirrel",
    "Small Indian Squirrel",
    "Pygmy Squirrel",
    "Northern Flying Squirrel",
    "Southern Flying Squirrel",
    "American Red Squirrel",
    "Siberian Chipmunk",
    "Chinese Striped Squirrel",
    "Neotropical Pygmy Squirrel"
]
for i in range(0,len(squirrel_names)):

    folderName=f'Data\\{squirrel_names[i]}'
    if not os.path.isdir(folderName):
        os.makedirs(folderName)

    searchURL = f'https://www.google.com/search?q={squirrel_names[i]}&tbm=isch&hl=en'
    driver.get(searchURL)
    time.sleep(5)
    pageHtml = driver.page_source
    pageSoup = BeautifulSoup(pageHtml,'html.parser')

    containers = pageSoup.find_all('div',{'class':"eA0Zlc WghbWd FnEtTd mkpRId m3LIae RLdvSe qyKxnc ivg-i PZPZlf GMCzAd"})

    amountContainers = len(containers)
    print(f"found {amountContainers} image containers")

    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    containers = driver.find_elements(By.CSS_SELECTOR, "div.czzyk.XOEbc")  
    for j, container in enumerate(containers,start=1):
        try:
            xpath= f"""//*[@id="rso"]/div/div/div[1]/div/div/div[{j}]"""
            imagePath="img.sFlh5c.FyHeAf"

        
            #driver.find_element(By.XPATH,xpath).click()
            container.click()
            time.sleep(5)
            imageD= driver.find_element(By.CSS_SELECTOR,imagePath)
            imageURL = imageD.get_attribute('src')
            print(imageURL)
            if j >= len(containers)-1:
                 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                 containers = driver.find_elements(By.CSS_SELECTOR, "div.czzyk.XOEbc")
                 print(f'Total found {len(containers)}')
                 time.sleep(5)
            #if j%25 ==0:
                #continue
            downloadImages(imageURL,folderName,j)
            print(f'me here {j}')
        except:
            print(f'unable to download image {j}')
        if j > 1000:
            i = i+1
