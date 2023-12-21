from abc import ABC, abstractmethod
from math import pi

#definicion de clase abstracta que hereda de ABC
class GeometricFigure(ABC):
    #metodo abstracto para que sea implementado solo por las clases hijas
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

#clase concreta Square que hereda de la clase abstracta GemoetricFigure
class Square(GeometricFigure):
    #contructor que define el paramentro lado
    def __init__(self, side):
        self.side = side
    #implementacion metodos abstractos
    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side
    
#clase concreta Circle que hereda de la clase abstracta GemoetricFigure
class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.radius
    
#manejo de inputs y gestion de errores   
def get_user_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Error: Ingresa un número válido.")

# Input values from the user with error handling
side= get_user_input("Ingresa la longitud del cuadrado del cual deseas calcular sus valores: ")
radius= get_user_input("Ingresa la longitud del radio del círculo para calcular sus valores correspondientes: ")


#creacion de instancias de las clases concretas
square=Square(side)
circle=Circle(radius)

#creacion de lista contenedora de instancias
figure_collection = [square, circle]

#iteracion para determinar el tipo de figura al que pertenece el dato
for figure in figure_collection:
    if isinstance(figure, Square):
        figure_type = "Square"
    elif isinstance(figure, Circle):
        figure_type = "Circle"
    else:
        figure_type = "Unknown Figure"

    print(f"{figure_type} - Area: {figure.calculate_area()}, Perimeter: {figure.calculate_perimeter()}")