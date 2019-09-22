from bs4 import BeautifulSoup
import requests,sys,csv,json

url="https://fce.ufm.edu/carrera/cs/"
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

soup = BeautifulSoup(html_content, "html.parser")
title=soup.title.string

########################################
######################################## FUNCTIONS
########################################

def counter(a):
    '''counts iterations of element'''
    counter=0
    for b in soup.find_all(a):
        counter+=1
    return counter

def cs():
    '''prints phase 3'''
    print(f"""
=============================
3. CS

GET title: {title}
---------------------------------------
GET and display the href: 
------------------------------------------
Download the "FACULTAD de CIENCIAS ECONOMICAS" logo. (you need to obtain the link dynamically): 
------------------------------------------
GET following <meta>: "title", "description" ("og"):""")
    # print(*(listprinting(listofnavmenuitems)))
    print(f"""
------------------------------------------
Count all <a>:""")
    print(counter("a"))
    print(f"""------------------------------------------
Count all <div>:""")
    print(counter("div"))
    print("""------------------------------------------
""")
