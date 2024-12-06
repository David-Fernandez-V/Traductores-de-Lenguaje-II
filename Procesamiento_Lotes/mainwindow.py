# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(624, 573)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout_2 = QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_ingresarProceso = QGroupBox(self.tab)
        self.groupBox_ingresarProceso.setObjectName(u"groupBox_ingresarProceso")
        self.groupBox_ingresarProceso.setGeometry(QRect(40, 40, 271, 211))
        self.label = QLabel(self.groupBox_ingresarProceso)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 26, 119, 16))
        self.label_2 = QLabel(self.groupBox_ingresarProceso)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 55, 49, 16))
        self.label_3 = QLabel(self.groupBox_ingresarProceso)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 84, 56, 16))
        self.label_4 = QLabel(self.groupBox_ingresarProceso)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 113, 68, 16))
        self.label_5 = QLabel(self.groupBox_ingresarProceso)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 142, 73, 16))
        self.lineEdit_nombreProgramador = QLineEdit(self.groupBox_ingresarProceso)
        self.lineEdit_nombreProgramador.setObjectName(u"lineEdit_nombreProgramador")
        self.lineEdit_nombreProgramador.setGeometry(QRect(135, 26, 122, 20))
        self.pushButton_agregarProceso = QPushButton(self.groupBox_ingresarProceso)
        self.pushButton_agregarProceso.setObjectName(u"pushButton_agregarProceso")
        self.pushButton_agregarProceso.setGeometry(QRect(10, 171, 251, 23))
        self.comboBox_operacion = QComboBox(self.groupBox_ingresarProceso)
        self.comboBox_operacion.addItem("")
        self.comboBox_operacion.addItem("")
        self.comboBox_operacion.addItem("")
        self.comboBox_operacion.addItem("")
        self.comboBox_operacion.addItem("")
        self.comboBox_operacion.addItem("")
        self.comboBox_operacion.setObjectName(u"comboBox_operacion")
        self.comboBox_operacion.setGeometry(QRect(135, 55, 61, 20))
        self.spinBox_primerDato = QSpinBox(self.groupBox_ingresarProceso)
        self.spinBox_primerDato.setObjectName(u"spinBox_primerDato")
        self.spinBox_primerDato.setGeometry(QRect(135, 84, 61, 20))
        self.spinBox_segundoDato = QSpinBox(self.groupBox_ingresarProceso)
        self.spinBox_segundoDato.setObjectName(u"spinBox_segundoDato")
        self.spinBox_segundoDato.setGeometry(QRect(135, 113, 61, 20))
        self.spinBox_Tiempo = QSpinBox(self.groupBox_ingresarProceso)
        self.spinBox_Tiempo.setObjectName(u"spinBox_Tiempo")
        self.spinBox_Tiempo.setGeometry(QRect(135, 142, 61, 20))
        self.spinBox_Tiempo.setMinimum(1)
        self.spinBox_Tiempo.setMaximum(60)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_lotesPendientes = QLineEdit(self.groupBox_2)
        self.lineEdit_lotesPendientes.setObjectName(u"lineEdit_lotesPendientes")
        self.lineEdit_lotesPendientes.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_lotesPendientes, 1, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)

        self.pushButton_iniciar = QPushButton(self.groupBox_2)
        self.pushButton_iniciar.setObjectName(u"pushButton_iniciar")

        self.gridLayout_6.addWidget(self.pushButton_iniciar, 2, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)

        self.lcdNumber = QLCDNumber(self.groupBox_2)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.gridLayout_6.addWidget(self.lcdNumber, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget_procesoEjecucion = QTableWidget(self.groupBox_4)
        if (self.tableWidget_procesoEjecucion.columnCount() < 1):
            self.tableWidget_procesoEjecucion.setColumnCount(1)
        if (self.tableWidget_procesoEjecucion.rowCount() < 6):
            self.tableWidget_procesoEjecucion.setRowCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_procesoEjecucion.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_procesoEjecucion.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_procesoEjecucion.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_procesoEjecucion.setVerticalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_procesoEjecucion.setVerticalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_procesoEjecucion.setVerticalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_procesoEjecucion.setObjectName(u"tableWidget_procesoEjecucion")
        self.tableWidget_procesoEjecucion.setRowCount(6)
        self.tableWidget_procesoEjecucion.setColumnCount(1)

        self.gridLayout_2.addWidget(self.tableWidget_procesoEjecucion, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_4, 0, 1, 2, 1)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_3 = QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget_procesosTerminados = QTableWidget(self.groupBox_5)
        if (self.tableWidget_procesosTerminados.columnCount() < 5):
            self.tableWidget_procesosTerminados.setColumnCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        self.tableWidget_procesosTerminados.setObjectName(u"tableWidget_procesosTerminados")
        self.tableWidget_procesosTerminados.setColumnCount(5)

        self.gridLayout_3.addWidget(self.tableWidget_procesosTerminados, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_5, 2, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_loteEjecucion = QTableWidget(self.groupBox_3)
        if (self.tableWidget_loteEjecucion.columnCount() < 2):
            self.tableWidget_loteEjecucion.setColumnCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_loteEjecucion.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_loteEjecucion.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        self.tableWidget_loteEjecucion.setObjectName(u"tableWidget_loteEjecucion")
        self.tableWidget_loteEjecucion.setRowCount(0)
        self.tableWidget_loteEjecucion.setColumnCount(2)

        self.gridLayout.addWidget(self.tableWidget_loteEjecucion, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 624, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_nombreProgramador, self.comboBox_operacion)
        QWidget.setTabOrder(self.comboBox_operacion, self.spinBox_primerDato)
        QWidget.setTabOrder(self.spinBox_primerDato, self.spinBox_segundoDato)
        QWidget.setTabOrder(self.spinBox_segundoDato, self.spinBox_Tiempo)
        QWidget.setTabOrder(self.spinBox_Tiempo, self.pushButton_agregarProceso)
        QWidget.setTabOrder(self.pushButton_agregarProceso, self.lineEdit_lotesPendientes)
        QWidget.setTabOrder(self.lineEdit_lotesPendientes, self.tableWidget_loteEjecucion)
        QWidget.setTabOrder(self.tableWidget_loteEjecucion, self.tableWidget_procesoEjecucion)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_ingresarProceso.setTitle(QCoreApplication.translate("MainWindow", u"Ingresar Proceso", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre del Programador", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Primer Dato", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Segundo Dato", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tiempo maximo", None))
        self.pushButton_agregarProceso.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.comboBox_operacion.setItemText(0, QCoreApplication.translate("MainWindow", u"+", None))
        self.comboBox_operacion.setItemText(1, QCoreApplication.translate("MainWindow", u"-", None))
        self.comboBox_operacion.setItemText(2, QCoreApplication.translate("MainWindow", u"*", None))
        self.comboBox_operacion.setItemText(3, QCoreApplication.translate("MainWindow", u"/", None))
        self.comboBox_operacion.setItemText(4, QCoreApplication.translate("MainWindow", u"%", None))
        self.comboBox_operacion.setItemText(5, QCoreApplication.translate("MainWindow", u"^", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Lotes Pendientes", None))
        self.pushButton_iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Contador Global", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Proceso en ejecuci\u00f3n", None))
        ___qtablewidgetitem = self.tableWidget_procesoEjecucion.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem1 = self.tableWidget_procesoEjecucion.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget_procesoEjecucion.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem3 = self.tableWidget_procesoEjecucion.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tiempo Estimado", None));
        ___qtablewidgetitem4 = self.tableWidget_procesoEjecucion.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Tiempo Transcurrido", None));
        ___qtablewidgetitem5 = self.tableWidget_procesoEjecucion.verticalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tiempo Restante", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Procesos terminados", None))
        ___qtablewidgetitem6 = self.tableWidget_procesosTerminados.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem7 = self.tableWidget_procesosTerminados.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Primer Dato", None));
        ___qtablewidgetitem8 = self.tableWidget_procesosTerminados.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem9 = self.tableWidget_procesosTerminados.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Segundo Dato", None));
        ___qtablewidgetitem10 = self.tableWidget_procesosTerminados.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Lote en ejecuci\u00f3n", None))
        ___qtablewidgetitem11 = self.tableWidget_loteEjecucion.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem12 = self.tableWidget_loteEjecucion.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Tiempo Estimado", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Procesos", None))
    # retranslateUi

