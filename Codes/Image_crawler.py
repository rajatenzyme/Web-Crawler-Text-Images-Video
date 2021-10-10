import requests
from bs4 import BeautifulSoup
import os

data = []
images = []
image_url = "https://books.toscrape.com"
# add your url
for i in range(1,51):
    url = "https://books.toscrape.com/catalogue/page-" + str(i) + ".html"
    #print(url)
    r = requests.get (url)
    html_content = r.content
    soup = BeautifulSoup (html_content, 'html.parser')
    catalogue = soup.find_all("img")
    
    
    for image in catalogue:
      images.append(image['src'])

for i in range(len(images)):
  temp = images[i][2:]
  images[i] = image_url+temp
  #print(image)


os.mkdir('Rajat_photos')
i = 1

for index, img_link in enumerate(images):
    if i <= len(images):
        img_data = requests.get(img_link).content
        with open("my_pics/"+str(index+1)+'.jpg', 'wb+') as f:
            f.write(img_data)
        i += 1
    else:
        f.close()
        break