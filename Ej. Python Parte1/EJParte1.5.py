print ("Ingrese su nombre: ")
nombre = input ()
print ("Ingrese su edad: ")
edad = int (input())

if edad >=13 and edad <= 15: 
    print ("El socio ", nombre, "pertenece a la categoria infantiles" )
elif edad >15 and edad <= 17: 
    print ("El socio ", nombre, "pertenece a la categoria cadetes" )
elif edad >17 and edad <= 19: 
    print ("El socio ", nombre, "pertenece a la categoria juveniles" )
elif edad >19: 
    print ("El socio ", nombre, "pertenece a la categoria mayores" )
