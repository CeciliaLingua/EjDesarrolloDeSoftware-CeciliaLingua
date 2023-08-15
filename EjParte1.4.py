print ("Ingrese el monto de la compra: ")
monto = float (input())
porcentajeAumento = 10
if monto >= 3500: 
    descuento = monto * (porcentajeAumento/100)
    descuento1 = monto - descuento
    print ("El monto final es:", descuento1)
else: print ("El monto final es: ", monto)

