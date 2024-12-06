from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem
from PySide2.QtCore import Slot
from mainwindow import Ui_MainWindow
from PySide2.QtCore import QThread
from PySide2.QtCore import Signal

from Proceso import Proceso
from Simulador import Simulador

class SimulacionThread(QThread):
    finalizada = Signal()

    def __init__(self, simulador):
        super().__init__()
        self.simulador = simulador

    def run(self):
        self.simulador.ejecutar_lotes()
        self.finalizada.emit()

class Interfaz(QMainWindow):
    def __init__(self):
        super(Interfaz, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.simulador = Simulador(self)

        self.simulacion_thread = None
        self.ui.pushButton_iniciar.clicked.connect(self.iniciar)

        self.ui.pushButton_agregarProceso.clicked.connect(self.agregar_proceso)
        self.ui.pushButton_iniciar.clicked.connect(self.iniciar)

    def crear_proceso(self):
        nombre_programador = self.ui.lineEdit_nombreProgramador.text()
        operacion = self.ui.comboBox_operacion.currentText()
        dato_operacion_1 = self.ui.spinBox_primerDato.value()
        dato_operacion_2 = self.ui.spinBox_segundoDato.value()
        tiempo_estimado = self.ui.spinBox_Tiempo.value()
        if tiempo_estimado <= 0:
            tiempo_estimado = 1
        
        proceso = Proceso(nombre_programador, operacion, dato_operacion_1, dato_operacion_2, tiempo_estimado, self.simulador.total_procesos+1)
        return proceso

    def limpiar_entradas_datos(self):
        self.ui.lineEdit_nombreProgramador.clear()
        self.ui.spinBox_primerDato.clear()
        self.ui.spinBox_segundoDato.clear()
        self.ui.spinBox_Tiempo.clear()

    def actualizar_tabla_lote_en_ejecucion(self, lote):
        self.ui.tableWidget_loteEjecucion.setRowCount(len(lote.procesos))

        for row, proceso in enumerate(lote.procesos):
            numero_programa_item = QTableWidgetItem(str(proceso.numero_programa))
            tiempo_estimado_item = QTableWidgetItem(str(proceso.tiempo_maximo))

            self.ui.tableWidget_loteEjecucion.setItem(row, 0, numero_programa_item)
            self.ui.tableWidget_loteEjecucion.setItem(row, 1, tiempo_estimado_item)

    def actualizar_tabla_proceso_en_ejecucion(self, proceso):
        numero_programa_item = QTableWidgetItem(str(proceso.numero_programa))
        nombre_programador_item = QTableWidgetItem(proceso.nombre_programador)
        operacion_item = QTableWidgetItem(proceso.operacion)
        tiempo_estimado_item = QTableWidgetItem(str(proceso.tiempo_maximo))
        tiempo_transcurrido_item = QTableWidgetItem(str(proceso.tiempo_transcurrido))
        tiempo_restante_item = QTableWidgetItem(str(proceso.tiempo_restante))

        self.ui.tableWidget_procesoEjecucion.setItem(0, 0, numero_programa_item)
        self.ui.tableWidget_procesoEjecucion.setItem(1, 0, nombre_programador_item)
        self.ui.tableWidget_procesoEjecucion.setItem(2, 0, operacion_item)
        self.ui.tableWidget_procesoEjecucion.setItem(3, 0, tiempo_estimado_item)
        self.ui.tableWidget_procesoEjecucion.setItem(4, 0, tiempo_transcurrido_item)
        self.ui.tableWidget_procesoEjecucion.setItem(5, 0, tiempo_restante_item)


    def actualizar_tabla_procesos_terminados(self):
        self.ui.tableWidget_procesosTerminados.setRowCount(len(self.simulador.procesos_terminados))

        for row, proceso in enumerate(self.simulador.procesos_terminados):
            numero_programa_item = QTableWidgetItem(str(proceso.numero_programa))
            dato_operacion_1_item = QTableWidgetItem(str(proceso.dato_operacion_1))
            operacion_item = QTableWidgetItem(proceso.operacion)
            dato_operacion_2_item = QTableWidgetItem(str(proceso.dato_operacion_2))
            resultado_item = QTableWidgetItem(str(proceso.realizar_operacion()))

            self.ui.tableWidget_procesosTerminados.setItem(row, 0, numero_programa_item)
            self.ui.tableWidget_procesosTerminados.setItem(row, 1, dato_operacion_1_item)
            self.ui.tableWidget_procesosTerminados.setItem(row, 2, operacion_item)
            self.ui.tableWidget_procesosTerminados.setItem(row, 3, dato_operacion_2_item)
            self.ui.tableWidget_procesosTerminados.setItem(row, 4, resultado_item)

    def actualizar_lotes_pendientes(self, numero_lotes_pendientes):
        self.ui.lineEdit_lotesPendientes.setText(str(numero_lotes_pendientes))

    def actualizar_reloj(self):
        segundos = self.simulador.reloj_global
        minutos = segundos // 60
        segundos = segundos % 60
        self.ui.lcdNumber.display(f"{minutos:02d}:{segundos:02d}")

    def actualizar_tiempos_proceso(self, proceso):
        tiempo_transcurrido_item = QTableWidgetItem(str(proceso.tiempo_transcurrido))
        tiempo_restante_item = QTableWidgetItem(str(proceso.tiempo_restante))

        self.ui.tableWidget_procesoEjecucion.setItem(4, 0, tiempo_transcurrido_item)
        self.ui.tableWidget_procesoEjecucion.setItem(5, 0, tiempo_restante_item)
        

    def simulacion_finalizada(self):
        QMessageBox.information(self, "Simulación Terminada", "La simulación ha terminado.")

    @Slot()
    def agregar_proceso(self):
        self.simulador.agregar_proceso(self.crear_proceso())
        self.limpiar_entradas_datos()
        self.actualizar_lotes_pendientes(self.simulador.numero_lotes_pendientes)
        
    @Slot()
    def iniciar(self):
        if not self.simulacion_thread or not self.simulacion_thread.isRunning():
            self.simulacion_thread = SimulacionThread(self.simulador)
            self.simulacion_thread.finalizada.connect(self.simulacion_finalizada)
            self.simulacion_thread.start()