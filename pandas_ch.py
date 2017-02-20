import requests
from bs4 import BeautifulSoup
import pandas as pd

print "Welcome to web scrape program" + "\n"
print "Currently scraping data from http://www.sql-join.com/ website using BeautifulSoup" + "\n"
print "Customers and orders tables' data is being gathered" + "\n"
r=requests.get('http://www.sql-join.com/')
soup = BeautifulSoup(r.content,'lxml')

customer_table = soup.find_all('table')[0]
customers_header = [th.getText() for th in customer_table.findAll('tr')[0].findAll('th')]
cus_data_html = customer_table.findAll('tr')[1:]
customers_data = [[td.getText() for td in cus_data_html[i].findAll('td')] for i in range(len(cus_data_html))]


orders_table = soup.find_all('table')[1]
orders_header = [th.getText() for th in orders_table.findAll('tr')[0].findAll('th')]
ord_data_html = orders_table.findAll('tr')[1:]
orders_data = [[td.getText() for td in ord_data_html[i].findAll('td')] for i in range(len(ord_data_html))]

print "Data gathering done ! " + "\n"
cus_dataframe=pd.DataFrame(customers_data, columns=customers_header)
ord_dataframe=pd.DataFrame(orders_data, columns=orders_header)

print "Ingested data into dataframes" + "\n"

merged_datasets = pd.merge(cus_dataframe,ord_dataframe, how='inner', on=['customer_id', 'customer_id'])

print "Merged data on customer_id column present in both tables. Here's the output" + "\n"
print(merged_datasets)

