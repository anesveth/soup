FROM python:3-alpine
#donde vamos a trabajar (como home)
WORKDIR /soup
#Con este comando se crea una carpeta
RUN mkdir /soup
#Copiamos archivo a locacion /carpetaPrograna
COPY requirements.txt /soup
#instalas los requerimentos 
RUN pip install -r requirements.txt
#transferis tu programa
COPY soup.py /soup
#Asi podes transferir todo menos lo que este en .docker ignore
COPY . /soup
#corres tu programa
CMD [ "python3", "soup.py" ]
#Le podes poner tu nombre o borrarlo
ENV DEVELOPER="Anesveth Maatens"