from Lote import Lote

class Simulador:
    def __init__(self, interfaz):
        self.lotes_pendientes = []
        self.procesos_terminados = [] 
        self.reloj_global = 0
        self.total_procesos = 0
        self.numero_lotes_pendientes = 0
        self.capacidad_lote = 4     

        self.interfaz = interfaz

    def agregar_proceso(self, proceso):
        if not self.lotes_pendientes or not self.lotes_pendientes[-1].agregar_proceso(proceso):
            nuevo_lote = Lote(self.capacidad_lote,self.interfaz)
            nuevo_lote.agregar_proceso(proceso)
            self.lotes_pendientes.append(nuevo_lote)
        self.total_procesos += 1
        self.numero_lotes_pendientes += 1
 
    def ejecutar_lotes(self):
        while self.lotes_pendientes:
            lote_en_ejecucion = self.lotes_pendientes.pop(0)
            self.interfaz.actualizar_tabla_lote_en_ejecucion(lote_en_ejecucion)
            lote_en_ejecucion.ejecutar_lote(self)
            self.interfaz.actualizar_lotes_pendientes(self.numero_lotes_pendientes)