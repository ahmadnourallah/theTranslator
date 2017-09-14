from __main__ import *
from sys import path
sys.path.append('/home/{0}/.theTranslatorConfig/'.format(getuser()))
from ProgramLanguage import CurrentLanguage
import config
sys.path.append('/usr/share/theTranslator/')
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *
from imp import reload
from translateapi.supportLanguage import *


class SettingsWidget(QDialog):
    def __init__(self, parent=None):
        super(SettingsWidget, self).__init__(parent)
        loadUi('ui/settings.ui',self)
        self.setFixedSize(327,342)
        #
        reload(config)
        from config import MainLanguage, Translator, DefaultTranslateLanguage, FontType, FontSize
        if Translator == 'Yandex':
            self.comboBox3.clear()
            for i in YandexSupportLanguage:
                self.comboBox3.addItem(i)
        elif Translator == "Google":
            self.comboBox3.clear()
            for i in sorted(language_code.keys()):
                self.comboBox3.addItem(i)
        self.targetPosition = self.comboBox1.findText(str(MainLanguage))
        self.comboBox1.setCurrentIndex(self.targetPosition)
        self.targetPosition = self.comboBox2.findText(str(Translator))
        self.comboBox2.setCurrentIndex(self.targetPosition)
        self.targetPosition = self.comboBox3.findText(str(DefaultTranslateLanguage))
        self.comboBox3.setCurrentIndex(self.targetPosition)
        self.targetPosition = self.fontComboBox.findText(str(FontType))
        self.fontComboBox.setCurrentIndex(self.targetPosition)
        self.fontSizeSpin.setValue(int(FontSize))
        #
        self.cancelButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(self.save_config)
        self.pushButton.clicked.connect(self.background_color_picker)
        self.pushButton2.clicked.connect(self.font_color_picker)
        #
        if CurrentLanguage == 'Arabic':
            self.setLayoutDirection(Qt.RightToLeft)
            self.comboBox1.setGeometry(12,61,101,29)
            self.label1.setGeometry(150,60,123,21)
            self.comboBox2.setGeometry(12,121,101,29)
            self.label2.setGeometry(180,120,69,21)
            self.comboBox3.setGeometry(12,181,101,29)
            self.label3.setGeometry(130,180,191,29)
            self.pushButton.setGeometry(12,38,97,31)
            self.label4.setGeometry(160,41,131,21)
            self.fontComboBox.setGeometry(10,100,171,29)
            self.label5.setGeometry(195,101,81,21)
            self.pushButton2.setGeometry(10,159,97,31)
            self.label6.setGeometry(200,161,81,21)
            self.fontSizeLabel.setGeometry(215,221,65,21)
            self.fontSizeSpin.setGeometry(10,214,60,31)
        self.fontComboBox.setContextMenuPolicy(Qt.CustomContextMenu)

    def background_color_picker(self):
        self.backgroundColor = QColorDialog.getColor()

    def font_color_picker(self):
        self.fontColor = QColorDialog.getColor()

    def save_config(self):
        with open('/home/{0}/.theTranslatorConfig/config.py'.format(getuser()),'w') as f:
            data = "MainLanguage = '{}'".format(self.comboBox1.currentText())
            data += "\nTranslator = '{}'".format(self.comboBox2.currentText())
            data += "\nDefaultTranslateLanguage = '{}'".format(self.comboBox3.currentText())
            try:
                data += "\nBackgroundColor = '{}'".format(self.backgroundColor.name())
            except Exception:
                data += "\nBackgroundColor = 'off'"
            try:
                data + "FontColor = '{}'".format(self.fontColor.name())
            except Exception:
                data += "\nFontColor = 'off'"
            data += "\nFontType = '{}'".format(self.fontComboBox.currentText())
            data += "\nFontSize = '{}'".format(self.fontSizeSpin.value())
            f.write(data)
            self.close()
