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
        if email[0] =='a':
            counter+=1
        if email[0] =='e':
            counter+=1
        if email[0] =='i':
            counter+=1
        if email[0] =='o':
            counter+=1
        if email[0] =='u':
            counter+=1
    print (counter)

# def createcsv(dictionaryy,filename,field_names):
#     with open(filename, mode='w') as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=field_names)
#         writer.writeheader()
#         for k,v in dictionaryy:
#             writer.writerow({k:v})
        # writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
        # writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

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
    vowelcounting(get_emails())
    print("""------------------------------------------
Group in a JSON all rows that have Same Address (dont use Room number) as address, dump it to logs/4directorio_address.json: """)


