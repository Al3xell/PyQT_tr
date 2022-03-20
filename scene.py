#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore,QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QT_VERSION_STR

class Scene (QtWidgets.QGraphicsScene) :
    def __init__(self,parent=None) :
        QtWidgets.QGraphicsScene.__init__(self)
        self.name=None
        self.path=None
        self.tool=None
        self.font=("Helvetica [Cronyx]",10)
        self.begin,self.end,self.offset=QtCore.QPoint(0,0),QtCore.QPoint(0,0),QtCore.QPoint(0,0)
        self.item=None
        self.pen=QtGui.QPen()
        self.pen.setColor(QtCore.Qt.red)
        self.pen.setWidth(3)
        self.brush=QtGui.QBrush(QtCore.Qt.green)
    #    self.brush.setColor(QtCore.Qt.green)
        rect=QtWidgets.QGraphicsRectItem(0,0,100,100)
        rect.setPen(self.pen)
        rect.setBrush(self.brush)
        self.addItem(rect)
        self.polygon=[]
        
    def set_tool(self,tool) :
        print("set_tool(self,tool)",tool)
        self.tool=tool

    def set_pen_color(self,color) :
        print("set_pen_color(self,color)",color)
        self.pen.setColor(color)

    def set_brush_color(self,color) :
       print("set_brush_color(self,color)",color)
       self.brush.setColor(color)
 
    def mousePressEvent(self, event):
        print("Scene.mousePressEvent()")
        self.begin = self.end = event.scenePos()
        self.item=self.itemAt(self.begin,QtGui.QTransform())
        if self.item :
            self.offset =self.begin-self.item.pos()
        elif self.tool == "poly":
            print("button_press_event()")
            point=event.scenePos()
            print("coordonnes View  : event.pos() ",point)
            # Ajout de point de polygone 
            self.polygon.append(point)
                
    def mouseMoveEvent(self, event):
        # print("Scene.mouseMoveEvent()",self.item)
        if self.item :
            self.item.setPos(event.scenePos() - self.offset)
        self.end = event.scenePos()
 
    def mouseReleaseEvent(self, event):
        print("Scene.mouseReleaseEvent()",self.tool)
        self.end = event.scenePos()
        if self.item :
            self.item.setPos(event.scenePos() - self.offset)
            self.item=None
        elif self.tool=='line' :
            self.addLine(self.begin.x(), self.begin.y(),self.end.x(), self.end.y(),self.pen)
        elif self.tool=='rect' :
            self.addRect(self.begin.x(), self.begin.y(),self.end.x()-self.begin.x(), self.end.y()-self.begin.y(),self.pen, self.brush)
        elif self.tool=='eli' :
            self.addEllipse(self.begin.x(), self.begin.y(),self.end.x()-self.begin.x(), self.end.y()-self.begin.y(),self.pen, self.brush)
        elif self.tool=='text' :
            text = QtWidgets.QInputDialog.getText(None, "Text", "Enter the text")
            print(text)
            if text :
                print("Text choosen : ", text)
                txt = self.addText(text[0])
                txt.setPos(self.end.x(), self.end.y())
                txt.setFont(QtGui.QFont(self.font[0], self.font[1]))
        
        elif self.tool=='poly' :
            print("Polygone en cours de formation")
        else :
            print("no item selected and nothing to draw !")
            
    def mouseDoubleClickEvent(self, event):
        
        print("mouseDoubleClickEvent()")
        qpoly=QtGui.QPolygonF(self.polygon)
        qgpoly=QtWidgets.QGraphicsPolygonItem(qpoly)
        qgpoly.setPen(self.pen)
        qgpoly.setBrush(self.brush)
        self.addItem(qgpoly)
        del self.polygon[:]
