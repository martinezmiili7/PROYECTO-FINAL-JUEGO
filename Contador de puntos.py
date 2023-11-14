class ContadorDePuntos:
    def __init__(self):
        self.puntos = 0
        print("Puntos iniciales:", self.obtener_puntos())

    def sumar_puntos(self, cantidad):
        self.puntos += cantidad
        print("Puntos después de sumar 1:", self.obtener_puntos())

    def restar_puntos(self, cantidad):
        self.puntos -= cantidad
        print("Puntos después de restar 1:", self.obtener_puntos())

    def reiniciar_puntos(self):
        self.puntos = 0
        print("Puntos después de reiniciar:", self.obtener_puntos())

    def obtener_puntos(self):
        return self.puntos

contador = ContadorDePuntos()

while True:
    print("\n1. Sumar puntos")
    print("2. Restar puntos")
    print("3. Reiniciar puntos")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        cantidad = int(input("Ingrese la cantidad de puntos a sumar: "))
        contador.sumar_puntos(cantidad)
    elif opcion == '2':
        cantidad = int(input("Ingrese la cantidad de puntos a restar: "))
        contador.restar_puntos(cantidad)
    elif opcion == '3':
        contador.reiniciar_puntos()
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
