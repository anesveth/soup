from bs4 import BeautifulSoup
import requests,sys,csv,json

url="http://ufm.edu/Portal"
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)
soup = BeautifulSoup(html_content, "html.parser")
##########################################Navigationg to /Estudios
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

# tagcounter=0
# listofdivs=[]
# for tag in soup.find_all("div", {"id": "topmenu"}):
#     lis = tag.find_all("li")
#     print("lis")
    #     for div in divsubclasses:
    #         tagcounter+=1
    #         listofdivs.append(div)##list of tags found in div
    # t=listofdivs[1].text
    # listoftexts=t.split("\n")
    # email=listoftexts[5].strip()
    # phonenumer=listoftexts[1].strip()

def estudios():
    '''prints phase 2'''
    print(f"""
=============================
2. Estudios

Navigate to /Estudios, obtain href from the DOM:{url}
---------------------------------------
DISPLAY all items from "topmenu": 
------------------------------------------
DISPLAY ALL "Estudios": 
------------------------------------------
DISPLAY from "leftbar" all <li> items:""")
    # print(*(listprinting(listofnavmenuitems)))
    print(f"""
------------------------------------------
GET and DISPLAY all available social media with its links (href) "class=social pull-right": 
------------------------------------------
""")
    print(f"""
------------------------------------------
Count all <a>:""")
    print(counter("a"))
    print("""------------------------------------------
""")
