from empleado import Empleado
from area import Area


class Jefe_Area(Area,Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self.objetivo_area = ""

    #Getter y Setter

    def get_objetivo_area(self):
            return self.objetivo_area
    def set_objetivo_area(self, object_area):
            self.objetivo_area = object_area

    #metodos particulares
    def asignar_supervisor(self):
        print("el nuevo supervisor es x")
    def ccnvocar_reunion(self):
        print("llamando a la gente....")