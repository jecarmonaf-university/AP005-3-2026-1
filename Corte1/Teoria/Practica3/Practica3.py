while True:

    a = input("Por favor ingrese un valor: ")
    print(a)

    mod = int(a) % 2
    print(mod)

    if(mod == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
    m = int(input("Ingrese 1 para continuar y cero para terminar: "))
    if (m == 0):
        break