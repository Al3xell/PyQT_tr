#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys,json
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QT_VERSION_STR

from scene import Scene

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.resize(500, 300)
        self.setWindowTitle("Editeur v0.1")
        self.create_scene()
        self.create_actions()
        self.create_menus()
        self.connect_actions()
        
    def create_scene(self) :
        view=QtWidgets.QGraphicsView()
        self.scene=Scene(self)
        text= self.scene.addText("Hello World !")
    #    text.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        text.setPos(100,200)
    #    text.setVisible(True)
        view.setScene(self.scene)              # MVD
        self.setCentralWidget(view)

    def create_actions(self) :
        self.action_save = QtWidgets.QAction(QtGui.QIcon('icons/save.png'), 'Save', self)
        self.action_save.setShortcut('Ctrl+S')
        self.action_save.setStatusTip('Save to file')

        self.action_open = QtWidgets.QAction(QtGui.QIcon('icons/open.png'), 'Open', self)
        self.action_open.setShortcut('Ctrl+O')
        self.action_open.setStatusTip('Open file')

        self.action_exit = QtWidgets.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        self.action_exit.setShortcut('Ctrl+Q')
        self.action_exit.setStatusTip('Exit application')

        self.group_action_tools = QtWidgets.QActionGroup(self)
        self.action_line = QtWidgets.QAction(self.tr("&Line"), self)
        self.action_line.setCheckable(True)
        self.action_rect = QtWidgets.QAction(self.tr("&Rect"), self)
        self.action_rect.setCheckable(True)
        self.action_poly = QtWidgets.QAction(self.tr("&Poly"), self)
        self.action_poly.setCheckable(True)
        # self.action_line.setChecked(True)
        self.group_action_tools.addAction(self.action_line)
        self.group_action_tools.addAction(self.action_rect)
        self.group_action_tools.addAction(self.action_poly)

        self.action_pen_color = QtWidgets.QAction(self.tr("Color"), self)
        self.action_pen_width = QtWidgets.QAction(self.tr("Width"), self)
        self.action_brush_color = QtWidgets.QAction(self.tr("Color"), self)

    def create_menus(self) :
 #       statusbar=self.statusBar()
        menubar = self.menuBar()
        menu_file = menubar.addMenu('&File')
        menu_file.addAction(self.action_open)
        menu_file.addAction(self.action_save)
        menu_file.addAction(self.action_exit)

        menu_tools = menubar.addMenu('&Tools')
        menu_tools.addAction(self.action_line)
        menu_tools.addAction(self.action_rect)
        menu_tools.addAction(self.action_poly)

        menu_style=menubar.addMenu('&Style')
        menu_style_pen=menu_style.addMenu('Pen')
        menu_style_pen.addAction(self.action_pen_color)
        menu_style_pen.addAction(self.action_pen_width)
        menu_style_brush=menu_style.addMenu('Brush')
        menu_style_brush.addAction(self.action_brush_color)

        menu_help=self.menuBar().addMenu(self.tr("&Help"))

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(self.action_exit)

        self.action_about = menu_help.addAction(self.tr("& About this Editor"))

    def connect_actions(self) :
        self.action_open.triggered.connect(self.file_open)
        self.action_save.triggered.connect(self.file_save)
        self.action_exit.triggered.connect(self.file_exit)
        self.action_about.triggered.connect(self.help_about)
        self.action_pen_color.triggered.connect(self.pen_color_selection)
        self.action_pen_width.triggered.connect(self.pen_width_selection)
        self.action_brush_color.triggered.connect(self.brush_color_selection)
        self.action_line.triggered.connect(lambda checked, tool="line": self.set_action_tool(checked,tool))
        self.action_rect.triggered.connect(lambda checked, tool="rect": self.set_action_tool(checked,tool))
        self.action_poly.triggered.connect(lambda checked, tool="poly": self.set_action_tool(checked,tool))

    def set_action_tool(self,checked, tool) :
        print("lamda checked, tool : ",checked, tool)
        self.scene.set_tool(tool)
        
    
    def file_exit(self):
        answer = QtWidgets.QMessageBox.question(self, self.tr("Exit ?"),
                                self.tr("Are you sure ?"), QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
        if answer == QtWidgets.QMessageBox.Yes:
            exit(0)
        return

    def data_to_items(self, data):
        self.scene.clear()
        print("data open")
        for d_item in data :
            print("d_item",d_item)
            t = d_item["type"]
            if t == "line":
                x1, y1, x2, y2 = d_item["x1"], d_item["y1"], d_item["x2"], d_item["y2"]
                pen = QtGui.QPen()
                pen.setWidth(d_item["width"])
                color = QtGui.QColor()
                color.setRgb(d_item["color"])
                pen.setColor(color)
                self.scene.addLine(x1, y1, x2, y2, pen)
            elif t == "rect":
                x, y, width, height = d_item["x"], d_item["y"], d_item["width"], d_item["height"]
                pen = QtGui.QPen()
                brush = QtGui.QBrush()
                pen.setWidth(d_item["width_pen"])
                color_pen = QtGui.QColor()
                color_brush = QtGui.QColor()
                color_pen.setRgb(d_item["color_pen"])
                color_brush.setRgb(d_item["color_brush"])
                pen.setColor(color_pen)
                brush.setColor(color_brush)
                brush.setStyle(1)
                self.scene.addRect(x, y, width, height, pen, brush)
                
   
    def file_open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', os.getcwd(), "Json FILES (*.json)")
        fileopen=QtCore.QFile(filename[0])
        file_to_load = open(filename[0],"r")
        self.data_to_items(json.load(file_to_load))
        file_to_load.close()
        print(filename[0] + " opened !")

    def file_save(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', f"{os.getcwd()}/unknown.json", "Json FILES (*.json)")
        filesave=QtCore.QFile(filename[0])
        filename=filename[0].split("/")
        self.scene.name=filename[-1]
        if filesave.open(QtCore.QIODevice.WriteOnly)==None :
            print("echec de sauvegarde du fichier : "+self.scene.name)
            return -1
        else :
            data=self.items_to_data()
            print(data)
            filesave.write(json.dumps(data).encode("utf-8"))
            filesave.close()
            print("sauvegarde du fichier : "+self.scene.name+" avec success")
            

    def items_to_data(self):
        # liste de dictionnaires d'items à sauvegarder
        to_save=[] 
        for item in self.scene.items():
            if isinstance(item, QtWidgets.QGraphicsLineItem):
                # création d'un dictionnaire pour chaque item
                data = {} 
                data["type"] = "line"
                data["x1"] = item.line().x1()
                data["y1"] = item.line().y1()
                data["x2"] = item.line().x2()
                data["y2"] = item.line().y2()
                data["color"] = item.pen().color().rgb()
                data["width"] = item.pen().width()
                # ajout du dictionnaire dans la liste des dictionnaires d'items
                to_save.append(data) 
            # a completer pour chaque item
            elif  isinstance(item, QtWidgets.QGraphicsRectItem): 
                data = {} 
                data["type"] = "rect"
                data["x"] = item.rect().x()
                data["y"] = item.rect().y()
                data["width"] = item.rect().width()
                data["height"] = item.rect().height()
                data["color_pen"] = item.pen().color().rgb()
                data["width_pen"] = item.pen().width()
                data["color_brush"] = item.brush().color().rgb()
                # ajout du dictionnaire dans la liste des dictionnaires d'items
                to_save.append(data) 
            else :
                pass
        return to_save

    def pen_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow, self )
        if color.isValid() :
            print("choosen color : ",color.name())
            self.scene.set_pen_color(color)
        else :
            print("color is not a valid one !")
            
    def pen_width_selection(self):
        width = QtWidgets.QInputDialog.getInt(self, "Pen Width", "Enter Value :")
        if width[0] :
            print("Width choosen : ", width)
            self.scene.pen.setWidth(width[0])
        else :
            print("Width is not valid !")

    def brush_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow, self )
        if color.isValid() :
            print("choosen color : ",color.name())
            self.scene.set_brush_color(color)
        else :
            print("color is not a valid one !")
        
    def help_about(self):
        QtWidgets.QMessageBox.information(self, self.tr("About Me"),
                                self.tr("Guillaume/Choucq\ncopyright ENIB 2022P"))
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
    
    
if __name__ == "__main__" :  
    print(QT_VERSION_STR)
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
