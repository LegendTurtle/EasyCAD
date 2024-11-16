import openpyscad as ops
import os

"""
c1 = ops.Cylinder(h = 2, d = 6)
c2 = ops.Cylinder(h = 16, d = 3)
c1 = c1.translate([0, 0, 16])
u1 = ops.Union()
u1.append(c1)
u1.append(c2)
sh1 = ops.Cube([0.5, 4, 0.5]).translate([-0.25, -2, 17.75])
sh2 = ops.Cube([0.5, 4, 0.5]).translate([-0.25, -2, 17.75]).rotate([0, 0, 90])
u2 = ops.Union()
u2.append(sh1)
u2.append(sh2)
dif = ops.Difference()
dif.append(u1)
dif.append(u2)
create_model(dif)"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(512, 376)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(160, 20, 81, 51))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 201, 51))
        self.label_2.setObjectName("label_2")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(160, 90, 81, 51))
        self.spinBox_2.setObjectName("spinBox_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 330, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 330, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 185, 141, 41))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 180, 321, 51))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.click)
        self.pushButton_2.clicked.connect(exit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Holes in width"))
        self.label_2.setText(_translate("Dialog", "Holes in lenght"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label_3.setText(_translate("Dialog", "Filename"))
    def click(self):
        holes = ops.Union()
        planka = ops.Cube([self.spinBox.value()*10, self.spinBox_2.value()*10, 6])
        for i in range(self.spinBox.value()):
            for j in range(self.spinBox_2.value()):
                holes.append(ops.Circle(1.5, 3, 100).translate([5, 5, 0]).translate([i*10, j*10, 0]))
        holes = holes.linear_extrude(7).translate([0, 0, -0.1])
        result = ops.Difference()
        result.append(planka)
        result.append(holes)
        result = "module a(){" + str(result) + "};\nprojection() a();"
        with open(f"{self.lineEdit.text()}.scad", "w") as f:
            f.write(result)
        exit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
