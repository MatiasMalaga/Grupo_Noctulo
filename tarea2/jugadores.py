


class jugador:

    def __init__(self, nombre, edad, altura, dorsal):

        self.nombre=nombre
        self.edad=edad
        self.altura=altura
        self.dorsal=dorsal

        def correr(self):
            print(self.nombre+" esta corriendo")
            return self.nombre+" esta corriendo"

        def mostral_rol(self):
            return "soy un jugador de futbol profesional"
        
        def celebrar(self):
            return "el jugardor celebra la anotacion"
        
        def fingir_lesion(self):
            return "el jugar finge una lesion para gastar tiempo" # XD


# portero
class portero(jugador):

    def __init__(self, nombre, edad, altura, dorsal, atajadas, reflejos):
        
        super().__init__(nombre, edad, altura, dorsal)

        # atributos propios
        self.atajadas=atajadas
        self.reflejos=reflejos
        
    def correr(self):
        print(self.nombre+" esta corriendo")
        return self.nombre+" esta corriendo"

    # metodos propios

    def atajar(self):
        print(self.nombre +" realizo una atajada.")
        return self.nombre +" realizo una atajada."

    def organiza_la_defensa(self):
        print(self.nombre+" alerta y organiza a la defensa.")
        return self.nombre+" alerta y organiza a la defensa."

    # sobrescritura
    def mostrar_rol(self):
        print(self.nombre+" juega como portero.")
        return self.nombre+" juega como portero."



# defensa
class defensa(jugador):

    def __init__(self, nombre, edad, altura, dorsal, robos_de_balon, entradas):
        
        super().__init__(nombre, edad, altura, dorsal)

        # atributos propios
        self.balones_recuperados=robos_de_balon
        self.entradas=entradas

    def correr(self):
        print(self.nombre+" esta corriendo")
        return self.nombre+" esta corriendo"
    
    # metodos propios
    def marcar(self):
        print(self.nombre+" está marcando al rival.")
        return self.nombre+" está marcando al rival."

    def interceptar(self):
        print(self.nombre+" interceptó un pase del rival.")
        return self.nombre+" interceptó un pase del rival."

    # sobrescritura
    def mostrar_rol(self):
        print(self.nombre+" juega como defensa.")
        return self.nombre+" juega como defensa."


# medio campista
class mediocampista(jugador):

    def __init__(self, nombre, edad, altura, dorsal, asistencias, pases_exitosos):
        
        super().__init__(nombre, edad, altura, dorsal)

        # atributos propios
        self.asistencias=asistencias
        self.precision_pase=pases_exitosos

    def correr(self):
        print(self.nombre+" esta corriendo")
        return self.nombre+" esta corriendo"
    
    # metodos propios
    def dar_pase(self):
        print(self.nombre+" dio un pase.")
        return self.nombre+" dio un pase."

    def organizar_juego(self):
        print(self.nombre+" organizo el ataque.")
        return self.nombre+" organizo el ataque."

    # sobrescritura
    def mostrar_rol(self):
        print(self.nombre+" juega como mediocampista.")
        return self.nombre+" juega como mediocampista."



# delantero
class delantero(jugador):

    def __init__(self, nombre, edad, altura, dorsal, goles, velocidad):
        
        super().__init__(nombre, edad, altura, dorsal)

        # atributos propios
        self.goles=goles
        self.velocidad=velocidad
        
    def correr(self):
        print(self.nombre+" esta corriendo")
        return self.nombre+" esta corriendo"
    
    # metodos propios
    def patear_al_arco(self):
        print(self.nombre+" pateó al arco.")
        return self.nombre+" pateó al arco."
    def celebrar_gol(self):
        print(self.nombre+" celebró el gol.")
        return self.nombre+" celebró el gol."

    # sobrescritura
    def mostrar_rol(self):
        print(self.nombre+" juega como delantero.")
        return self.nombre+" juega como delantero."










