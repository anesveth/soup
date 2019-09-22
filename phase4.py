from bs4 import BeautifulSoup
import requests,sys,csv,json
import logging
from phase1 import listprinting,log

url="https://www.ufm.edu/Directorio"
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

soup = BeautifulSoup(html_content, "html.parser")

def get_emails():
    emaillist=[]
    for element in soup.find_all("div",{'id':'mw-content-text'}):
        for table in element.find_all("table",{'class':'tabla ancho100'}):
            for tr in table.find_all("td"):
                try:
                    for a in tr.find_all("a",href=True):
                        mail=a.text
                        if (a['href'])==(f"mailto:{mail}"):
                            emaillist.append(a.text)
                except:
                    print("error while collecting emails")
    emaillist=sorted(emaillist)
    return emaillist

def vowelcounting(emaillist):
    counter=0
    for i in range(len(emaillist)):
        email=emaillist[i]
        print(email[0])


def directorio():
    '''prints phase 4'''
    print(f"""
=============================
4. Directorio

Sort all emails alphabetically (href="mailto:arquitectura@ufm.edu") in a list, dump it to logs/4directorio_emails.txt:
""")
    log(get_emails(),'4directorio_emails')
    print("""---------------------------------------
Count all emails that start with a vowel: """)
    
    print("""------------------------------------------
Group in a JSON all rows that have Same Address (dont use Room number) as address, dump it to logs/4directorio_address.json: """)


