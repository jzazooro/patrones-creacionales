# Supongamos que tienes un conjunto de datos que contiene fechas y activaciones por día

import pandas as pd
# importame ltodo lo que hay en prueba2.py y prueba.py
from parte2 import *
from parte1 import *
import pandas as pd
from abc import ABC, abstractmethod
import statistics
import seaborn as sns
import matplotlib.pyplot as plt
from parte2 import *
from parte1 import *
from parte3 import *


#4
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


