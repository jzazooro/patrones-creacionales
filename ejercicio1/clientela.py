from abstract import *
from read import *
import pandas as pd
import csv

direccion = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

data = pd.read_csv(direccion, sep= ";", encoding= "ISO-8859-1")

print(data.head())
def cliente(factory: Analisis):
    creargrafica = factory.grafica()
    estadistica = factory.estadisticas()
    creargrafica.mostrar(data)
    estadistica.mostrar(data)