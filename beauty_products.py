import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://www.tomford.com/beauty/face/")
soup = BeautifulSoup(page.content,'lxml')
title = soup.title.text
print(title)

csv_file = open('product_file.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Product ID', 'Product Price', 'Product Image link', 'Product Description'])

products = soup.find_all('li',class_ = 'grid-tile')
for product in products:
    #product_name = product.find('li', class_ = 'grid-tile')
    #headline = product_name.a.text
    #print(headline)
    product_name = product.a.text
    print(product_name)

    product_price = product.find('span', class_ = 'product-sales-price')
    headline2 = product_price.text
    print(headline2)
    #product_id = product.find('li', class_ = 'grid-tile')['id']
    #print(product_id)
    product_id = product.div['data-itemsku']
    print(product_id)
    #product_link = product.find('a', class_ = 'overlay-link')['href']
    #print(product_link)
    product_link = product.div.a['href']
    print(product_link)

    product_page = requests.get(product_link)
    soup1 = BeautifulSoup(product_page.content,'html.parser')
    img_link = soup1.find('img', class_ = 'primary-image')['src']
    print(img_link)

    product_description = soup1.find('div', class_ = 'panel-body')
    head_desc = (product_description.text)
    print(head_desc)

    print()

    csv_writer.writerow([product_name, product_id, headline2, img_link, head_desc])
csv_file.close()





