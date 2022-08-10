from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

name_book = []
name_final = []
price_book = []
instock_book = []
star_rating_book = []
category_book = []

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5),AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

#url_mistery = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
url_classics = 'https://books.toscrape.com/catalogue/category/books/classics_6/index.html'
url_science = 'https://books.toscrape.com/catalogue/category/books/science_22/index.html'
url_humor = 'https://books.toscrape.com/catalogue/category/books/humor_30/index.html'
url_business = 'https://books.toscrape.com/catalogue/category/books/business_35/index.html'

urls_categories = [url_classics,url_science,url_humor,url_business]
url_base = 'https://books.toscrape.com/catalogue'

for k in range(len(urls_categories)):
    page = requests.get(urls_categories[k],headers=headers)
    soup = BeautifulSoup(page.text,'html.parser')

    block = soup.find('div',class_='col-sm-8 col-md-9')

    url_books = []
    for a in block.find_all('a',href=True):
        if a.get('title'):
            a['href'] = a['href'].replace('../../..','')
            url_books.append(a['href'])    
   
    for i in url_books:

        url_final = url_base + i
        print(url_final)
        page = requests.get(url_final,headers=headers)
        soup = BeautifulSoup(page.text,'html.parser') 

        #print(soup)
        #block_info = soup.find_all('div',class_='col-sm-6 product_main')

        #Get Title-Name
        name = soup.find('h1').get_text()

        #Get Price 
        price = soup.find('p',class_='price_color').get_text().replace('Â','')

        #Get Instock Availability
        instock = soup.find('p',class_='instock availability').get_text().replace('\n','').replace(' ','').replace('k','k ')

        #Get Star Rating
        star_rating = soup.find('p',class_='star-rating').get('class')[1] + ' Star(s)'

        #Get Category
        category = soup.find('ul',class_='breadcrumb').find_all('li')[2].a.get_text()

        name_book.append(name)
        price_book.append(price)
        instock_book.append(instock)
        star_rating_book.append(star_rating)
        category_book.append(category)


data = pd.DataFrame({'Title': name_book,
                     'Price': price_book,
                     'Instock Availability': instock_book,
                     'Star-Rating': star_rating_book,
                     'Category': category_book})







    
