# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glimpse-project/glimpse/glab/ui/glab_main.ui'
#
# Created: Fri Nov  9 23:09:59 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 368)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExperiment = QtGui.QMenu(self.menubar)
        self.menuExperiment.setObjectName("menuExperiment")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_2.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exp_list = QtGui.QListWidget(self.dockWidgetContents_2)
        self.exp_list.setObjectName("exp_list")
        self.horizontalLayout.addWidget(self.exp_list)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
        self.add_action = QtGui.QAction(MainWindow)
        self.add_action.setObjectName("add_action")
        self.save_action = QtGui.QAction(MainWindow)
        self.save_action.setObjectName("save_action")
        self.export_action = QtGui.QAction(MainWindow)
        self.export_action.setObjectName("export_action")
        self.run_action = QtGui.QAction(MainWindow)
        self.run_action.setObjectName("run_action")
        self.del_action = QtGui.QAction(MainWindow)
        self.del_action.setObjectName("del_action")
        self.exit_action = QtGui.QAction(MainWindow)
        self.exit_action.setObjectName("exit_action")
        self.edit_action = QtGui.QAction(MainWindow)
        self.edit_action.setObjectName("edit_action")
        self.menuFile.addAction(self.export_action)
        self.menuFile.addAction(self.save_action)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit_action)
        self.menuExperiment.addAction(self.add_action)
        self.menuExperiment.addAction(self.run_action)
        self.menuExperiment.addAction(self.del_action)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExperiment.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.exit_action, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Glimpse Laboratory", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExperiment.setTitle(QtGui.QApplication.translate("MainWindow", "&Experiment", None, QtGui.QApplication.UnicodeUTF8))
        self.add_action.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.add_action.setToolTip(QtGui.QApplication.translate("MainWindow", "Create a new experiment", None, QtGui.QApplication.UnicodeUTF8))
        self.save_action.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.save_action.setToolTip(QtGui.QApplication.translate("MainWindow", "Save the current experiment", None, QtGui.QApplication.UnicodeUTF8))
        self.export_action.setText(QtGui.QApplication.translate("MainWindow", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.export_action.setToolTip(QtGui.QApplication.translate("MainWindow", "Export features to a CSV file", None, QtGui.QApplication.UnicodeUTF8))
        self.run_action.setText(QtGui.QApplication.translate("MainWindow", "&Run", None, QtGui.QApplication.UnicodeUTF8))
        self.run_action.setToolTip(QtGui.QApplication.translate("MainWindow", "Run the current experiment", None, QtGui.QApplication.UnicodeUTF8))
        self.del_action.setText(QtGui.QApplication.translate("MainWindow", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.del_action.setToolTip(QtGui.QApplication.translate("MainWindow", "Delete the current experiment", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_action.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_action.setToolTip(QtGui.QApplication.translate("MainWindow", "Quit the program", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_action.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_action.setText(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))

