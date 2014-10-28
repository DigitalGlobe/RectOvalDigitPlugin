# -*- coding: utf-8 -*-
"""
/***************************************************************************
 StationLinesDialog
                                 A QGIS plugin
 Create lines along a polyline with specifications (length, side, angle)
                             -------------------
        begin                : 2014-04-11
        copyright            : (C) 2014 by Loïc BARTOLETTI
        email                : l.bartoletti@free.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_getDistance import Ui_DialogRadius
from ui_getAngle import Ui_DialogAngle
from ui_CADDigitizeSettings import Ui_CADDigitizeSettings
# create the dialog for zoom to point


class Ui_CADDigitizeDialogRadius(QtGui.QDialog, Ui_DialogRadius):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
class Ui_CADDigitizeDialogAngle(QtGui.QDialog, Ui_DialogAngle):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

class Ui_CADDigitizeSettings(QtGui.QDialog, Ui_CADDigitizeSettings):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
            
        self.settings = QtCore.QSettings()
        self.circle_segments = self.settings.value("/CADDigitize/circle/segments", 36,type=int)
        self.ellipse_points = self.settings.value("/CADDigitize/ellipse/segments", 36,type=int)
        self.arc_featurePitch = self.settings.value("/CADDigitize/arc/pitch", 2,type=float)
        self.arc_featureAngle = self.settings.value("/CADDigitize/arc/angle", 1,type=int)
        self.arc_method = self.settings.value("/CADDigitize/arc/method",  "pitch")
        self.arc_angleDirection = self.settings.value("/CADDigitize/arc/direction",  "ClockWise")

        self.ArcFeaturePitch.setMinimum(1)
        self.ArcFeaturePitch.setMaximum(1000)
        self.ArcFeaturePitch.setDecimals(1)
        self.ArcFeaturePitch.setValue(int(self.arc_featurePitch))
        
        self.ArcFeatureAngle.setMinimum(1)
        self.ArcFeatureAngle.setMaximum(90)
        self.ArcFeatureAngle.setDecimals(0)    
        self.ArcFeatureAngle.setValue(int(self.arc_featureAngle))    
        
        self.circleSegmentsSpinbox.setMinimum(3)
        self.circleSegmentsSpinbox.setMaximum(3600)
        self.circleSegmentsSpinbox.setDecimals(0)    
        self.circleSegmentsSpinbox.setValue(int(self.circle_segments))
        
        self.ellipsePointsSpinbox.setMinimum(4)
        self.ellipsePointsSpinbox.setMaximum(3600)
        self.ellipsePointsSpinbox.setDecimals(0)    
        self.ellipsePointsSpinbox.setValue(int(self.ellipse_points))             
      

        if self.arc_method == "pitch":
            self.radioFeaturePitch.setChecked(True)
            self.radioFeatureAngle.setChecked(False)
            self.settings.setValue("/CADDigitize/arc/segments", self.settings.value("/CADDigitize/arc/pitch", 2,type=float))
        else:
            self.radioFeaturePitch.setChecked(False)
            self.radioFeatureAngle.setChecked(True) 
            self.settings.setValue("/CADDigitize/arc/segments", self.settings.value("/CADDigitize/arc/angle", 1,type=int))
            
        if self.arc_angleDirection == "ClockWise":
            self.ArcClockWise.setChecked(True)
            self.ArcCounterClockWise.setChecked(False)
        else:
            self.ArcClockWise.setChecked(False)
            self.ArcCounterClockWise.setChecked(True)
                
        self.okButton = self.buttonBox.button(QtGui.QDialogButtonBox.Ok)
        self.okButton.clicked.connect(self.accept)

        self.cancelButton = self.buttonBox.button(QtGui.QDialogButtonBox.Cancel)
        self.cancelButton.clicked.connect(self.close)

        pass



#    @pyqtSignature("on_btnSelectVertex_clicked()") 
#    def on_btnSelectVertex_clicked(self):
#        self.method = "vertex"
#        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)   
#        self.btnSelectVertex_clicked.emit()
#
#
    def accept(self):
        self.settings.setValue("/CADDigitize/circle/segments", self.circleSegmentsSpinbox.value())
        self.settings.setValue("/CADDigitize/ellipse/segments", self.ellipsePointsSpinbox.value())
        self.settings.setValue("/CADDigitize/arc/pitch", self.ArcFeaturePitch.value())
        self.settings.setValue("/CADDigitize/arc/angle", self.ArcFeatureAngle.value())
        
        if self.radioFeaturePitch.isChecked():
            self.settings.setValue("/CADDigitize/arc/method",  "pitch")
            self.settings.setValue("/CADDigitize/arc/segments", self.settings.value("/CADDigitize/arc/pitch"))
        else:
            self.settings.setValue("/CADDigitize/arc/method",  "angle")
            self.settings.setValue("/CADDigitize/arc/segments", self.settings.value("/CADDigitize/arc/angle"))

        if self.ArcClockWise.isChecked():
            self.settings.setValue("/CADDigitize/arc/direction",  "ClockWise")
        else:
            self.settings.setValue("/CADDigitize/arc/direction",  "CounterClockWise")
            
        self.close()
        
