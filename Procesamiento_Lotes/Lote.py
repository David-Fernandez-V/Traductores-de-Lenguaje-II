import time

class Lote:
    def __init__(self, capacidad_maxima, interfaz):
        self.capacidad_maxima = capacidad_maxima
        self.procesos = []
        self.interfaz = interfaz

    def agregar_proceso(self, proceso):
        if len(self.procesos) < self.capacidad_maxima:
            self.procesos.append(proceso)
            return True
        return False

    def ejecutar_lote(self, simulador):
        for proceso in self.procesos:
            self.interfaz.actualizar_tabla_proceso_en_ejecucion(proceso)
            while proceso.tiempo_restante > 0:
                time.sleep(1)
                proceso.actualizar_tiempo()
                self.interfaz.actualizar_tiempos_proceso(proceso)
                simulador.reloj_global += 1
                self.interfaz.actualizar_reloj()

            simulador.procesos_terminados.append(proceso)
            simulador.numero_lotes_pendientes -= 1
            self.interfaz.actualizar_tabla_procesos_terminados()
            self.interfaz.actualizar_lotes_pendientes(simulador.numero_lotes_pendientes)