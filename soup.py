import requests
import numpy as np
from bs4 import BeautifulSoup

#send HTTP/1.1 to the website
page = requests.get('https://ycharts.com/companies/LNR.TO/dividend')


#Passing the page to the soup
soup = BeautifulSoup(page.content, 'html.parser')


results = soup.find(id="dataTableBox")

needed = results.find_all('table', class_='histDividendDataTable')

for x in needed:
    getit = x.text

getit = getit.splitlines()

tt = np.array(getit)

tt = tt[tt!='']

col = tt[1:6]
data = tt[6:]

date = data[2:150:6]
div = data[5:150:6]

final = np.column_stack((date,div))

np.savetxt("LNR.TO.csv", final, delimiter=",",fmt='%s')
