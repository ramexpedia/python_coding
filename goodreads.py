from urllib2 import urlopen
import urllib2
import urllib
import os.path
import re
import json
from bs4 import BeautifulSoup
import requests
import getpass
import mechanize
import re
import sys

reload(sys)
sys.setdefaultencoding("utf8")

print("\n")
print("Hello! Welcome to goodreads quote app, that retrieves top and least popular 10 quotes of Mark_Twain. Please proceed with credentials.. ")

a=[]

user = raw_input("Username:")
passwd = getpass.getpass("Password for " + user + ":")

br = mechanize.Browser()
br.set_handle_robots(False)
br.open("https://www.goodreads.com/user/sign_in")    
br.select_form(nr=0)
br['user[email]'] = user 
br['user[password]'] = passwd
result = br.submit().read()
soup = BeautifulSoup(result,'lxml')
quoteText = soup.findAll('script')[1].string
try:
	p = re.findall(r'home:index:signed_in', quoteText)
except TypeError:
	print "Oops!  Wrong user credentials.  Try again..."

if p:
	print("Login Successful !")
	filename = raw_input("Output file location (absolute path):")
	print("Hang tight ! We're getting the data for you, based on number of likes the quotes received from readers")
	for i in (1,67,68):
		r = requests.get('https://www.goodreads.com/author/quotes/1244.Mark_Twain?page='+str(i))
		soup = BeautifulSoup(r.content,'lxml')
		quoteText = soup.findAll('div', attrs = {'class':'quoteText'})
		quoteFooterRight = soup.findAll('div', attrs = {'class':'right'})
		for (q,r) in zip(quoteText, quoteFooterRight):
			q_str = str(q.contents).replace("<br/>,",".")
			q_str = str(q.contents).replace("\u2032","")
			lines = re.findall(r'\u201c(.*)\\\u201d', str(q_str))
			line = lines[0].encode('ascii', 'ignore').decode('ascii', 'ignore')
			a.append(re.sub("  +", "", line.replace("\n", "")) + "\n")	
write = open(filename,'w+')
write.write('Top 10 popular quotes' + "\n" + "\n")
write.write('\n'.join(a[0:10]))
write.write("\n")
write.write('Least 10 popular quotes' + "\n" + "\n")
write.write('\n'.join(a[len(a)-10:]))
write.close()
print("Successful! We got the data in the file you specified")
print("Execute this command from terminal to read and enjoy Mark_Twain quotes: 'open " + filename + "'")
