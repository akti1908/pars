from urllib import request, error
from bs4 import BeautifulSoup

with request.urlopen('https://akipress.org') as resp:
    data = resp.read()
    # print(data)
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('a', attrs={'class': 'newslink'})
    # print(items)
    for item in items:
        title = item.get_text()
        link = item.get('href')
        if 'turmush' in link:
            with request.urlopen('https:' + link) as page:
                data2 = page.read()
                soup2 = BeautifulSoup(data2, 'html.parser', encording="utf-8")
                des = soup2.find_all('p')
                for i in des:
                    text = i.get_text()
                    with open(title + '.txt', 'a') as file:
                        file.write(text)
                        print('done')
