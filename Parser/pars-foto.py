import requests
from bs4 import BeautifulSoup as BS


url = 'https://www.lamoda.ru/catalogsearch/result/?q=%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8&submit=y&gender_section=men'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

full_page = requests.get(url,headers=headers)
soup = BS(full_page.content, 'html.parser')

# con = soup.findAll('div', {"class":'x-product-card__card'})
# con = soup.findAll('div', {"class":'grid__catalog'}).next_element
all_a = soup.find_all('a')
arr = []
# print(con)
for i in all_a:
    if str(i.get('href')).count('/p/') == 1:
        arr.append(i.get('href'))
print(arr)

# for i in con:
#     arr.append(i['href'])
# print(arr)

    
