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
        MainWindow.resize(638, 637)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_ingresarProcesos = QGroupBox(self.tab)
        self.groupBox_ingresarProcesos.setObjectName(u"groupBox_ingresarProcesos")
        self.formLayout = QFormLayout(self.groupBox_ingresarProcesos)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_ingresarProcesos)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.spinBox_numeroProcesos = QSpinBox(self.groupBox_ingresarProcesos)
        self.spinBox_numeroProcesos.setObjectName(u"spinBox_numeroProcesos")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox_numeroProcesos)

        self.pushButton_agregarProcesos = QPushButton(self.groupBox_ingresarProcesos)
        self.pushButton_agregarProcesos.setObjectName(u"pushButton_agregarProcesos")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.pushButton_agregarProcesos)


        self.gridLayout_5.addWidget(self.groupBox_ingresarProcesos, 0, 0, 1, 1)

        self.groupBox_listaProcesos = QGroupBox(self.tab)
        self.groupBox_listaProcesos.setObjectName(u"groupBox_listaProcesos")
        self.horizontalLayout = QHBoxLayout(self.groupBox_listaProcesos)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plainTextEdit_listaProcesos = QPlainTextEdit(self.groupBox_listaProcesos)
        self.plainTextEdit_listaProcesos.setObjectName(u"plainTextEdit_listaProcesos")

        self.horizontalLayout.addWidget(self.plainTextEdit_listaProcesos)


        self.gridLayout_5.addWidget(self.groupBox_listaProcesos, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 331, 121))
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)

        self.pushButton_iniciar = QPushButton(self.groupBox_2)
        self.pushButton_iniciar.setObjectName(u"pushButton_iniciar")

        self.gridLayout_6.addWidget(self.pushButton_iniciar, 2, 0, 1, 2)

        self.lcdNumber = QLCDNumber(self.groupBox_2)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.gridLayout_6.addWidget(self.lcdNumber, 0, 1, 1, 1)

        self.lineEdit_procesosNuevos = QLineEdit(self.groupBox_2)
        self.lineEdit_procesosNuevos.setObjectName(u"lineEdit_procesosNuevos")
        self.lineEdit_procesosNuevos.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_procesosNuevos, 1, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(350, 180, 251, 211))
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget_procesoEjecucion = QTableWidget(self.groupBox_4)
        if (self.tableWidget_procesoEjecucion.columnCount() < 1):
            self.tableWidget_procesoEjecucion.setColumnCount(1)
        if (self.tableWidget_procesoEjecucion.rowCount() < 5):
            self.tableWidget_procesoEjecucion.setRowCount(5)
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
        self.tableWidget_procesoEjecucion.setObjectName(u"tableWidget_procesoEjecucion")
        self.tableWidget_procesoEjecucion.setEnabled(True)
        self.tableWidget_procesoEjecucion.setRowCount(5)
        self.tableWidget_procesoEjecucion.setColumnCount(1)

        self.gridLayout_2.addWidget(self.tableWidget_procesoEjecucion, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 130, 331, 261))
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_procesosListos = QTableWidget(self.groupBox_3)
        if (self.tableWidget_procesosListos.columnCount() < 3):
            self.tableWidget_procesosListos.setColumnCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_procesosListos.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_procesosListos.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_procesosListos.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        self.tableWidget_procesosListos.setObjectName(u"tableWidget_procesosListos")
        self.tableWidget_procesosListos.setEnabled(True)
        self.tableWidget_procesosListos.setRowCount(0)
        self.tableWidget_procesosListos.setColumnCount(3)

        self.gridLayout.addWidget(self.tableWidget_procesosListos, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 393, 601, 161))
        self.gridLayout_3 = QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget_procesosTerminados = QTableWidget(self.groupBox_5)
        if (self.tableWidget_procesosTerminados.columnCount() < 5):
            self.tableWidget_procesosTerminados.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.tableWidget_procesosTerminados.setObjectName(u"tableWidget_procesosTerminados")
        self.tableWidget_procesosTerminados.setEnabled(True)
        self.tableWidget_procesosTerminados.setColumnCount(5)

        self.gridLayout_3.addWidget(self.tableWidget_procesosTerminados, 0, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(350, 10, 251, 171))
        self.gridLayout_4 = QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget_procesosBloqueados = QTableWidget(self.groupBox_6)
        if (self.tableWidget_procesosBloqueados.columnCount() < 2):
            self.tableWidget_procesosBloqueados.setColumnCount(2)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_procesosBloqueados.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_procesosBloqueados.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        self.tableWidget_procesosBloqueados.setObjectName(u"tableWidget_procesosBloqueados")
        self.tableWidget_procesosBloqueados.setEnabled(True)
        self.tableWidget_procesosBloqueados.setRowCount(0)
        self.tableWidget_procesosBloqueados.setColumnCount(2)

        self.gridLayout_4.addWidget(self.tableWidget_procesosBloqueados, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.formLayout_2 = QFormLayout(self.tab_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.tableWidget_bcp = QTableWidget(self.tab_4)
        if (self.tableWidget_bcp.rowCount() < 13):
            self.tableWidget_bcp.setRowCount(13)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(9, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(10, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(11, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_bcp.setVerticalHeaderItem(12, __qtablewidgetitem27)
        self.tableWidget_bcp.setObjectName(u"tableWidget_bcp")
        self.tableWidget_bcp.setEnabled(False)
        self.tableWidget_bcp.setColumnCount(0)

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.tableWidget_bcp)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_8 = QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tableWidget_resultados = QTableWidget(self.tab_3)
        if (self.tableWidget_resultados.rowCount() < 12):
            self.tableWidget_resultados.setRowCount(12)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(8, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(9, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(10, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_resultados.setVerticalHeaderItem(11, __qtablewidgetitem39)
        self.tableWidget_resultados.setObjectName(u"tableWidget_resultados")
        self.tableWidget_resultados.setEnabled(True)
        self.tableWidget_resultados.setDragEnabled(False)
        self.tableWidget_resultados.setAlternatingRowColors(False)
        self.tableWidget_resultados.setColumnCount(0)

        self.gridLayout_8.addWidget(self.tableWidget_resultados, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_7.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 638, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButton_agregarProcesos, self.lineEdit_procesosNuevos)
        QWidget.setTabOrder(self.lineEdit_procesosNuevos, self.tableWidget_procesosListos)
        QWidget.setTabOrder(self.tableWidget_procesosListos, self.tableWidget_procesoEjecucion)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_ingresarProcesos.setTitle(QCoreApplication.translate("MainWindow", u"Ingresar Procesos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Numero de Procesos", None))
        self.pushButton_agregarProcesos.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.groupBox_listaProcesos.setTitle(QCoreApplication.translate("MainWindow", u"Lista de Procesos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tiempo Global", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Procesos Nuevos", None))
        self.pushButton_iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Proceso en ejecuci\u00f3n", None))
        ___qtablewidgetitem = self.tableWidget_procesoEjecucion.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem1 = self.tableWidget_procesoEjecucion.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem2 = self.tableWidget_procesoEjecucion.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tiempo Estimado", None));
        ___qtablewidgetitem3 = self.tableWidget_procesoEjecucion.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tiempo Transcurrido", None));
        ___qtablewidgetitem4 = self.tableWidget_procesoEjecucion.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Tiempo Restante", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Procesos Listos", None))
        ___qtablewidgetitem5 = self.tableWidget_procesosListos.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem6 = self.tableWidget_procesosListos.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tiempo Estimado", None));
        ___qtablewidgetitem7 = self.tableWidget_procesosListos.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Tiempo Restante", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Procesos terminados", None))
        ___qtablewidgetitem8 = self.tableWidget_procesosTerminados.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem9 = self.tableWidget_procesosTerminados.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Primer Dato", None));
        ___qtablewidgetitem10 = self.tableWidget_procesosTerminados.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem11 = self.tableWidget_procesosTerminados.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Segundo Dato", None));
        ___qtablewidgetitem12 = self.tableWidget_procesosTerminados.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Procesos Bloqueados", None))
        ___qtablewidgetitem13 = self.tableWidget_procesosBloqueados.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem14 = self.tableWidget_procesosBloqueados.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"T. Bloqueado", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Procesos", None))
        ___qtablewidgetitem15 = self.tableWidget_bcp.verticalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem16 = self.tableWidget_bcp.verticalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem17 = self.tableWidget_bcp.verticalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Primer Dato", None));
        ___qtablewidgetitem18 = self.tableWidget_bcp.verticalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem19 = self.tableWidget_bcp.verticalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Segundo Dato", None));
        ___qtablewidgetitem20 = self.tableWidget_bcp.verticalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        ___qtablewidgetitem21 = self.tableWidget_bcp.verticalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"T. Llegada", None));
        ___qtablewidgetitem22 = self.tableWidget_bcp.verticalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"T. Finalizaci\u00f3n", None));
        ___qtablewidgetitem23 = self.tableWidget_bcp.verticalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"T. Retorno", None));
        ___qtablewidgetitem24 = self.tableWidget_bcp.verticalHeaderItem(9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"T. Espera", None));
        ___qtablewidgetitem25 = self.tableWidget_bcp.verticalHeaderItem(10)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"T. Servicio", None));
        ___qtablewidgetitem26 = self.tableWidget_bcp.verticalHeaderItem(11)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"T. Restante", None));
        ___qtablewidgetitem27 = self.tableWidget_bcp.verticalHeaderItem(12)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"T. Respuesta", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"BCP", None))
        ___qtablewidgetitem28 = self.tableWidget_resultados.verticalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem29 = self.tableWidget_resultados.verticalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Primer Dato", None));
        ___qtablewidgetitem30 = self.tableWidget_resultados.verticalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem31 = self.tableWidget_resultados.verticalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Segundo Dato", None));
        ___qtablewidgetitem32 = self.tableWidget_resultados.verticalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        ___qtablewidgetitem33 = self.tableWidget_resultados.verticalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"T. M\u00e1ximo", None));
        ___qtablewidgetitem34 = self.tableWidget_resultados.verticalHeaderItem(6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"T. Llegada", None));
        ___qtablewidgetitem35 = self.tableWidget_resultados.verticalHeaderItem(7)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"T. Finalizaci\u00f3n", None));
        ___qtablewidgetitem36 = self.tableWidget_resultados.verticalHeaderItem(8)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"T. Retorno", None));
        ___qtablewidgetitem37 = self.tableWidget_resultados.verticalHeaderItem(9)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"T. Respuesta", None));
        ___qtablewidgetitem38 = self.tableWidget_resultados.verticalHeaderItem(10)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"T. Espera", None));
        ___qtablewidgetitem39 = self.tableWidget_resultados.verticalHeaderItem(11)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"T. Servicio", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Resultados", None))
    # retranslateUi

