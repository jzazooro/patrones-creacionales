import pandas as pd
import csv

direccion = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

data = pd.read_csv(direccion, sep= ";", encoding= "ISO-8859-1")

print(data.head())