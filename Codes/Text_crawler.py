# import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv


# adding given urls
url = "https://books.toscrape.com/"

# get the html content
r = requests.get (url)

html_content = r.content

# making the soup - parsing the HTML
soup = BeautifulSoup (html_content, 'html.parser')

# tree traversal of html
# saving the html content as a list
# title, rating, price, stock
data = []

catalogue = soup.find_all ("ol", {"class":"row"})

for item in catalogue [0].find_all ("li", {"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"}):
  mdata = {}
  mdata ['title'] = item.h3.a.get ("title")
  mdata ['rating'] = item.p.get ("class") [1]
  mdata ['price'] = item.find ("p", {"class":"price_color"}).text
  mdata ['stock'] = item.find ("p", {"class":"instock availability"}).text [15:17]
  data.append (mdata)

file_csv = 'book-store.csv'

with open (file_csv, 'w', newline='') as f:
    w = csv.DictWriter (f, ['title', 'rating', 'price', 'stock'])
    w.writeheader ()
    for mdata in data:
        w.writerow (mdata)

























