from director import Director
from gerente import Gerente
from jefe_area import Jefe_Area

director = Director()

director.set_nombre_persona("Rick")
director.set_apellido_persona("Sanchez")
director.set_edad_persona(60)

director.setPuesto("Director")
director.setTurno("Matutino")
director.setSueldo(95000)

director.set_nombre_area("Administrativa")
director.set_presupuesto(500000)
director.set_nombre_departamento("Administrativa general")
director.set_no_empleados(58)

director.setRegion("Monterrey")
director.setPresupuesto_asignado(500000)



jefe_area = Jefe_Area()

jefe_area.set_nombre_persona("Daniel")
jefe_area.set_apellido_persona("Vargas")
jefe_area.set_edad_persona(52)

jefe_area.setPuesto("Jefe de Area")
jefe_area.setTurno("Matutino")
jefe_area.setSueldo(32000)

jefe_area.set_nombre_area("Administrativa")
jefe_area.set_presupuesto(150000)
jefe_area.set_nombre_departamento("Administrativa General")
jefe_area.set_no_empleados(30)




gerente = Gerente()

gerente.set_nombre_persona("Juan")
gerente.set_apellido_persona("Morales")
gerente.set_edad_persona(25)

gerente.setPuesto("Gerente")
gerente.setTurno("Matutino")
gerente.setSueldo(45000)

gerente.set_nombre_area("Administrativa")
gerente.set_presupuesto(200000)
gerente.set_nombre_departamento("Administrativa General")
gerente.set_no_empleados(15)



print("Informacion de Empleados")
print("")
director.mostrar_informacion_empleado()
print("")
jefe_area.mostrar_informacion_empleado()
print("")
gerente.mostrar_informacion_empleado()
print("")

print("\nInformacion por Areas")
print("")
director.mostrar_informacion_area()
print("")
jefe_area.mostrar_informacion_area()
print("")
gerente.mostrar_informacion_area()