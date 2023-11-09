import pandas as pd

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

datos = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

print(datos.head())  

from abc import ABC, abstractmethod
import statistics

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
class Cliente:
    def __init__(self, fabrica):
        self.fabrica = fabrica

    def realizar_analisis(self, datos):
        analisis = self.fabrica.crear_analisis()
        resultados = analisis.realizar_analisis(datos)
        return resultados

# Uso del patrón Abstract Factory
if __name__ == "__main__":
    # Crear una fábrica de análisis estadísticos
    fabrica_estadistica = AnalisisEstadisticoFactory()

    # Crear un cliente que utiliza la fábrica de análisis estadísticos
    cliente = Cliente(fabrica_estadistica)

    # Datos de ejemplo para el análisis
    datos_ejemplo = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

    # Realizar el análisis estadístico
    resultados_estadisticos = cliente.realizar_analisis(datos_ejemplo)

    # Imprimir los resultados
    print("Resultados del análisis estadístico:")
    for clave, valor in resultados_estadisticos.items():
        print(f"{clave}: {valor}")

