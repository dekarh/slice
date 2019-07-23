from bs4 import BeautifulSoup
import os, openpyxl
from lib import s, fl, unique

dirs = ['.']
positions = os.listdir('.')
for position in positions:
    if not os.path.isfile(position) and position[0] != '.':
        dirs.append(position)
all_tables_titles = []
all_col_names = []
all_row_names = []
for dir in dirs:
    with open(dir + '/1.html',encoding='cp1251') as f:
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
        all_col_names = all_col_names + col_names
        all_row_names = all_row_names + row_names
    all_tables_titles = all_tables_titles + tables_titles

all_tables_titles = unique(all_tables_titles)
all_col_names = unique(all_col_names)
all_row_names = unique(all_row_names)

wb_rez = openpyxl.Workbook(write_only=True)
ws_rez = wb_rez.create_sheet('all_tables_titles')
for all_table_title in all_tables_titles:
    ws_rez.append([all_table_title])
ws_rez = wb_rez.create_sheet('all_col_names')
for all_col_name in all_col_names:
    ws_rez.append([all_col_name])
ws_rez = wb_rez.create_sheet('all_row_names')
for all_row_name in all_row_names:
    ws_rez.append([all_row_name])
wb_rez.save('termins.xlsx')


pass # см. tables