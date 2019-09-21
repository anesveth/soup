from bs4 import BeautifulSoup
import requests,sys,csv,json

url="https://fce.ufm.edu/carrera/cs/"
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
    counter=0
    for b in soup.find_all(a):
        counter+=1
    return counter

def cs():
    '''prints phase 3'''
    print(f"""
=============================
3. CS

GET title:
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
    print(f"""------------------------------------------
Count all <div>:""")
    print(counter("div"))
    print("""------------------------------------------
""")
