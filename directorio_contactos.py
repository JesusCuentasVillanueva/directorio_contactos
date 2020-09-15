directorio={"usuario":000}



def ingresar_contacto():
    llave = input("Ingresa el nombre del contacto -->  ")
    numero_telefono = int(input("Ingresa su numero telefonico -->  "))
    for i in directorio.keys():
        if llave != i:
            directorio[llave]=numero_telefono
            print("Contacto agregado con EXITO!")
            break
        else:
            print("El nombre de contacto ya existe")



def main():
    while True:
        print("Bienvenido a nuestro directorio")
        print("-------------------------------")
        print("1.-Ingresar un nuevo contacto")
        print("2.-Ver contactos")
        print("3.-Salir")
        print("")
        opcion = int(input("Elige una opcion -->  "))
        if opcion == 1:
            ingresar_contacto()
        elif opcion == 2:
            print(directorio)
        elif opcion == 3:
            break
        else:
            print("Escoge una opcion valida".upper())


if __name__=="__main__":
    main()