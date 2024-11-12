class Persona:
    def __init__(self):
        self.__nombre_persona = ""
        self.__apellido_persona = ""
        self.__edad_persona = 0

    #Getters y Setters

    def get_nombre_persona(self):
        return self.__nombre_persona

    def set_nombre_persona(self, nombre_persona):
        self.__nombre_persona = nombre_persona

    def get_apellido_persona(self):
        return self.__apellido_persona

    def set_apellido_persona(self, apellido_persona):
        self.__apellido_persona = apellido_persona

    def get_edad_persona(self):
        return self.__edad_persona
    def set_edad_persona(self, edad_persona):
        self.__edad_persona = edad_persona