from bs4 import BeautifulSoup
import requests,sys,csv,json
from phase1 import listprinting

url="http://ufm.edu/Portal"
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)
soup = BeautifulSoup(html_content, "html.parser")
##########################################Navigating to /Estudios
for tag in soup.find_all("a",string="Estudios"):
    ref_for_estudios=tag['href']
url=f"http://ufm.edu{ref_for_estudios}"
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)
soup = BeautifulSoup(html_content, "html.parser")
########################################
######################################## FUNCTIONS
########################################

def counter(a):
    '''counts iterations of element'''
    counter=0
    for b in soup.find_all(a):
        counter+=1
    return counter

def topmenuitems():
    '''DISPLAY all items from "topmenu":'''
    items=[]
    for e in soup.find_all("div",{'id':'topmenu'}):
        for li in e.find_all("li"):
            items.append((li.text).strip(" "))
    print(*(listprinting(items)))

def all_estudios():
    '''DISPLAY ALL "Estudios"'''
    items=[]
    for e in soup.find_all("div",{"class":"estudios"}):
        items.append((e.text).strip(" "))
    print(*(listprinting(items)))

def leftbar():
    '''DISPLAY from "leftbar" all <li> items:'''
    items=[]
    for e in soup.find_all("div",{"class":"leftbar"}):
        for li in e.find_all("li"):
            items.append((li.text).strip(" "))
    print(*(listprinting(items)))

def social_pull_right():
    '''GET and DISPLAY all available social media with its links (href) "class=social pull-right"'''
    items=[]
    for e in soup.find_all("div",{"class":"social pull-right"}):
        for a in e.find_all("a"):
            items.append(a['href'])
    print(*(listprinting(items)))

def estudios():
    '''prints phase 2'''
    print(f"""
=============================
2. Estudios

Navigate to /Estudios, obtain href from the DOM:{url}
---------------------------------------
DISPLAY all items from "topmenu":""")
    (topmenuitems())
    print("""------------------------------------------
DISPLAY ALL "Estudios":""")
    all_estudios()
    print("""------------------------------------------
DISPLAY from "leftbar" all <li> items:""")
    leftbar()
    # print(*(listprinting(listofnavmenuitems)))
    print(f"""------------------------------------------
GET and DISPLAY all available social media with its links (href) "class=social pull-right": """)
    social_pull_right()
    print(f"""------------------------------------------
Count all <a>:""")
    print(counter("a"))


