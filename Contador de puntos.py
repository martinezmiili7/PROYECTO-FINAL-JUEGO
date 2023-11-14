def crear_contador_de_puntos():
    class ContadorDePuntos:
        def __init__(self):
            self.puntos = 0
            self.ultimas_letras = []  # Lista para guardar las últimas letras ingresadas
            print("Puntos iniciales:", self.obtener_puntos())

        def sumar_puntos(self, cantidad):
            self.puntos += cantidad
            print("Puntos después de sumar:", self.obtener_puntos())

            # Verificar si las últimas tres letras son 'x'
            self.ultimas_letras.append('x')
            if len(self.ultimas_letras) >= 3 and all(letra == 'x' for letra in self.ultimas_letras[-3:]):
                self.puntos += 1
                print("¡Se sumó 1 punto por tener tres 'x' seguidas!")

        def reiniciar_puntos(self):
            self.puntos = 0
            print("Puntos después de reiniciar:", self.obtener_puntos())

        def obtener_puntos(self):
            return self.puntos
    
    return ContadorDePuntos()


