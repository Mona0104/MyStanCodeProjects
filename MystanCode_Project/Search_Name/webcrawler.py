"""
File: webcrawler.py
Name: Mona Lai
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        # amount
        items = soup.find_all('tbody')[0].find_all('tr')
        lst = []
        for row in items[0:-1]:
            for td in row.find_all('td'):
                lst.append(td.text)

        boy_amount = 0
        girl_amount = 0

        for i in range(len(lst)):
            if i % 5 == 2:
                ans = ''
                for ch in lst[i]:
                    if ch.isdigit():
                        ans += ch
                boy_amount += int(ans)
            elif i % 5 == 4:
                ans = ''
                for ch in lst[i]:
                    if ch.isdigit():
                        ans += ch
                girl_amount += int(ans)

        print('Male Number:', boy_amount)
        print('Female Number:', girl_amount)


if __name__ == '__main__':
    main()
