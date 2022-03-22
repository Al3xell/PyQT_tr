#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys,json, webbrowser
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
        
        self.action_new = QtWidgets.QAction(QtGui.QIcon('icons/new.png'), 'New', self)
        self.action_new.setShortcut('Ctrl+N')
        self.action_new.setStatusTip('New File')
        
        self.action_save = QtWidgets.QAction(QtGui.QIcon('icons/save.png'), 'Save', self)
        self.action_save.setShortcut('Ctrl+S')
        self.action_save.setStatusTip('Save to file')
        
        self.action_save_as = QtWidgets.QAction(QtGui.QIcon('icons/save.png'), 'Save As', self)
        self.action_save_as.setStatusTip('Save to file as filename')

        self.action_open = QtWidgets.QAction(QtGui.QIcon('icons/open.png'), 'Open', self)
        self.action_open.setShortcut('Ctrl+O')
        self.action_open.setStatusTip('Open file')
        
        self.action_undo = QtWidgets.QAction(QtGui.QIcon('icons/undo.png'), 'Undo', self)
        self.action_undo.setShortcut('Ctrl+Z')
        self.action_undo.setStatusTip('Undo')
        
        self.action_redo = QtWidgets.QAction(QtGui.QIcon('icons/redo.png'), 'Redo', self)
        self.action_redo.setShortcut('Ctrl+Y')
        self.action_redo.setStatusTip('Redo')

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
        self.action_eli = QtWidgets.QAction(self.tr("&Ellipse"), self)
        self.action_eli.setCheckable(True)
        self.action_txt = QtWidgets.QAction(self.tr("&Text"), self)
        self.action_txt.setCheckable(True)
        
        self.group_action_tools.addAction(self.action_line)
        self.group_action_tools.addAction(self.action_rect)
        self.group_action_tools.addAction(self.action_poly)
        self.group_action_tools.addAction(self.action_eli)
        self.group_action_tools.addAction(self.action_txt)
        
        

        self.action_pen_color = QtWidgets.QAction(self.tr("Color"), self)
        self.action_pen_width = QtWidgets.QAction(self.tr("Width"), self)
        self.group_action_pen = QtWidgets.QActionGroup(self)
        
        self.action_solid = QtWidgets.QAction(self.tr("&Solid Line"), self)
        self.action_solid.setCheckable(True)
        self.action_dash = QtWidgets.QAction(self.tr("&Dash Line"), self)
        self.action_dash.setCheckable(True)
        self.action_dot = QtWidgets.QAction(self.tr("&Dot Line"), self)
        self.action_dot.setCheckable(True)
        self.action_dashdot = QtWidgets.QAction(self.tr("&Dash Dot Line"), self)
        self.action_dashdot.setCheckable(True)
        self.action_dashdotdot = QtWidgets.QAction(self.tr("&Dash Dot Dot Line"), self)
        self.action_dashdotdot.setCheckable(True)
        self.action_nopen = QtWidgets.QAction(self.tr("&No Pen Line"), self)
        self.action_nopen.setCheckable(True)
        
        self.group_action_pen.addAction(self.action_solid)
        self.group_action_pen.addAction(self.action_dash)
        self.group_action_pen.addAction(self.action_dot)
        self.group_action_pen.addAction(self.action_dashdot)
        self.group_action_pen.addAction(self.action_dashdotdot)
        self.group_action_pen.addAction(self.action_nopen)
        
        
        self.action_brush_color = QtWidgets.QAction(self.tr("Color"), self)
        self.group_action_brush = QtWidgets.QActionGroup(self)
        
        self.action_solidb = QtWidgets.QAction(self.tr("&Solid Pattern"), self)
        self.action_solidb.setCheckable(True)
        self.action_dense1 = QtWidgets.QAction(self.tr("&Dense 1 Pattern"), self)
        self.action_dense1.setCheckable(True)
        self.action_dense2 = QtWidgets.QAction(self.tr("&Dense 2 Pattern"), self)
        self.action_dense2.setCheckable(True)
        self.action_dense3 = QtWidgets.QAction(self.tr("&Dense 3 Pattern"), self)
        self.action_dense3.setCheckable(True)
        self.action_dense4 = QtWidgets.QAction(self.tr("&Dense 4 Pattern"), self)
        self.action_dense4.setCheckable(True)
        self.action_dense5 = QtWidgets.QAction(self.tr("&Dense 5 Pattern"), self)
        self.action_dense5.setCheckable(True)
        self.action_dense6 = QtWidgets.QAction(self.tr("&Dense 6 Pattern"), self)
        self.action_dense6.setCheckable(True)
        self.action_dense7 = QtWidgets.QAction(self.tr("&Dense 7 Pattern"), self)
        self.action_dense7.setCheckable(True)
        self.action_hor = QtWidgets.QAction(self.tr("&Horizontal Pattern"), self)
        self.action_hor.setCheckable(True)
        self.action_ver = QtWidgets.QAction(self.tr("&Vertical Pattern"), self)
        self.action_ver.setCheckable(True)
        self.action_cross = QtWidgets.QAction(self.tr("&Simple Crossing Pattern"), self)
        self.action_cross.setCheckable(True)
        self.action_bdiag = QtWidgets.QAction(self.tr("&Backward Diagonale Pattern"), self)
        self.action_bdiag.setCheckable(True)
        self.action_fdiag = QtWidgets.QAction(self.tr("&Forward Diagonale Pattern"), self)
        self.action_fdiag.setCheckable(True)
        self.action_diagcross = QtWidgets.QAction(self.tr("&Diagonale Crossing Pattern"), self)
        self.action_diagcross.setCheckable(True)
        self.action_nobrush = QtWidgets.QAction(self.tr("&No Brush"), self)
        self.action_nobrush.setCheckable(True)
        
        self.group_action_brush.addAction(self.action_solidb)
        self.group_action_brush.addAction(self.action_dense1)
        self.group_action_brush.addAction(self.action_dense2)
        self.group_action_brush.addAction(self.action_dense3)
        self.group_action_brush.addAction(self.action_dense4)
        self.group_action_brush.addAction(self.action_dense5)
        self.group_action_brush.addAction(self.action_dense6)
        self.group_action_brush.addAction(self.action_dense7)
        self.group_action_brush.addAction(self.action_hor)
        self.group_action_brush.addAction(self.action_ver)
        self.group_action_brush.addAction(self.action_cross)
        self.group_action_brush.addAction(self.action_bdiag)
        self.group_action_brush.addAction(self.action_fdiag)
        self.group_action_brush.addAction(self.action_diagcross)
        self.group_action_brush.addAction(self.action_nobrush)
        
        self.action_font = QtWidgets.QAction(self.tr("Font"), self)

    def create_menus(self) :
 #       statusbar=self.statusBar()
        menubar = self.menuBar()
        menu_file = menubar.addMenu('&File')
        menu_file.addAction(self.action_new)
        menu_file.addSeparator()
        menu_file.addAction(self.action_open)
        menu_file.addAction(self.action_save)
        menu_file.addAction(self.action_save_as)
        menu_file.addSeparator()
        menu_file.addAction(self.action_undo)
        menu_file.addAction(self.action_redo)
        menu_file.addSeparator()
        menu_file.addAction(self.action_exit)

        menu_tools = menubar.addMenu('&Tools')
        menu_tools.addAction(self.action_line)
        menu_file.addAction(self.action_save_as)
        menu_tools.addAction(self.action_rect)
        menu_tools.addAction(self.action_poly)
        menu_tools.addAction(self.action_eli)
        menu_tools.addSeparator()
        menu_tools.addAction(self.action_txt)
        
        

        menu_style=menubar.addMenu('&Style')
        menu_style_pen=menu_style.addMenu('Pen')
        menu_style_pen.addAction(self.action_pen_color)
        menu_style_pen.addAction(self.action_pen_width)
        menu_style_pen_line=menu_style_pen.addMenu('Line')
        menu_style_pen_line.addAction(self.action_solid)
        menu_style_pen_line.addAction(self.action_dash)
        menu_style_pen_line.addAction(self.action_dot)
        menu_style_pen_line.addAction(self.action_dashdot)
        menu_style_pen_line.addAction(self.action_dashdotdot)
        menu_style_pen_line.addAction(self.action_nopen)
        
        menu_style_brush=menu_style.addMenu('Brush')
        menu_style_brush.addAction(self.action_brush_color)
        menu_style_brush_fill=menu_style_brush.addMenu('Fill')
        menu_style_brush_fill.addAction(self.action_solidb)
        menu_style_brush_fill.addAction(self.action_dense1)
        menu_style_brush_fill.addAction(self.action_dense2)
        menu_style_brush_fill.addAction(self.action_dense3)
        menu_style_brush_fill.addAction(self.action_dense4)
        menu_style_brush_fill.addAction(self.action_dense5)
        menu_style_brush_fill.addAction(self.action_dense6)
        menu_style_brush_fill.addAction(self.action_dense7)
        menu_style_brush_fill.addAction(self.action_hor)
        menu_style_brush_fill.addAction(self.action_ver)
        menu_style_brush_fill.addAction(self.action_cross)
        menu_style_brush_fill.addAction(self.action_bdiag)
        menu_style_brush_fill.addAction(self.action_fdiag)
        menu_style_brush_fill.addAction(self.action_diagcross)
        menu_style_brush_fill.addAction(self.action_nobrush)
        
        menu_style.addAction(self.action_font)
        
        menu_help=self.menuBar().addMenu(self.tr("&Help"))
        
        self.action_about_us = menu_help.addAction(self.tr("& About Us"))
        self.action_about_qt = menu_help.addAction(self.tr("& About Qt/PyQt5"))
        self.action_about_app = menu_help.addAction(self.tr("& About the App"))

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(self.action_exit)

    def contextMenuEvent(self, event):
        contextMenu = QtWidgets.QMenu(self)
        
        menu_tools = contextMenu.addMenu('&Tools')
        menu_tools.addAction(self.action_line)
        menu_tools.addAction(self.action_rect)
        menu_tools.addAction(self.action_poly)
        menu_tools.addAction(self.action_eli)
        menu_tools.addSeparator()
        menu_tools.addAction(self.action_txt)
        
        
        menu_style=contextMenu.addMenu('&Style')
        
        menu_style_pen=menu_style.addMenu('Pen')
        menu_style_pen.addAction(self.action_pen_color)
        menu_style_pen.addAction(self.action_pen_width)
        menu_style_pen_line=menu_style_pen.addMenu('Line')
        menu_style_pen_line.addAction(self.action_solid)
        menu_style_pen_line.addAction(self.action_dash)
        menu_style_pen_line.addAction(self.action_dot)
        menu_style_pen_line.addAction(self.action_dashdot)
        menu_style_pen_line.addAction(self.action_dashdotdot)
        menu_style_pen_line.addAction(self.action_nopen)
        
        menu_style_brush=menu_style.addMenu('Brush')
        menu_style_brush.addAction(self.action_brush_color)
        menu_style_brush_fill=menu_style_brush.addMenu('Fill')
        menu_style_brush_fill.addAction(self.action_solidb)
        menu_style_brush_fill.addAction(self.action_dense1)
        menu_style_brush_fill.addAction(self.action_dense2)
        menu_style_brush_fill.addAction(self.action_dense3)
        menu_style_brush_fill.addAction(self.action_dense4)
        menu_style_brush_fill.addAction(self.action_dense5)
        menu_style_brush_fill.addAction(self.action_dense6)
        menu_style_brush_fill.addAction(self.action_dense7)
        menu_style_brush_fill.addAction(self.action_hor)
        menu_style_brush_fill.addAction(self.action_ver)
        menu_style_brush_fill.addAction(self.action_cross)
        menu_style_brush_fill.addAction(self.action_bdiag)
        menu_style_brush_fill.addAction(self.action_fdiag)
        menu_style_brush_fill.addAction(self.action_diagcross)
        menu_style_brush_fill.addAction(self.action_nobrush)
        
        menu_style.addAction(self.action_font)
        
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
    def connect_actions(self) :
        
        self.action_new.triggered.connect(self.file_new)
        self.action_open.triggered.connect(self.file_open)
        self.action_save.triggered.connect(self.file_save)
        self.action_undo.triggered.connect(self.undo)
        self.action_redo.triggered.connect(self.redo)
        self.action_save_as.triggered.connect(self.file_save_as)
        self.action_exit.triggered.connect(self.file_exit)
        
        self.action_about_us.triggered.connect(self.help_about_us)
        self.action_about_qt.triggered.connect(self.help_about_qt)
        self.action_about_app.triggered.connect(self.help_about_app)
        
        
        self.action_pen_color.triggered.connect(self.pen_color_selection)
        self.action_pen_width.triggered.connect(self.pen_width_selection)
        
        
        self.action_solid.triggered.connect(lambda checked, value=1: self.set_pen_line(checked,value))
        self.action_dash.triggered.connect(lambda checked, value=2: self.set_pen_line(checked,value))
        self.action_dot.triggered.connect(lambda checked, value=3: self.set_pen_line(checked,value))
        self.action_dashdot.triggered.connect(lambda checked, value=4: self.set_pen_line(checked,value))
        self.action_dashdotdot.triggered.connect(lambda checked, value=5: self.set_pen_line(checked,value))
        self.action_nopen.triggered.connect(lambda checked, value=0: self.set_pen_line(checked,value))
        
        self.action_brush_color.triggered.connect(self.brush_color_selection)
        
        self.action_solidb.triggered.connect(lambda checked, value=1: self.set_brush_fill(checked,value))
        self.action_dense1.triggered.connect(lambda checked, value=2: self.set_brush_fill(checked,value))
        self.action_dense2.triggered.connect(lambda checked, value=3: self.set_brush_fill(checked,value))
        self.action_dense3.triggered.connect(lambda checked, value=4: self.set_brush_fill(checked,value))
        self.action_dense4.triggered.connect(lambda checked, value=5: self.set_brush_fill(checked,value))
        self.action_dense5.triggered.connect(lambda checked, value=6: self.set_brush_fill(checked,value))
        self.action_dense6.triggered.connect(lambda checked, value=7: self.set_brush_fill(checked,value))
        self.action_dense7.triggered.connect(lambda checked, value=8: self.set_brush_fill(checked,value))
        self.action_hor.triggered.connect(lambda checked, value=9: self.set_brush_fill(checked,value))
        self.action_ver.triggered.connect(lambda checked, value=10: self.set_brush_fill(checked,value))
        self.action_cross.triggered.connect(lambda checked, value=11: self.set_brush_fill(checked,value))
        self.action_bdiag.triggered.connect(lambda checked, value=12: self.set_brush_fill(checked,value))
        self.action_fdiag.triggered.connect(lambda checked, value=13: self.set_brush_fill(checked,value))
        self.action_diagcross.triggered.connect(lambda checked, value=14: self.set_brush_fill(checked,value))
        self.action_nobrush.triggered.connect(lambda checked, value=0: self.set_brush_fill(checked,value))
        
        self.action_line.triggered.connect(lambda checked, tool="line": self.set_action_tool(checked,tool))
        self.action_rect.triggered.connect(lambda checked, tool="rect": self.set_action_tool(checked,tool))
        self.action_poly.triggered.connect(lambda checked, tool="poly": self.set_action_tool(checked,tool))
        self.action_eli.triggered.connect(lambda checked, tool="eli": self.set_action_tool(checked,tool))
        self.action_txt.triggered.connect(lambda checked, tool="text": self.set_action_tool(checked,tool))
        
        self.action_font.triggered.connect(self.font_selection)
        
        
    
    def file_exit(self):
        answer = QtWidgets.QMessageBox.question(self, self.tr("Exit ?"),
                                self.tr("Are you sure ?"), QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
        if answer == QtWidgets.QMessageBox.Yes:
            exit(0)
            
    def file_new(self):
        answer = QtWidgets.QMessageBox.warning(self, self.tr("New File ?"),
                                               self.tr("Are you sure ?\nDo you want to make a new file ?"), QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
        if answer == QtWidgets.QMessageBox.Yes:
            self.scene.clear()
            QtWidgets.QMessageBox.information(self, self.tr("Success !"),
                                              self.tr("New file created !"), QtWidgets.QMessageBox.Ok)
    
    def file_open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', os.getcwd(), "Json FILES (*.json)")
        fileopen=QtCore.QFile(filename[0])
        file_to_load = open(filename[0],"r")
        self.data_to_items(json.load(file_to_load))
        file_to_load.close()
        self.scene.update()
        print(filename[0] + " opened !")

    def file_save_as(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', f"{os.getcwd()}/unknown.json", "Json FILES (*.json)")
        self.scene.path = filename[0]
        filesave=QtCore.QFile(filename[0])
        filename=filename[0].split("/")
        self.scene.name=filename[-1]
        
        if filesave.open(QtCore.QIODevice.WriteOnly)==None :
            print("echec de sauvegarde du fichier : "+self.scene.name)
            return -1
        else :
            data=self.items_to_data()
            filesave.write(json.dumps(data).encode("utf-8"))
            filesave.close()
            print("sauvegarde du fichier : "+self.scene.name+" avec success")
    
    def file_save(self):
        if self.scene.path == None:
            self.file_save_as()
            return
        
        filesave=QtCore.QFile(self.scene.path)
        data=self.items_to_data()
        filesave.open(QtCore.QIODevice.WriteOnly)
        filesave.write(json.dumps(data).encode("utf-8"))
        filesave.close()
        print("sauvegarde du fichier : "+self.scene.name+" avec success")
        
    def data_to_items(self, data):
        self.scene.clear()
        print("data open")
        self.scene.path = data.pop(0)
        self.scene.name = data.pop(0)
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
                pen.setStyle(d_item["style"])
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
                pen.setStyle(d_item["style_pen"])
                brush.setColor(color_brush)
                brush.setStyle(d_item["fill_brush"])
                self.scene.addRect(x, y, width, height, pen, brush)
            
            elif t == "poly":
                
                points = []
                for point in d_item["points"]:
                    points.append(QtCore.QPointF(point[0],point[1]))
                    print(point)
                
                qpoly=QtGui.QPolygonF(points)

                
                pen = QtGui.QPen()
                brush = QtGui.QBrush()
                pen.setWidth(d_item["width_pen"])
                color_pen = QtGui.QColor()
                color_brush = QtGui.QColor()
                color_pen.setRgb(d_item["color_pen"])
                color_brush.setRgb(d_item["color_brush"])
                pen.setColor(color_pen)
                pen.setStyle(d_item["style_pen"])
                brush.setColor(color_brush)
                brush.setStyle(d_item["fill_brush"])

                self.scene.addPolygon(qpoly, pen, brush)
                
            elif t == "eli":
                x, y, width, height = d_item["x"], d_item["y"], d_item["width"], d_item["height"]
                pen = QtGui.QPen()
                brush = QtGui.QBrush()
                pen.setWidth(d_item["width_pen"])
                color_pen = QtGui.QColor()
                color_brush = QtGui.QColor()
                color_pen.setRgb(d_item["color_pen"])
                color_brush.setRgb(d_item["color_brush"])
                pen.setColor(color_pen)
                pen.setStyle(d_item["style_pen"])
                brush.setColor(color_brush)
                brush.setStyle(d_item["fill_brush"])
                self.scene.addEllipse(x, y, width, height, pen, brush)
                
            elif t == "text":
                txt = self.scene.addText(d_item["text"])
                txt.setPos(d_item["x"], d_item["y"])
                txt.setFont(QtGui.QFont(d_item["font_type"], d_item["font_size"]))

    def items_to_data(self):
        # liste de dictionnaires d'items à sauvegarder
        to_save=[self.scene.path,self.scene.name] 
        
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
                data["style"] = item.pen().style()
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
                data["style_pen"] = item.pen().style()
                data["color_brush"] = item.brush().color().rgb()
                data["fill_brush"] = item.brush().style()
                # ajout du dictionnaire dans la liste des dictionnaires d'items
                to_save.append(data)
                
            elif  isinstance(item, QtWidgets.QGraphicsEllipseItem): 
                data = {} 
                data["type"] = "eli"
                data["x"] = item.rect().x()
                data["y"] = item.rect().y()
                data["width"] = item.rect().width()
                data["height"] = item.rect().height()
                data["color_pen"] = item.pen().color().rgb()
                data["width_pen"] = item.pen().width()
                data["style_pen"] = item.pen().style()
                data["color_brush"] = item.brush().color().rgb()
                data["fill_brush"] = item.brush().style()
                # ajout du dictionnaire dans la liste des dictionnaires d'items
                to_save.append(data)
                
            elif  isinstance(item, QtWidgets.QGraphicsPolygonItem): 
                data = {} 
                polygon = item.polygon().toPolygon()
                data["type"] = "poly"
                data["points"] = []
                for point in range(0,polygon.count()):
                    x = polygon.point(point).x()
                    y = polygon.point(point).y()
                    data["points"].append((x,y))
                data["color_pen"] = item.pen().color().rgb()
                data["width_pen"] = item.pen().width()
                data["style_pen"] = item.pen().style()
                data["color_brush"] = item.brush().color().rgb()
                data["fill_brush"] = item.brush().style()
                # ajout du dictionnaire dans la liste des dictionnaires d'items
                to_save.append(data)  
            elif  isinstance(item, QtWidgets.QGraphicsTextItem): 
                data = {} 
                data["type"] = "text"
                data["x"] = item.pos().x()
                data["y"] = item.pos().y()
                data["text"] = item.toPlainText()
                data["font_type"] = item.font().family()
                data["font_size"] = item.font().weight()
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
        print(self)
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
            
    def font_selection(self):
        (font, ok) = QtWidgets.QFontDialog.getFont(QtGui.QFont("Helvetica [Cronyx]", 10), self)

        if ok:
            self.scene.font = (font.family(),font.weight())
            
    def set_action_tool(self,checked, tool) :
        print("lamda checked, tool : ",checked, tool)
        self.scene.set_tool(tool)
        
    def set_pen_line(self, checked, value):
        print("lamda checked, value : ",checked, value)
        self.scene.pen.setStyle(value)
        
    def set_brush_fill(self, checked, value):
        print("lamda checked, value : ",checked, value)
        self.scene.brush.setStyle(value)
                 
    def help_about_us(self):
        QtWidgets.QMessageBox.information(self, self.tr("About Us"),
                                self.tr("Guillaume/Choucq\ncopyright ENIB 2022P"))
    def help_about_app(self):
        text = open("README.txt","r")
        QtWidgets.QMessageBox.information(self, self.tr("About the App"),
                                          self.tr(text.read()))
        text.close()
        
    def help_about_qt(self):
        answer = QtWidgets.QMessageBox.information(self, self.tr("About Qt/PyQt5"),
                                                   self.tr("You Will be redirect to the documentation.\nDo you want to proceed ?"),
                                                   QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
        
        if answer == QtWidgets.QMessageBox.Yes:
            webbrowser.open('https://doc.qt.io/qtforpython/')
            
    def undo(self):
        if(self.scene.item_remove == None):
            for index, item in enumerate(self.scene.items()):
                if(index==0):
                    item.setVisible(False)
                    self.scene.update()
                    self.scene.item_remove=item
        else :
            for index, item in enumerate(self.scene.items()):
                if(index==1):
                    item.setVisible(False)
                    self.scene.removeItem(self.scene.item_remove)
                    self.update()
                    self.scene.item_remove=item
                    
    def redo(self):
        if(self.scene.item_remove==None):
            print("No item")
        else :
            self.scene.item_remove.setVisible(True)
            self.scene.item_remove = None
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
    
    
if __name__ == "__main__" :  
    print(QT_VERSION_STR)
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
