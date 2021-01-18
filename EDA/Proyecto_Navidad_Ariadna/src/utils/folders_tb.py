'''
Date:201211
Este modulo se basa en funciones para el tratamiento de las BDD que muchas veces no se envian sin deduplicar, depurar o incluso crear tablas.
'''
import json #Instalado
import requests #Instalado
import pandas as pd #Instalado


def readcsv():
    df = pd.read_csv("/Users/ariadnapuigventos/Documents/CURSOS/BRIDGE/DS_Ejercicios_Python/BootCamp_TheBridge/Proyecto_Navidad_Ariadna/documentation/world_marathon_majors.csv", sep = ";")
    print(df)

def readurl():
    df = pd.read_csv("/Users/ariadnapuigventos/Documents/CURSOS/BRIDGE/DS_Ejercicios_Python/BootCamp_TheBridge/Proyecto_Navidad_Ariadna/documentation/altitud_countries.csv", sep= "\t")
    print(df)

def readbdd(url):
    df = pd.read_csv(url, sep= ";")
    return df
