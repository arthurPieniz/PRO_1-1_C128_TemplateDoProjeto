from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

# URL para coleta de dados
url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

# Obtenha a Página
page = requests.get(url)

# Analise a página
soup= bs(page.text,'html.parser')

# Obtenha a <table> com classe = 'wikitable sortable'
star_table = soup.find_all('table', {'class':"wikitable sortable"})

total_table = len(star_table)


temp_list = []


table_rows = star_table[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(temp_list)

# Converta para CSV
headers = ['Star_name', 'Distance', 'Mass', 'Radius']
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)), columns=['Star_name', 'Distance', 'Mass', 'Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")