#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json
import logging,auxiliar_for_logs


url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

def listprinting(lista):
    '''prints out elements of a list in correct layout'''
    l=[]
    for i in range(len(lista)):
        l.append(f"\n- {lista[i]}\n")
    return l


def setuplog(name,file_name):  
    '''sending output to: <logfile>'''
    #Create and configure logger 
    # logging.basicConfig(filename="logs/"+file_name+".txt",
    #                     format='%(message)s', 
    #                     filemode='w') 
    #with auxiliarmodule from log documentation, we can have more than one log at a time
    #Setting the threshold of logger to DEBUG 
    #Creating an object 
    handler = logging.FileHandler("logs/"+file_name+".txt")        

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger

def load_log(value,file_name,name_of_log):
    '''loads list into log file'''
    name_of_log=setuplog(name_of_log,file_name)
    print(f"Output exceeds 30 lines, sending output to: logs/{file_name}.txt")
    # messages
    if type(value)==list:
        for e in range(len(value)):
            string=str(value[e])
            name_of_log.debug(string+"\n")
        print("\nsuccesfully loaded")
    else:
        string=str(value)
        name_of_log.debug(string+"\n")  
    


def counter(a):
    '''counts iterations of element'''
    counter=0
    for b in soup.find_all(a):
        counter+=1
    return counter

def a_csvfile():
    '''creates a csv file with all a instances'''
    a_dict={}
    for a in soup.find_all("a"):
        text=((a.text).strip("\n")).strip("\t")
        ref=a['href']
        a_dict[text]=ref
    try:
        with open('logs/extra_as.csv', mode='w') as csv_file:
            fieldnames=['Text','href']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for k,v in a_dict.items():
                writer.writerow({'Text':str(k),'href':str(v)})
        print("Succesfully created csv file. saved in logs/extra_as.csv")
    except:
        print("could not create csv file")



#########################################
#########################################
#########################################


def portal():
    '''phase 1 project'''
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
    properties_with_hrefs=[]
    for propertyyyy in soup.find_all(href=True):
        properties_with_hrefs.append(propertyyyy)
    ######################################### GET href of "UFMail" button
    for tag in soup.find_all("a",{"id":"ufmail_"}):
        ufmmail_href=(tag['href'])
    ##########################################GET href of "MiU" button
    for tag in soup.find_all("a",string="MiU"):
        miu_href=(tag['href'])
    ########################################## GET HREFS OF ALL <img>
    imghrefs=[]
    for imgs in soup.find_all("img",src=True):
        imghrefs.append(imgs['src'])
    # log(imghrefs,'1portal_HREFS_FOR_IMGS')
    ###########################################################################################################################
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
    print("""------------------------------------------
find all properties that have href:""")
    load_log(properties_with_hrefs,'1portal_FINDS_all_properties_that_have_href','log1')
    print(f"""------------------------------------------
GET href of "UFMail" button: {ufmmail_href}
------------------------------------------
GET href "MiU" button: {miu_href}
------------------------------------------
get hrefs of all <img>: """)
    print(*(listprinting(imghrefs)))
    print(f"""------------------------------------------
Count all <a>:""")
    print(counter("a"))
    print(f"""------------------------------------------
From all (<a>) Create a csv file:""")
    a_csvfile()


