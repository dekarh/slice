from bs4 import BeautifulSoup
from lib import s, fl

with open('1.html',encoding='cp1251') as f:
    inp = f.read()
soup = BeautifulSoup(inp,'lxml')
tables = {}
tables_titles = []
ts_ts = soup.findAll('center')
for table_title in ts_ts:
    tables_titles.append(s(table_title.text))
for i, table_into in enumerate(soup.findAll('table')):
    col_names = []
    for col_name in table_into.findChildren('th'):
        col_names.append(s(col_name.text))
    row_names = ['']
    rows = table_into.findChildren('tr')
    tables[tables_titles[i]] = {}
    # Названия строк
    for row in rows:
        cells = row.findChildren('td')
        if len(cells):
            row_names.append(s(cells[0].text))
    for j, row in enumerate(rows):
        cells = row.findChildren('td')
        if len(cells):
            tables[tables_titles[i]][row_names[j]] = {}
            for k, cell in enumerate(cells):
                if k:
                    tables[tables_titles[i]][row_names[j]][col_names[k]] = fl(s(cell.text))
pass # см. tables