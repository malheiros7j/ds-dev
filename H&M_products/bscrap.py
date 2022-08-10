from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

### ID # Product_name ## Product_type ## Product_color #Composition # Price
url = 'https://www2.hm.com/en_us/men/products/jeans.html?sort=stock&image-size=small&image=model&offset=0&page-size=108'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5),AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.text,'html.parser')

products = soup.find('ul',class_="products-listing small")

products_list = products.find_all('article', class_='hm-product-item')

### Product_ID ###
product_id = [i.get('data-articlecode') for i in products_list]

### Product_Category ### 
product_category = [i.get('data-category') for i in products_list]

### Product_Name ###
products_list = products.find_all('a', class_='link')
#print(product_list[2].get_text())
product_name = [i.get_text() for i in products_list]

### Product_price ###
products_list = products.find_all('span',class_='price regular')
#print(products_list[0].get_text())
product_price = [i.get_text() for i in products_list]

data = pd.DataFrame([product_id,product_category,product_name,product_price]).T
data.columns = ['product_id','product_category','products_name','products_price']

#Scrapy datetime
data['scrapy_datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#empty DF
df_details = pd.DataFrame()

#Unique columns for all products
aux = []

cols = ['Art. No.', 'Composition', 'Fit', 'Product safety', 'Size']
df_pattern = pd.DataFrame(columns=cols)

for i in range(len(data)):
    #API Request
    url = 'https://www2.hm.com/en_us/productpage.' + data.loc[i,'product_id'] + '.html'
    
    page = requests.get(url,headers=headers)
    # Beautiful Soup Object
    soup = BeautifulSoup(page.text,'html.parser')
    
    
    ################ Color Name ################ 
    
    #Color Name and Product Type Actives
    products = soup.find_all('a',class_=['filter-option miniature active','filter-option miniature '])
    
    #Color Name and Product Type (Others)
    color = [i.get('data-color') for i in products]
    product_id = [i.get( 'data-articlecode' ) for i in products]

    df_color = pd.DataFrame( [product_id, color] ).T
    df_color.columns=['product_id','color_name']
    
    # generate style id + color id
    df_color['style_id'] = df_color['product_id'].apply(lambda x: x[:-3])
    df_color['color_id'] = df_color['product_id'].apply(lambda x: x[-3:])
    
    ################ Composition ################ 
    products_composition_list = soup.find_all('div',class_='pdp-description-list-item')
    product_composition = [list(filter(None,i.get_text().split('\n'))) for i in products_composition_list]
    
    if ((len(product_composition[2]) > 2)):
        product_composition[2][1:3] = [' '.join(product_composition[2][1:3])]         
    
    df_composition = pd.DataFrame(product_composition).T
    df_composition.columns = df_composition.iloc[0]

    #Delete first row
    df_composition = df_composition.iloc[1:].fillna(method='ffill').reset_index()
    
    # garantee the same number of columns
    df_composition = pd.concat( [df_pattern, df_composition], axis=0 )
    
    # generate style id + color id
    df_composition['style_id'] = df_composition['Art. No.'].apply( lambda x:x[:-3] )
    df_composition['color_id'] = df_composition['Art. No.'].apply( lambda x:x[-3:] )
    
    aux = aux + df_composition.columns.tolist()
       
    data_sku = pd.merge(df_color,df_composition[['style_id','Fit','Composition','Size','Product safety']],how='left',on='style_id')
    df_details = pd.concat([df_details,data_sku],axis=0)

data['style_id'] = data['product_id'].apply(lambda x: x[:-3])
data['color_id'] = data['product_id'].apply(lambda x: x[-3:])

data_raw = pd.merge(data,df_details[['style_id','color_name','Fit','Composition','Size','Product safety']],how='left',on='style_id')

data_raw.to_csv('data_raw.csv')
data_sku.to_csv('df_composition.csv')