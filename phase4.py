from bs4 import BeautifulSoup
import requests,sys,csv
import json
import logging, auxiliar_for_logs
from phase1 import listprinting,load_log,setuplog


url="https://www.ufm.edu/Directorio"
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

soup = BeautifulSoup(html_content, "html.parser")


def json_writing(dictionary,filename):
    '''writes json based on introduced dictionary'''
    try:
        with open("logs/"+filename, 'w+') as json_file:
            json.dump(dictionary, json_file)
        print(f"\nSuccesfully created json file. saved in logs/{filename}")        
    except:
        print("\nCould not create json file") 


def get_emails():
    '''gets emails from table, returns email list'''
    emaillist=[]
    for element in soup.find_all("div",{'id':'mw-content-text'}):
        for table in element.find_all("table",{'class':'tabla ancho100'}):
            for td in table.find_all("td"):
                try:
                    for a in td.find_all("a",href=True):
                        mail=(a.text).strip(" ")
                        if (a['href'])==(f"mailto:{mail}"):
                            emaillist.append(a.text)
                except:
                    print("error while collecting emails")
    emaillist=sorted(emaillist)
    return emaillist

def get_adress():
    '''Groups in a JSON all rows that have Same Address (doesn't use Room number) as address'''
    listfordict=[]
    c=0
    places_with_adresses=dict()
    adresses=['Edificio Académico','Edificio Escuela','6 Avenida 7-55',
    'Edificio Centro Estudiantil','Centro Estudiantil','6 Calle 7-11',
    'Edificio Biblioteca','Centro Cultural, 1 nivel','Centro Cultural, 2 nivel',
    'Centro Cultural, 3 nivel','Centro Cultural, Auditorio']
    # "," , " "
    for element in soup.find_all("div",{'id':'mw-content-text'}):   
        tables=element.find_all("table",{'class':'tabla ancho100'})
        for rows in tables[0].find_all("tr"):
            cells=rows.find_all("td")    
            if len(cells) == 5:
                ad=(((((cells[4]).text).strip(" ")).strip(",")).strip("\n"))
                if c==6:
                    ad=ad.split("\n")
                    c+=1
                else:
                    ad=ad.split(",")
                if len(ad)==2:
                    ad=ad[0]
                place=((cells[0]).text)
                both=[ad,place]
                listfordict.append(both)
    for e in range(len(listfordict)):
        line=listfordict[e]
        ad=line[0]
        if type(ad)==list:
            ad=((str(ad)).strip("['")).strip("']")
        place=line[1]
        if ad in places_with_adresses:
            places_with_adresses[ad].append(place)
        else:
            places_with_adresses[ad]=[place]
    json_writing(places_with_adresses,'4directorio_address.json')
                


def get_decanos_directores():
    '''LOADS ONTO A JSON Faculty Dean and Directors, and dump it to logs/4directorio_deans.json'''
    listfordict=[]
    faculties=[]
    finaldict={}
    # "," , " "
    for element in soup.find_all("div",{'id':'mw-content-text'}):
        tables=element.find_all("table",{'class':'tabla ancho100 col3'})
        for tr in tables[1].find_all("tr"):
            tds=tr.find_all("td")
            if len(tds) == 3:
                directores=((tds[1]).text)
                facultad=((((tds[0]).text).strip(" ")).strip("\n"))
                faculties.append(facultad)
                email=((tds[2]).text)

                for element in soup.find_all("div",{'id':'mw-content-text'}):
                    tables=element.find_all("table",{'class':'tabla ancho100'})
                    for tr in tables[0].find_all("tr"):
                        tds=tr.find_all("td")
                        if len(tds) == 5:
                            phone=((tds[2]).text)
                            facultad_de_esta_tabla=(((tds[0]).text).strip(" ")).strip("\n")
                            facultad_to_look_for=((facultad.replace("Facultad de","")).strip(" "))
                            if facultad_de_esta_tabla==facultad_to_look_for:
                                conjunction=[facultad,directores,email,phone]
                                listfordict.append(conjunction)
    for e in range(len(listfordict)):
        line=listfordict[e]
        key=line[0]
        if type(key)==list:
            key=((str(key)).strip("['")).strip("']")
        director=line[1]
        email=line[2]
        phone=line[3]
        data={"Dean/Director":director,"email":email,"Phone Number":phone}
        if key in finaldict:
            finaldict[key].append(data)
        else:
            finaldict[key]=[data]
    json_writing(finaldict,'4directorio_deans.json')
     

def directory_all_3_column_table():
    '''GET the directory of all 3 column table and generates a CSV with these columns'''
    listfordict=[]
    # "," , " "
    for element in soup.find_all("div",{'id':'mw-content-text'}):
        tables=element.find_all("table",{'class':'tabla ancho100 col3'})
        for table in range(len(tables)):
            for tr in tables[table].find_all("tr"):
                tds=tr.find_all("td")
                if len(tds) == 3:
                    Entity=((tds[0]).text)
                    FullName=((((tds[1]).text).strip(" ")).strip("\n"))
                    Email=((tds[2]).text)
                    conjunction={"Entity":Entity,"FullName":FullName,"Email":Email}
                    listfordict.append(conjunction)
                    
    try:
        with open('logs/4directorio_3column_tables.csv', mode='w') as csv_file:
            fieldnames=['Entity','FullName','Email']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for e in range(len(listfordict)):
                dictionary=listfordict[e]
                for k,v in dictionary.items():
                    writer.writerow({k:v})
     
        print("\nSuccesfully created csv file. saved in logs/extra_as.csv")        
    except:
        print("\nCould not create csv file")
 
def vowelcounting(emaillist):
    '''counts all items that star with vowels in list'''
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

def directorio():
    '''prints phase 4'''
    print(f"""
=============================
4. Directorio

Sort all emails alphabetically (href="mailto:arquitectura@ufm.edu") in a list, dump it to logs/4directorio_emails.txt:
""")
    load_log(get_emails(),'4directorio_emails','log2')
    print("""---------------------------------------
Count all emails that start with a vowel: """)
    vowelcounting(get_emails())
    print("""------------------------------------------
Group in a JSON all rows that have Same Address (dont use Room number) as address, dump it to logs/4directorio_address.json: """)
    get_adress()
    print("""------------------------------------------
Try to correlate in a JSON Faculty Dean and Directors, and dump it to logs/4directorio_deans.json: """)
    get_decanos_directores()
    print("""------------------------------------------
GET the directory of all 3 column table and generate a CSV with these columns (Entity,FullName, Email), and dump it to logs/4directorio_3column_tables.csv: """)
    directory_all_3_column_table()


