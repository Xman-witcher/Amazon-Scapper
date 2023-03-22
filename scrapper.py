import requests
from bs4 import BeautifulSoup
import csv


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}


base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}'


num_pages = 20

data = []


for page in range(1, num_pages + 1):
  
    url = base_url.format(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    for product in products:
        product_url = 'https://www.amazon.in' + product.find('a', {'class': 'a-link-normal'})['href']
        name = product.find("h2")
        if name:
            name = name.text.strip()
        else:
            name=''
        price = product.find("span", {"class": "a-price-whole"})
        if price:
            price = price.text.strip()
        else:
            price = ''
        rating = product.find("span", {"class": "a-icon-alt"})
        if rating:
            rating = rating.text.strip().split()[0]
        else:
            rating=''
        num_reviews = product.find('span', {'class': 'a-size-base', 'dir': 'auto'})
        if num_reviews:
            num_reviews = num_reviews.text.strip().replace(',', '')
        else:
            num_reviews =''
        
        response = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        asin = soup.find("th", {"class": "a-color-secondary a-size-base prodDetSectionEntry"})
        if asin:
            asin = asin.text.strip()
        else:
            asin = ''
        description = soup.find("div", {"id": "productDescription"})
        if description:
            description= description.text.strip()
        else:
            description = ''
        
        manufacturer = soup.find("a", {"id": "bylineInfo"})
        if manufacturer:
            manufacturer = manufacturer.text.strip()
        else:
            manufacturer = ''
        
        data.append({
            'Product URL': product_url,
            'Product Name': name,
            'Product Price': price,
            'Rating': rating,
            'Number of Reviews': num_reviews,
            'ASIN': asin,
            'Description': description,
            'Manufacturer': manufacturer
        })

with open('amazon_bags.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Product URL', 'Product Name', 'Product Price', 'Rating', 'Number of Reviews', 'ASIN', 'Description', 'Manufacturer']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        writer.writerow(item)
