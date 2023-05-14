'''
* Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área
 * de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.

# 02:12
# 02:29
# 17 min
def area_poligono(polig, base, altura = 0):
    if polig == 'triángulo':
        area = base * altura / 2
    elif polig == 'cuadrado':
        area = base**2
    else:
        area = base * altura
    return area

print("El área de un triágulo de base 3 y altura 1.5 es:", area_poligono("triángulo", 3, 1.5))
print("El área de un cuadrado de base 5 es:", area_poligono("cuadrado", 5))
print("El área de un rectángulo de base 2 y altura 7 es:", area_poligono("rectángulo", 2, 7))
'''
#-------------------------------------------------------------------------------------
#14/05/2023
class Rectangle:
    def __init__(self, width = 0, length = 0):
        self.width = width
        self.length = length

    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.length

    def area(self):
        return self.width * self.length

class Triangle(Rectangle):
    def __init__(self, base, length):
        super().__init__(base, length)
    
    def get_base(self):
        return self.width
    
    def area(self):
        # return self.width * self.length / 2
        return super().area() / 2

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def get_side(self):
        return self.width

rectangle = Rectangle(2, 7) 
triangle = Triangle(3, 1.5)
square = Square(5)

print("El área de un rectángulo de base", rectangle.get_width(),"y altura", rectangle.get_length(),"es:", rectangle.area())
print("El área de un triágulo de base", triangle.get_base(),"y altura", triangle.get_length(),"es:", triangle.area())
print("El área de un cuadrado de lado", square.get_side(),"es:", square.area())
