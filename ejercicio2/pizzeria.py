from abc import ABC, abstractmethod
import csv
import os.path

class PizzeriaBuilder(ABC):
    @property
    @abstractmethod
    def crear_pizza(self):
        pass

    @abstractmethod
    def crear_masa(self):
        pass

    @abstractmethod
    def crear_salsa(self):
        pass

    @abstractmethod
    def crear_ingredientes(self):
        pass

    @abstractmethod
    def crear_tecnica(self):
        pass

    @abstractmethod
    def crear_presentacion(self):
        pass

    @abstractmethod
    def crear_extras(self):
        pass

    @abstractmethod
    def crear_bebidas(self):
        pass

class Pizza:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.masa = ""
        self.salsa = ""
        self.ingredientes = []
        self.tecnica = ""
        self.presentacion = ""
        self.extras = ""
        self.bebidas = ""
    
    @property
    def pizza(self):
        pizza = [self.masa, self.salsa, self.ingredientes, self.tecnica, self.presentacion, self.extras, self.bebidas]
        self.reset()
        return pizza
    def crear_masa(self):
        masa= input("Ingrese el tipo de masa: ")
        self.masa = masa

    def crear_salsa(self):
        salsa = input("Ingrese el tipo de salsa: ")
        self.salsa = salsa

    def crear_ingredientes(self):
        respuesta = "si"
        while respuesta == "si":
            ingrediente = input("Ingrese un ingrediente: ")
            self.ingredientes.append(ingrediente)
            respuesta = input("Desea agregar otro ingrediente? si/no: ")

    def crear_tecnica(self):
        tecnica = input("Ingrese la tecnica de coccion: ")
        self.tecnica = tecnica
    
    def crear_presentacion(self):
        presentacion = input("Ingrese la presentacion: ")
        self.presentacion = presentacion

    def crear_extras(self):
        extras = input("Ingrese los extras: ")
        self.extras = extras
    
    def crear_bebidas(self):
        bebidas = input("Ingrese las bebidas: ")
        self.bebidas = bebidas
