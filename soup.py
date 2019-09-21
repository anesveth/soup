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

def myname():
    '''prints out my name'''
    return ("""\n<Sharon Anesveth Alvarado Maatens>""")

def listprinting(lista):
    '''prints out elements of a list in correct layout'''
    l=[]
    for i in range(len(lista)):
        l.append(f"\n- {lista[i]}\n")
    return l

def portal():
    #########################################TITLE
    title=soup.title.string

    #########################################FINDING PHONE NUMBER AND EMAIL
    tagcounter=0
    listofdivs=[]
    for tag in soup.find_all("div", {"id": "footer"}):
        divsubclasses = tag.find_all("div", {"class": "span4"})
        for div in divsubclasses:
            tagcounter+=1
            listofdivs.append(div)##list of tags found in div
    t=listofdivs[1].text
    listoftexts=t.split("\n")
    email=listoftexts[5].strip()
    phonenumer=listoftexts[1].strip()
    #########################################GET all items that are part of the upper nav menu (id: menu-table)
    listofnavmenuitems=[]
    for tag in soup.find_all("table", {"id": "menu-table"}):
        menukeys = tag.find_all("div", {"class": "menu-key"})
        for k in menukeys:
            k=k.text
            listofnavmenuitems.append(k.strip("\n"))
    for i in range(len(listofnavmenuitems)):
        try:
            ## gets rid of tons of unnecessary \t
            listofnavmenuitems[i]=listofnavmenuitems[i].replace("\t","")
        except:
            pass
        listofnavmenuitems[i]=(listofnavmenuitems[i].strip(" ")).strip("\n")
    #########################################  FINDS ALL PROPERTIES THAT HAVE HREF
    # properties_with_href=[]
    # for attr in soup():
    #     print(attr)

    ######################################### GET href of "UFMail" button
    for tag in soup.find_all("a",{"id":"ufmail_"}):
        ufmmail_href=(tag['href'])
    ##########################################GET href of "MiU" button
    for tag in soup.find_all("a",string="MiU"):
        miu_href=(tag['href'])

    ##########################################COUNTS <a> 
    #########################################COUNTS <a>
    a=0
    for b in soup.find_all("a"):
        a+=1
    #########################################
    print(f"""
=============================
1. Portal

GET the title and print it: {title}
---------------------------------------
GET the complete adress of UFM: {url}
------------------------------------------
GET the phone number and info email: {phonenumer}\n{email}
------------------------------------------
GET all items that are part of the upper nav menu:""")
    print(*(listprinting(listofnavmenuitems)))
    print(f"""
------------------------------------------
find all properties that have href: 
------------------------------------------
GET href of "UFMail" button: {ufmmail_href}
------------------------------------------
GET href "MiU" button: {miu_href}
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