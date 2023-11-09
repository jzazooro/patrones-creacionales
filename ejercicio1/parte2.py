from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from parte1 import *




#3.2
# Interfaz Abstracta para la fábrica de visualizaciones
class VisualizacionFactory(ABC):
    @abstractmethod
    def crear_visualizacion(self):
        pass

# Clase concreta de la fábrica para visualizaciones gráficas
class VisualizacionGraficaFactory(VisualizacionFactory):
    def crear_visualizacion(self):
        return VisualizacionGrafica()

# Interfaz Abstracta para las visualizaciones
class Visualizacion(ABC):
    @abstractmethod
    def crear_visualizacion(self, datos):
        pass

# Clase concreta para visualizaciones gráficas
class VisualizacionGrafica(Visualizacion):
    def crear_visualizacion(self, datos):
        # Crear un DataFrame con los datos (puedes adaptarlo según tus necesidades)
        df = pd.DataFrame({'Datos': datos})

        # Crear un histograma y un gráfico de barras utilizando Seaborn
        plt.figure(figsize=(10, 6))
        plt.subplot(2, 1, 1)
        sns.histplot(df['Datos'], kde=False)
        plt.title('Histograma')

        plt.subplot(2, 1, 2)
        sns.countplot(x='Datos', data=df)
        plt.title('Gráfico de Barras')

        # Mostrar las visualizaciones
        plt.tight_layout()
        plt.show()

# Cliente que utiliza la fábrica y las visualizaciones
class Cliente:
    def __init__(self, fabrica):
        self.fabrica = fabrica

    def crear_y_mostrar_visualizacion(self, datos):
        visualizacion = self.fabrica.crear_visualizacion()
        visualizacion.crear_visualizacion(datos)          