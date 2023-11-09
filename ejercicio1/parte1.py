import pandas as pd

from abc import ABC, abstractmethod
import statistics


#3.1
# Interfaz Abstracta para la fábrica de análisis
class AnalisisFactory(ABC):
    @abstractmethod
    def crear_analisis(self):
        pass

# Clase concreta de la fábrica para análisis estadísticos
class AnalisisEstadisticoFactory(AnalisisFactory):
    def crear_analisis(self):
        return AnalisisEstadistico()

# Interfaz Abstracta para los análisis
class Analisis(ABC):
    @abstractmethod
    def realizar_analisis(self, datos):
        pass

# Clase concreta para análisis estadístico
class AnalisisEstadistico(Analisis):
    def realizar_analisis(self, datos):
        # Realizar análisis estadístico utilizando la biblioteca statistics de Python
        media = statistics.mean(datos)
        mediana = statistics.median(datos)
        moda = statistics.mode(datos)

        # Devolver los resultados del análisis
        return {
            'media': media,
            'mediana': mediana,
            'moda': moda
        }

# Cliente que utiliza la fábrica y los análisis
class Clientela:
    def __init__(self, fabrica):
        self.fabrica = fabrica

    def realizar_analisis(self, datos):
        analisis = self.fabrica.crear_analisis()
        resultados = analisis.realizar_analisis(datos)
        return resultados

