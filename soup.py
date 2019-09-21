#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json
import sys

url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
#print(soup.prettify())
# for div in soup.find_all("div"):
#     print(div)
#     print("--------------------------")


# print(soup.title)
# print(soup.title.string)


def myname():
    return ("""\n<Sharon Anesveth Alvarado Maatens>""")

def portal():
    a=0
    for b in soup.find_all("a"):
        a+=1
    # for b in soup.find_all("div",{"class":"span4"}):
    #     #phonen is a tag now
    #     print(b['href'])
    #     print("---------")

    print(f"""
=============================
1. Portal

GET the title and print it: {soup.title.string}
---------------------------------------
GET the complete adress of UFM: {url}
------------------------------------------
GET the phone number and info email: Teléfono: ,
------------------------------------------
GET all item that are part of the upper nav menu: 
------------------------------------------
find all properties that have href: 
------------------------------------------
GET href of "UFMail" button: 
------------------------------------------
GET href "MiU" button: 
------------------------------------------
get hrefs of all <img>: 
------------------------------------------
Count all <a>: {a}
------------------------------------------
""")


# 1. Portal
# # item_title: <result>
# GET the title and print it: <result>
# ---------------------------------------
# GET the Complete Address of UFM: <result>
# ------------------------------------------
# .
# .
# .
# find all properties that have href (link to somewhere):
# - <result 1>
# - <result 2>
# - <result 3>
# =============================
# 2. Estudios
# # ----- : separator between items

# # ===== : separator between parts

# # 1. Title: Title of the section

# # use '-' if its a list

def main():
    choice=(sys.argv)
    try:
        if choice[1]=="1":
            print(myname())
            print(portal())
        if choice[1]=="2":
            pass
        if choice[1]=="3":
            pass
        if choice[1]=="4":
            pass
    except:
        print(myname())
        print(portal())

main()