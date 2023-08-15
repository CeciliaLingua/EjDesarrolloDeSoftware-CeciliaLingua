def main ():
    valor1 = None
    valor2 = None

    while True:
        print ("1. Ingrese el valor 1")
        print ("2. Ingrese el valor 2")
        print ("3. Mostrar la suma")
        print ("4. Mostrar la resta")
        print ("5. Mostrar la multiplicacion")
        print ("6. Mostrar la division")
        print ("7. Salir")
        
        option = int(input("\nElija una opcion: "))

        if option == 1:
            valor1 = float(input("\nIngrese el valor 1:"))
        elif option == 2:
            valor2 = float(input("\nIngrese el valor 2:"))
        elif option == 3:
            if valor1 != None and valor2 != None:
                print("\nSuma:",  (valor1 + valor2))
            else:
                print("\nERROR: debe ingresar ambos valores primero")
        elif option == 4:
            if valor1 != None and valor2 != None:
                print("\nResta:",  (valor1 - valor2))
            else:
                print("\nERROR: debe ingresar ambos valores primero")
        elif option == 5:
            if valor1 != None and valor2 != None:
                print("\nMultiplicacion:",  (valor1 * valor2))
            else:
                print("\nERROR: debe ingresar ambos valores primero")
        elif option == 6:
            if valor1 != None and valor2 != None:
                if valor2 !=0:
                    print("\nDivision:",  (valor1 / valor2))
                else:
                    print("\nNo se puede dividir por cero")
            else:
                print("\nERROR: debe ingresar ambos valores primero")
        elif option == 7:
            print("Chau")
            break
        else: print("\nOpcion invalida")

if __name__ == "__main__":
    main()

