from abstract import *
from read import *
import pandas as pd
import csv

print(data.head())
def cliente(factory: Analisis):
    creargrafica = factory.grafica()
    estadistica = factory.estadisticas()
    creargrafica.mostrar(data)
    estadistica.mostrar(data)

