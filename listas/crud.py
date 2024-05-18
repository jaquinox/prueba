

animales = ["perro", "gato", "leon", "jirafa"]


running = True

while running:
    print("Mi Zoologico \n")
    print("Opciones\n")
    opciones = int(input("Ingresa una opcion: \n1. Agregar un Animal\n2. Mostrar Animales\n3. Eliminar por indice\n4. Eliminar por nombre\n5. Salir\nIngrese: "))

    if opciones == 1:
        animal = input("ingrese un Animal: ")
        animales.append(animal)

    elif opciones == 2:
        print(animales)

    elif opciones == 3:
        eliminar_index = int(input("ingrese el indice: "))
        animales.pop(eliminar_index)

    elif opciones == 4:
        eliminar_palabra = input("ingrese el animal a eliminar: ")
        animales.remove(eliminar_palabra)


    elif opciones == 5:
        running = False


   

    print("\n")