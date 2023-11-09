import pandas as pd
from abc import ABC, abstractmethod
import statistics
import seaborn as sns
import matplotlib.pyplot as plt
from parte1 import *
from parte2 import *
from parte3 import *
from parte2 import Cliente
from parte1 import Clientela


def main():
    reiter= "si"
    while reiter == "si":
        ej= input("Ingrese el numero de apartado: 1/2/3.1/3.2/4 ")
        
        if ej == "1":
            URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"
            datos = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')
            print(datos.head())  
            reiter= (input("Desea ver otro apartado? si o no "))
        
        elif ej == "2":
            print("No funciona el codigo realizado para este apartado")
            reiter= (input("Desea ver otro apartado? si o no "))
        
        elif ej == "3.1":
            fabrica_estadistica = AnalisisEstadisticoFactory()
            cliente = Clientela(fabrica_estadistica)
            datos_ejemplo = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
            resultados_estadisticos = Clientela.realizar_analisis(datos_ejemplo)
            print("Resultados del análisis estadístico:")
            for clave, valor in resultados_estadisticos.items():
                print(f"{clave}: {valor}")
            reiter= (input("Desea ver otro apartado? si o no "))
                
        elif ej == "3.2":
            fabrica_visualizacion = VisualizacionGraficaFactory()
            cliente = Cliente(fabrica_visualizacion)
            datos_ejemplo = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
            cliente.crear_y_mostrar_visualizacion(datos_ejemplo)
            reiter= (input("Desea ver otro apartado? si o no "))
            
        elif ej == "4":
            fabrica_analisis = AnalisisEstadisticoFactory()
            analisis = fabrica_analisis.crear_analisis()
            activaciones_por_dia = [dato['activaciones'] for dato in datos_activaciones]
            resultado_analisis = analisis.realizar_analisis(activaciones_por_dia)
            print("Media de activaciones por día:", resultado_analisis['media'])
            fabrica_visualizacion = VisualizacionGraficaFactory()
            visualizacion = fabrica_visualizacion.crear_visualizacion()
            visualizacion.crear_visualizacion(activaciones_por_dia)
            reiter= (input("Desea ver otro apartado? si o no "))
            
        else: 
            print("No existe ese apartado")
if __name__ == "__main__":
    main()