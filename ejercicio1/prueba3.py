# Supongamos que tienes un conjunto de datos que contiene fechas y activaciones por día

import pandas as pd
# importame ltodo lo que hay en prueba2.py y prueba.py
from prueba2 import *
from prueba import *


URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

datos = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

print(datos.head())  


datos_activaciones = [
    {'fecha': '2023-11-01', 'activaciones': 10},
    {'fecha': '2023-11-02', 'activaciones': 15},
    {'fecha': '2023-11-03', 'activaciones': 8},
    # ... más datos ...
]

# Fábrica para análisis estadístico
class AnalisisEstadisticoFactory(AnalisisFactory):
    def crear_analisis(self):
        return AnalisisEstadistico()

# Fábrica para visualizaciones gráficas
class VisualizacionGraficaFactory(VisualizacionFactory):
    def crear_visualizacion(self):
        return VisualizacionGrafica()

# Analizar la media de activaciones por día
fabrica_analisis = AnalisisEstadisticoFactory()
analisis = fabrica_analisis.crear_analisis()

# Extraer las activaciones para el análisis estadístico
activaciones_por_dia = [dato['activaciones'] for dato in datos_activaciones]
resultado_analisis = analisis.realizar_analisis(activaciones_por_dia)

# Imprimir la media de activaciones por día
print("Media de activaciones por día:", resultado_analisis['media'])

# Visualizar un histograma de las activaciones
fabrica_visualizacion = VisualizacionGraficaFactory()
visualizacion = fabrica_visualizacion.crear_visualizacion()
visualizacion.crear_visualizacion(activaciones_por_dia)
