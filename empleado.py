from persona import Persona

class Empleado(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__puesto = ""
        self.__turno = ""
        self.__sueldo = 0

    #Getters y Setters

    def getPuesto(self):
        return self.__puesto
    def setPuesto(self, puesto):
        self.__puesto = puesto

    def getTurno(self):
        return self.__turno
    def setTurno(self, turno):
        self.__turno = turno

    def getSueldo(self):
        return self.__sueldo
    def setSueldo(self, sueldo):
        self.__sueldo = sueldo


    def cambiar_salario(self):
        print("solicitando permiso de cambio o ascenso para cambiar el salario")
    def solicitar_permiso(self):
        print("solicitando permiso para auscencia o vacaciones o prestamo")
    def mostrar_informacion_empleado(self):
        print(f"Nombre: {self.get_nombre_persona()}, Apellido: {self.get_apellido_persona()}\n"
              f"Edad: {self.get_edad_persona()}, Puesto: {self.getPuesto()}\n"
              f"turno: {self.getTurno()}, Sueldo: {self.getSueldo()}")
