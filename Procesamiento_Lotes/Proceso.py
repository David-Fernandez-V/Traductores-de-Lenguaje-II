class Proceso:
    def __init__(self, nombre_programador, operacion, dato_operacion_1, dato_operacion_2, tiempo_maximo, numero_programa):
        self.nombre_programador = nombre_programador
        self.operacion = operacion
        self.dato_operacion_1 = dato_operacion_1
        self.dato_operacion_2 = dato_operacion_2
        self.tiempo_maximo = tiempo_maximo
        self.tiempo_restante = tiempo_maximo
        self.tiempo_transcurrido = 0
        self.numero_programa = numero_programa
    
    def validar_operacion(self):
        operaciones_validas = ['+', '-', '*', '/', '%', '^']
        return self.operacion in operaciones_validas

    def validar_tiempo_maximo(self):
        return self.tiempo_maximo > 0
    
    def actualizar_tiempo(self):
        self.tiempo_transcurrido += 1
        self.tiempo_restante -= 1

    def realizar_operacion(self):
        if not self.validar_operacion():
            return None
        
        if self.operacion == '+':
            return self.dato_operacion_1 + self.dato_operacion_2
        elif self.operacion == '-':
            return self.dato_operacion_1 - self.dato_operacion_2
        elif self.operacion == '*':
            return self.dato_operacion_1 * self.dato_operacion_2
        elif self.operacion == '/':
            if self.dato_operacion_2 != 0:
                return self.dato_operacion_1 / self.dato_operacion_2
            else:
                return None
        elif self.operacion == '%':
            if self.dato_operacion_2 != 0:
                return self.dato_operacion_1 % self.dato_operacion_2
            else:
                return None
        elif self.operacion == '^':
            return self.dato_operacion_1 ** self.dato_operacion_2