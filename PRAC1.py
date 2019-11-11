# -*- coding: utf-8 -*-
"""
@author: Rafa
"""

import requests
from bs4 import BeautifulSoup
import csv

# Indicar la ruta
url_page = 'https://datosmacro.expansion.com/paro/espana/municipios'

# Beautiful Soup
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")

# Obtenemos la tabla basandonos en los Id's que tienen

ids=['tb2_1','tb3_1','tb2_2','tb3_2','tb2_3','tb3_3','tb2_4','tb3_4']

#Creamos el csv y le añadimos los encabezados

with open('paro.csv','a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Municipio','Tasa paro','Parados','Poblacion'])

#Para cada uno de las tablas obtenemos los valores de las celdas que nos interesan

for i in range(len(ids)):
    
    tabla = soup.find('table', attrs={'id': ids[i]})
    
    municipio=""
    tasa=""
    num=""
    pob=""
    nroFila=0
    for fila in tabla.find_all("tr"):
        if nroFila >=1:
            nroCelda=0
            for celda in fila.find_all('td'):
                #Municipio
                if nroCelda==1:
                    municipio=celda.text
                    #print("mun", municipio)
                #Tasa
                if nroCelda==2:
                    tasa=celda.text
                    #print("tasa:", tasa)
                #Parados
                if nroCelda==4:
                    num=celda.text
                    #print("parados:", num)
                #Poblacion
                if nroCelda==5:
                    pob=celda.text
                    #print("pob", pob)
                nroCelda=nroCelda+1
            #Grabamos los datos en un csv
            with open('paro.csv','a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([municipio,tasa,num,pob])
        nroFila=nroFila+1
