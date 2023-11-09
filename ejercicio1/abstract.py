from abc import ABC, abstractmethod
from pandas import *
import matplotlib as plt
from read import *

class Analisis(ABC):
    @abstractmethod
    def grafica(self):
        pass
    @abstractmethod
    def estadisticas(self):
        pass

class Factoria1(Analisis):
    def grafica(self):
        return grafica_de_barras()
    def estadisticas(self):
        return analisis_de_mediana()

class Factoria2(Analisis):
    def grafica(self):
        return grafica_de_histograma()
    def estadisticas(self):
        return analisis_de_media()

class Grafica(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class Estadistica(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class grafica_de_barras(Grafica):
    def mostrar(self, data):
        data['FECHA']=to_datetime(data['FECHA'])
        data['MES']=data['FECHA'].dt.month
        activacion_por_mes=data['MES'].value_counts().sort_index()
        activacion_por_mes.plot(kind='bar', color='green', edgecolor='black')
        plt.title("Activaciones por mes")
        plt.show()    

class grafica_de_histograma(Grafica):
    def mostrar(self, data):
        activacion_por_tipo=data['TITULO'].value_counts()
        activacion_por_tipo.plot(kind='bar', color='green', edgecolor='black')
        plt.title("histograma por tipo de emergencia")
        plt.show()   

class analisis_de_media(Analisis):
    def mostrar(self, data):
        data['FECHA']=to_datetime(data['FECHA'])
        data['DIA']=data['FECHA'].dt.day
        activacion_por_dia=data['DIA'].value_counts().sort_index()
        print("La media de activaciones por día es: "+ str(activacion_por_dia.mean()))
        return activacion_por_dia.mean()
    
class analisis_de_mediana(Analisis):
    def mostrar(self, data):
        data['FECHA']=to_datetime(data['FECHA'])
        data['DIA']=data['FECHA'].dt.day
        activacion_por_dia=data['DIA'].value_counts().sort_index()
        print("La mediana de activaciones por día es: "+ str(activacion_por_dia.median()))
        return activacion_por_dia.median()