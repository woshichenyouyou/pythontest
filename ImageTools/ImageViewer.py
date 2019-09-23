# -*- coding: utf-8 -*-

"""
Module implementing CImageViewer.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QGraphicsScene
from PyQt5.QtGui import *
from Ui_ImageViewer import Ui_Form

from PkgImgCtl  import  DcmReader
class CImageViewer(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(CImageViewer, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_OpenImage_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
        file_name, filetype = QFileDialog.getOpenFileName(self,"open file dialog","/home/cyy","Txt files(*.*)")
        ##"open file Dialog "文件对话框的标题，第二个是打开的默认路径，第三个是文件类型
        if file_name != "":
            self.label_Path.setText(file_name)
            dr = DcmReader()
            dr.LoadFromFile(file_name)
            
#            self.scene = QGraphicsScene(self)
#            image=QImage()
#            image.load(file_name)
#            pixmap=QPixmap().fromImage(image)
#            #pixmap.load(file_name)
#            
#            self.scene.addPixmap(pixmap)
#            self.graphicsView__Image.setScene(self.scene)
#            self.graphicsView__Image.resize(image.width() + 10, image.height() + 10)
#            self.graphicsView__Image.show()
        #raise NotImplementedError

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = CImageViewer()
    dlg.show()
    sys.exit(app.exec_())
    
