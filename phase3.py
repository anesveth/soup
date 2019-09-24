from bs4 import BeautifulSoup
import requests,sys,csv,json
from phase1 import listprinting

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

def meta_title_description():
    '''GET following <meta>: "title", "description" ("og")'''
    items=[]
    for e in soup.find_all("meta",{'property':'og:title'}):
        items.append(e['content'])
    for e in soup.find_all("meta",{'property':'og:description'}):
        items.append(e['content'])
    print(*listprinting(items))
    #      for li in e.find_all("li"):
    #         items.append((li.text).strip(" "))
    # print(*(listprinting(items)))
def download(imgsrc,filename):
    '''downloads file from source'''
    myfile = requests.get(imgsrc)
    open(f'logs/{filename}', 'wb').write(myfile.content)

def facultad_ciencias_economicas_logo():
    '''Downloads the "FACULTAD de CIENCIAS ECONOMICAS" logo'''
    for div in soup.find_all("div",{'class':'fl-photo-content fl-photo-img-png'}):
        for a in div.find_all("a"):
            for link in a.find_all("img"):
                imgsrc=(link['src'])
    print("\n"+imgsrc)
    download(imgsrc,'ciencias_economicas_logo.png')

def cs():
    '''prints phase 3'''
    print(f"""
=============================
3. CS

GET title: {title}
---------------------------------------
GET and display the href: """)

    print("""
------------------------------------------
Download the "FACULTAD de CIENCIAS ECONOMICAS" logo. (you need to obtain the link dynamically):""")
    facultad_ciencias_economicas_logo()
    print("""------------------------------------------
GET following <meta>: "title", "description" ("og"):""")
    meta_title_description()
    # print(*(listprinting(listofnavmenuitems)))
    print(f"""------------------------------------------
Count all <a>:""")
    print(counter("a"))
    print(f"""------------------------------------------
Count all <div>:""")
    print(counter("div"))
    print("""------------------------------------------
""")
