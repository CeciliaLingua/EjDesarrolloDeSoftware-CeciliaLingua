print ("Ingrese la cantidad de invitados: ")
cantInvitados = int(input())
print ("Ingrese el precio del kilo de carne: ")
precioCarne = float(input())

kilosTotales = cantInvitados * 0.7
precioTotal = kilosTotales * precioCarne

print ("La cantidad de kilos en total son: ", kilosTotales, "Y el precio total es: ",precioTotal)
