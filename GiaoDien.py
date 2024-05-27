# Form implementation generated from reading ui file 'GiaoDien.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import re
import sys
import Assembly
from dict import line_edit_dict, conditon_dict
import Create_memory
from encoder import Encoder
from decoder import Decoder


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 691)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 70, 1131, 621))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.SimulateButton = QtWidgets.QPushButton(parent=self.tab_1)
        self.SimulateButton.setGeometry(QtCore.QRect(630, 320, 111, 51))
        self.SimulateButton.setObjectName("SimulateButton")
        self.RestarButton = QtWidgets.QPushButton(parent=self.tab_1)
        self.RestarButton.setGeometry(QtCore.QRect(990, 320, 111, 51))
        self.RestarButton.setObjectName("RestarButton")
        self.StepButton = QtWidgets.QPushButton(parent=self.tab_1)
        self.StepButton.setGeometry(QtCore.QRect(750, 320, 111, 51))
        self.StepButton.setObjectName("StepButton")
        self.BreakPointButton = QtWidgets.QPushButton(parent=self.tab_1)
        self.BreakPointButton.setGeometry(QtCore.QRect(870, 320, 111, 51))
        self.BreakPointButton.setObjectName("BreakPointButton")
        self.CodeEditText = QtWidgets.QTextEdit(parent=self.tab_1)
        self.CodeEditText.setGeometry(QtCore.QRect(620, 30, 491, 271))
        self.CodeEditText.setObjectName("CodeEditText")
        
        self.SimulateButton.clicked.connect(self.Check)
        self.RestarButton.clicked.connect(self.Restart)
        self.StepButton.clicked.connect(self.check_next_line)
        
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.tab_1)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 381, 511))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.Layout_registers = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.Layout_registers.setContentsMargins(10, 10, 10, 0)
        self.Layout_registers.setObjectName("Layout_registers")
        self.r0_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r0_Label.setObjectName("r0_Label")
        self.Layout_registers.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r0_Label)
        self.r0_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r0_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r0_LineEdit.setObjectName("r0_LineEdit")
        self.Layout_registers.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r0_LineEdit)
        self.r1_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r1_Label.setObjectName("r1_Label")
        self.Layout_registers.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r1_Label)
        self.r1_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r1_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r1_LineEdit.setObjectName("r1_LineEdit")
        self.Layout_registers.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r1_LineEdit)
        self.r2_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r2_Label.setObjectName("r2_Label")
        self.Layout_registers.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r2_Label)
        self.r2_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r2_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r2_LineEdit.setObjectName("r2_LineEdit")
        self.Layout_registers.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r2_LineEdit)
        self.r3_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r3_Label.setObjectName("r3_Label")
        self.Layout_registers.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r3_Label)
        self.r3_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r3_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r3_LineEdit.setObjectName("r3_LineEdit")
        self.Layout_registers.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r3_LineEdit)
        self.r4_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r4_Label.setObjectName("r4_Label")
        self.Layout_registers.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r4_Label)
        self.r4_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r4_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r4_LineEdit.setObjectName("r4_LineEdit")
        self.Layout_registers.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r4_LineEdit)
        self.r5_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r5_Label.setObjectName("r5_Label")
        self.Layout_registers.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r5_Label)
        self.r5_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r5_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r5_LineEdit.setObjectName("r5_LineEdit")
        self.Layout_registers.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r5_LineEdit)
        self.r6_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r6_Label.setObjectName("r6_Label")
        self.Layout_registers.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r6_Label)
        self.r6_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r6_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r6_LineEdit.setObjectName("r6_LineEdit")
        self.Layout_registers.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r6_LineEdit)
        self.r7_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r7_Label.setObjectName("r7_Label")
        self.Layout_registers.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r7_Label)
        self.r7_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r7_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r7_LineEdit.setObjectName("r7_LineEdit")
        self.Layout_registers.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r7_LineEdit)
        self.r8_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r8_Label.setObjectName("r8_Label")
        self.Layout_registers.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r8_Label)
        self.r8_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r8_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r8_LineEdit.setObjectName("r8_LineEdit")
        self.Layout_registers.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r8_LineEdit)
        self.r9_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r9_Label.setObjectName("r9_Label")
        self.Layout_registers.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r9_Label)
        self.r9_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r9_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r9_LineEdit.setObjectName("r9_LineEdit")
        self.Layout_registers.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r9_LineEdit)
        self.r10_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r10_Label.setObjectName("r10_Label")
        self.Layout_registers.setWidget(10, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r10_Label)
        self.r10_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r10_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r10_LineEdit.setObjectName("r10_LineEdit")
        self.Layout_registers.setWidget(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r10_LineEdit)
        self.r11_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r11_Label.setObjectName("r11_Label")
        self.Layout_registers.setWidget(11, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r11_Label)
        self.r11_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r11_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r11_LineEdit.setObjectName("r11_LineEdit")
        self.Layout_registers.setWidget(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r11_LineEdit)
        self.r12_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.r12_Label.setObjectName("r12_Label")
        self.Layout_registers.setWidget(12, QtWidgets.QFormLayout.ItemRole.LabelRole, self.r12_Label)
        self.r12_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.r12_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r12_LineEdit.setObjectName("r12_LineEdit")
        self.Layout_registers.setWidget(12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.r12_LineEdit)
        self.sp_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.sp_Label.setObjectName("sp_Label")
        self.Layout_registers.setWidget(13, QtWidgets.QFormLayout.ItemRole.LabelRole, self.sp_Label)
        self.sp_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.sp_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sp_LineEdit.setObjectName("sp_LineEdit")
        self.Layout_registers.setWidget(13, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sp_LineEdit)
        self.lr_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.lr_Label.setObjectName("lr_Label")
        self.Layout_registers.setWidget(14, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lr_Label)
        self.lr_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lr_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lr_LineEdit.setObjectName("lr_LineEdit")
        self.Layout_registers.setWidget(14, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lr_LineEdit)
        self.pc_Label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.pc_Label.setObjectName("pc_Label")
        self.Layout_registers.setWidget(15, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pc_Label)
        self.pc_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.pc_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pc_LineEdit.setObjectName("pc_LineEdit")
        self.Layout_registers.setWidget(15, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pc_LineEdit)
        
        line_edit_dict["r0"] = self.r0_LineEdit
        line_edit_dict["r1"] = self.r1_LineEdit
        line_edit_dict["r2"] = self.r2_LineEdit
        line_edit_dict["r3"] = self.r3_LineEdit
        line_edit_dict["r4"] = self.r4_LineEdit
        line_edit_dict["r5"] = self.r5_LineEdit
        line_edit_dict["r6"] = self.r6_LineEdit
        line_edit_dict["r7"] = self.r7_LineEdit
        line_edit_dict["r8"] = self.r8_LineEdit
        line_edit_dict["r9"] = self.r9_LineEdit
        line_edit_dict["r10"] = self.r10_LineEdit
        line_edit_dict["r11"] = self.r11_LineEdit
        line_edit_dict["r12"] = self.r12_LineEdit
        line_edit_dict["lr"] = self.lr_LineEdit
        line_edit_dict["sp"] = self.sp_LineEdit
        line_edit_dict["pc"] = self.pc_LineEdit

        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_1)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(430, 30, 160, 138))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.Layout_condition = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.Layout_condition.setContentsMargins(10, 10, 10, 10)
        self.Layout_condition.setObjectName("Layout_condition")
        self.n_Label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.n_Label.setObjectName("n_Label")
        self.Layout_condition.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.n_Label)
        self.n_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.n_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_LineEdit.setObjectName("n_LineEdit")
        self.Layout_condition.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.n_LineEdit)
        self.z_Label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.z_Label.setObjectName("z_Label")
        self.Layout_condition.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.z_Label)
        self.z_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.z_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.z_LineEdit.setObjectName("z_LineEdit")
        self.Layout_condition.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.z_LineEdit)
        self.c_Label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.c_Label.setObjectName("c_Label")
        self.Layout_condition.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.c_Label)
        self.c_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.c_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.c_LineEdit.setObjectName("c_LineEdit")
        self.Layout_condition.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.c_LineEdit)
        self.v_Label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.v_Label.setObjectName("v_Label")
        self.Layout_condition.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.v_Label)
        self.v_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.v_LineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.v_LineEdit.setObjectName("v_LineEdit")
        self.Layout_condition.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.v_LineEdit)
        
        conditon_dict["n"] = self.n_LineEdit
        conditon_dict["z"] = self.z_LineEdit
        conditon_dict["c"] = self.c_LineEdit
        conditon_dict["v"] = self.v_LineEdit
        
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 201, 31))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.sizeMemory_LineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.sizeMemory_LineEdit.setFont(font)
        self.sizeMemory_LineEdit.setObjectName("sizeMemory_LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sizeMemory_LineEdit)
        self.sizeMemory_Label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.sizeMemory_Label.setObjectName("sizeMemory_Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.sizeMemory_Label)
        self.MemoryTextEdit = QtWidgets.QPlainTextEdit(parent=self.tab_2)
        self.MemoryTextEdit.setGeometry(QtCore.QRect(20, 50, 1091, 521))
        self.MemoryTextEdit.setObjectName("MemoryTextEdit")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SimulateButton.setText(_translate("MainWindow", "Simulate"))
        self.RestarButton.setText(_translate("MainWindow", "Restart"))
        self.StepButton.setText(_translate("MainWindow", "Step"))
        self.BreakPointButton.setText(_translate("MainWindow", "BreakPoint"))
        self.r0_Label.setText(_translate("MainWindow", "r0"))
        self.r0_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r1_Label.setText(_translate("MainWindow", "r1"))
        self.r1_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r2_Label.setText(_translate("MainWindow", "r2"))
        self.r2_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r3_Label.setText(_translate("MainWindow", "r3"))
        self.r3_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r4_Label.setText(_translate("MainWindow", "r4"))
        self.r4_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r5_Label.setText(_translate("MainWindow", "r5"))
        self.r5_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r6_Label.setText(_translate("MainWindow", "r6"))
        self.r6_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r7_Label.setText(_translate("MainWindow", "r7"))
        self.r7_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r8_Label.setText(_translate("MainWindow", "r8"))
        self.r8_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r9_Label.setText(_translate("MainWindow", "r9"))
        self.r9_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r10_Label.setText(_translate("MainWindow", "r10"))
        self.r10_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r11_Label.setText(_translate("MainWindow", "r11"))
        self.r11_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.r12_Label.setText(_translate("MainWindow", "r12"))
        self.r12_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.sp_Label.setText(_translate("MainWindow", "sp"))
        self.sp_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.lr_Label.setText(_translate("MainWindow", "lr"))
        self.lr_LineEdit.setText(_translate("MainWindow", "00000000000000000000000000000000"))
        self.pc_Label.setText(_translate("MainWindow", "pc"))
        self.pc_LineEdit.setText(_translate("MainWindow", hex(0)))
        self.n_Label.setText(_translate("MainWindow", "N"))
        self.n_LineEdit.setText(_translate("MainWindow", "0"))
        self.z_Label.setText(_translate("MainWindow", "Z"))
        self.z_LineEdit.setText(_translate("MainWindow", "0"))
        self.c_Label.setText(_translate("MainWindow", "C"))
        self.c_LineEdit.setText(_translate("MainWindow", "0"))
        self.v_Label.setText(_translate("MainWindow", "V"))
        self.v_LineEdit.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Editor"))
        self.sizeMemory_LineEdit.setText(_translate("MainWindow", "32"))
        self.sizeMemory_Label.setText(_translate("MainWindow", "Size(bytes)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Memory"))
        self.label.setText(_translate("MainWindow", "ARMv7-M instruction set simulator"))
        
    pc = 0
    instruction_size = 4
    address = []
    
    def Check(self):
        self.message_box = QtWidgets.QMessageBox(self.tab_1)
        global pc
        memory = []
        text = self.CodeEditText.toPlainText()
        lines = text.split("\n")
        for index, line in enumerate(lines, start=1):
            pc_binary = '0x' + format(self.pc, '08x')
            self.pc_LineEdit.setText(pc_binary)
            self.address.append(pc_binary)
            self.pc += self.instruction_size
            
            memory_line = Create_memory.check_memory(self, line)
            if memory_line:
                memory.append(memory_line)
                
            if not len(memory) > int(self.sizeMemory_LineEdit.text()):
                text_content = "\t".join(str(item) for item in memory)
                self.MemoryTextEdit.setPlainText(text_content)
            else:
                print("Out of Memory")
                break
        
        for index, line in enumerate(lines, start=1):
            if line.strip():
                reg, arguments, flag_N, flag_Z, flag_C, flag_V, flag_T = Assembly.check_assembly_line(self, line, self.address, memory)
            elif not line.strip():
                print("không có câu lệnh nào")
                break

            if arguments and len(reg) == 1 and len(arguments) == 1:
                line_edit = line_edit_dict.get(reg[0])
                line_edit.setText(arguments[0])
            elif arguments and len(reg) == 2 and len(arguments) == 2:
                line_edit_1 = line_edit_dict.get(reg[0])
                line_edit_1.setText(arguments[0])
                line_edit_2 = line_edit_dict.get(reg[1])
                line_edit_2.setText(arguments[1])
            elif arguments is None and flag_T:
                pass
            elif arguments is None:
                print("Lệnh ở dòng " + str(index) + " không hợp lệ")
                break
                
            n_edit = conditon_dict.get("n")
            z_edit = conditon_dict.get("z")
            c_edit = conditon_dict.get("c")
            v_edit = conditon_dict.get("v")

            n_edit.setText(flag_N)
            z_edit.setText(flag_Z)
            c_edit.setText(flag_C)
            v_edit.setText(flag_V)
                       
    current_line_index = 0
    memory_current_line = []
    def check_next_line(self):
        global current_line_index
        text = self.CodeEditText.toPlainText()    
        lines = text.split("\n")
        if self.current_line_index == 0:
            address_index = 0
            for index, line in enumerate(lines, start=1):
                pc_binary = '0x' + format(address_index, '08x')
                self.address.append(pc_binary)
                address_index += self.instruction_size
                
                memory_line = Create_memory.check_memory(self, line)
                if memory_line:
                    self.memory_current_line.append(memory_line)
                    
                if not len(self.memory_current_line) > int(self.sizeMemory_LineEdit.text()):
                    text_content = "\t".join(str(item) for item in self.memory_current_line)
                    self.MemoryTextEdit.setPlainText(text_content)
                else:
                    print("Out of Memory")
                    break
        if self.current_line_index < len(lines):
            current_line = lines[self.current_line_index]
            if current_line.strip():
                reg, arguments, flag_N, flag_Z, flag_C, flag_V, flag_T = Assembly.check_assembly_line(self, current_line, self.address, self.memory_current_line)
            elif not line.strip():
                print("không còn câu lệnh nào")
                pass
                
            if arguments and len(reg) == 1 and len(arguments) == 1:
                line_edit = line_edit_dict.get(reg[0])
                line_edit.setText(arguments[0])
            elif arguments and len(reg) == 2 and len(arguments) == 2:
                line_edit_1 = line_edit_dict.get(reg[0])
                line_edit_1.setText(arguments[0])
                line_edit_2 = line_edit_dict.get(reg[1])
                line_edit_2.setText(arguments[1])
            elif arguments is None and flag_T:
                pass
            elif arguments is None:
                print("Lệnh ở dòng " + str(self.current_line_index) + " không hợp lệ")
                    
            n_edit = conditon_dict.get("n")
            z_edit = conditon_dict.get("z")
            c_edit = conditon_dict.get("c")
            v_edit = conditon_dict.get("v")

            n_edit.setText(flag_N)
            z_edit.setText(flag_Z)
            c_edit.setText(flag_C)
            v_edit.setText(flag_V)
            
            pc_binary = '0x' + format(self.pc, '08x')
            self.pc_LineEdit.setText(pc_binary)
            self.pc += self.instruction_size
            
            self.current_line_index += 1

    def Restart(self):
        self.address = []
        self.memory_current_line = []
        self.CodeEditText.setText("")
        self.r0_LineEdit.setText(f"{0:032b}")
        self.r1_LineEdit.setText(f"{0:032b}")
        self.r2_LineEdit.setText(f"{0:032b}")
        self.r3_LineEdit.setText(f"{0:032b}")
        self.r4_LineEdit.setText(f"{0:032b}")
        self.r5_LineEdit.setText(f"{0:032b}")
        self.r6_LineEdit.setText(f"{0:032b}")
        self.r7_LineEdit.setText(f"{0:032b}")
        self.r8_LineEdit.setText(f"{0:032b}")
        self.r9_LineEdit.setText(f"{0:032b}")
        self.r10_LineEdit.setText(f"{0:032b}")
        self.r11_LineEdit.setText(f"{0:032b}")
        self.r12_LineEdit.setText(f"{0:032b}")
        self.sp_LineEdit.setText(f"{0:032b}")
        self.lr_LineEdit.setText(f"{0:032b}")
        self.pc = 0
        self.pc_LineEdit.setText('0x' + format(0, '08x'))
        self.current_line_index = 0
        self.n_LineEdit.setText("0")
        self.z_LineEdit.setText("0")
        self.c_LineEdit.setText("0")
        self.v_LineEdit.setText("0")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
