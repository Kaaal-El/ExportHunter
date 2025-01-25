# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCharFormat, QColor, QFont, QSyntaxHighlighter,QTextCursor
import helper.globalVariables as globalVariables
from helper.JavaHighlighter import JavaHighlighter
from helper.javaCodeAnalyzer import javaCodeAnalyzer
from helper.ExceptionHandler import ExceptionHandler
from ui.ui_form import Ui_MainWindow
from ui.ui_addExtrasDialog import Ui_addExtrasDialog
from ui.ui_configureBundle import Ui_configureBundle
from ui.ui_apkCreate import Ui_apkCreate
import subprocess,os, xml.etree.ElementTree as ET
from PySide6.QtWidgets import (QFileDialog, QDialog, QTableWidgetItem)

import re


class MainWindow(QMainWindow):

    def addExtrasWindow(self):
        try:

            def onBundleCheckBoxChanged(state):
                if(state==2):

                    ui.typeInput.setText("Bundle"+str(globalVariables.numberOfBundles))
                    ui.typeInput.setReadOnly(True)
                    ui.typeInput.setEnabled(False)
                    ui.valueInput.setText("[Configure Later]")
                    ui.valueInput.setReadOnly(True)
                    ui.valueInput.setEnabled(False)


                if(state==0):
                    ui.typeInput.setText("")
                    ui.typeInput.setReadOnly(False)
                    ui.typeInput.setEnabled(True)
                    ui.valueInput.setText("")
                    ui.valueInput.setReadOnly(False)
                    ui.valueInput.setEnabled(True)

            window = QDialog()
            ui = Ui_addExtrasDialog()
            ui.setupUi(window)

            ui.bundleCheckBox.stateChanged.connect(onBundleCheckBoxChanged)

            if window.exec() == QDialog.Accepted:
                if(ui.typeInput.isEnabled()):
                    row_position = self.ui.extrasTable.rowCount()
                    self.ui.extrasTable.insertRow(row_position)
                    self.ui.extrasTable.setItem(row_position, 0, QTableWidgetItem(ui.typeInput.text()))
                    self.ui.extrasTable.setItem(row_position, 1, QTableWidgetItem(ui.keyInput.text()))
                    self.ui.extrasTable.setItem(row_position, 2, QTableWidgetItem(ui.valueInput.text()))

                else:
                    globalVariables.numberOfBundles += 1
                    configure_button = QPushButton("Configure")
                    configure_button.setFixedSize(100,30)
                    row_position = self.ui.extrasTable.rowCount()
                    self.ui.extrasTable.insertRow(row_position)
                    self.ui.extrasTable.setItem(row_position, 0, QTableWidgetItem(ui.typeInput.text()))
                    self.ui.extrasTable.setItem(row_position, 1, QTableWidgetItem(ui.keyInput.text()))
                    self.ui.extrasTable.setCellWidget(row_position, 2, configure_button)

                    cell = self.ui.extrasTable.item(row_position,0)
                    cell.setFlags(cell.flags() & ~Qt.ItemIsEditable & ~Qt.ItemIsEnabled)

                    cell2 = self.ui.extrasTable.item(row_position,2)

                    configure_button.clicked.connect(lambda checked, bundleId=ui.typeInput.text(): self.configureBundleWindow(bundleId))

        except Exception as e:
            warning("Error in addExtrasWindow", str(e))

    def configureBundleWindow(self,bundleId):

        def addBundleRow(self):
            try:
                row_position=ui.bundleTable.rowCount()
                ui.bundleTable.insertRow(row_position)
                for i in range(0,3):
                    ui.bundleTable.setItem(row_position,i,QTableWidgetItem(""))
            except Exception as e:
                ExceptionHandler.warning("Error in addBundleRow", str(e))


        def removeBundleRow(self):
            try:
                selected= ui.bundleTable.selectedItems()[0].row()
                ui.bundleTable.removeRow(selected)
            except Exception as e:
                ExceptionHandler.warning("Error in removeBundleRow", str(e))

        try:
            window = QDialog()
            ui = Ui_configureBundle()
            ui.setupUi(window)

            ui.addBundle.clicked.connect(addBundleRow)

            ui.removeBundle.clicked.connect(removeBundleRow)

            if(bundleId in globalVariables.bundleData):
                for rows in globalVariables.bundleData[bundleId]:
                    row_position = ui.bundleTable.rowCount()
                    ui.bundleTable.insertRow(row_position)
                    ui.bundleTable.setItem(row_position,0,QTableWidgetItem(globalVariables.bundleData[bundleId][rows]["type"]))
                    ui.bundleTable.setItem(row_position,1,QTableWidgetItem(globalVariables.bundleData[bundleId][rows]["key"]))
                    ui.bundleTable.setItem(row_position,2,QTableWidgetItem(globalVariables.bundleData[bundleId][rows]["value"]))


            tempBundle={}
            if window.exec() == QDialog.Accepted:
                for i in range(0,ui.bundleTable.rowCount()):
                    type=ui.bundleTable.item(i,0)
                    key=ui.bundleTable.item(i,1)
                    if(type and key):
                        if(type.text() != "" and key.text() != ""):
                            tempBundle[i] = {"type":ui.bundleTable.item(i,0).text(),"key":ui.bundleTable.item(i,1).text(),"value":ui.bundleTable.item(i,2).text()}
                        else:
                            ExceptionHandler.warning("Error", str("Type and Keys must have values"))
                            return self.configureBundleWindow(bundleId)
                    else:
                        ExceptionHandler.warning("Error", str("Type and Keys must have values"))
                        return self.configureBundleWindow(bundleId)

                globalVariables.bundleData[bundleId]=tempBundle


        except Exception as e:
            ExceptionHandler.warning("Error in configureBundleWindow", str(e))

    def apkCodeWindow(self):
        def apkCodeGenerate():
            try:
                ui.apkCodeText.clear()
                ui.apkCodeText.append("var intent = Intent()");
                ui.apkCodeText.append("");

                package=MainWindow.getPackageValue(self)
                activity=globalVariables.selectedActivity
                action = globalVariables.action
                data = globalVariables.data


                if(package and activity):
                    ui.apkCodeText.append("intent.setClassName(\""+package+"\", \""+activity+"\")");
                else:
                    print("No package or activity selected")
                if(action):
                    ui.apkCodeText.append("");
                    ui.apkCodeText.append("intent.action = \""+action+"\"");
                if(data):
                    ui.apkCodeText.append("");
                    ui.apkCodeText.append("intent.data = Uri.parse(\""+data+"\")");

                ui.apkCodeText.append(globalVariables.apkCode)

                ui.apkCodeText.append("");
                ui.apkCodeText.append("startActivity(intent)");

            except Exception as e:
                ExceptionHandler.warning("Error in apkCodeGenerate", str(e))

        def apkLaunch():
            try:
                ui.outputText.clear()
                package = globalVariables.packageName

                if(package):
                    result = subprocess.run(["rm", "-rf", "/tmp/ExportHunter_build"], capture_output=False, text=False)
                    if(result.returncode == 1):
                        ui.outputText.append(result.stderr)
                        return
                    ui.outputText.append("[*] /tmp cleared")

                    result = subprocess.run(["unzip", "-o", "helper/baseAPKCode.zip", "-d", "/tmp/ExportHunter_build"], capture_output=True, text=True)
                    if(result.returncode == 1):
                        ui.outputText.append(result.stderr)
                        return
                    ui.outputText.append("[*] Base APK Code extracted to /tmp")

                    with open(globalVariables.tmpCompiledApkPath + "baseMainActivityCode.kt","r") as file:
                        mainActivity = file.read()
                        file.close()

                    apkCode = ui.apkCodeText.toPlainText()
                    mainActivityModified = mainActivity.replace("//CODEREPLACEMENTPLACEHOLDER",apkCode)

                    with open(globalVariables.tmpCompiledApkPath + "app/src/main/java/com/kaal/exporthunter/MainActivity.kt","w") as file:
                        file.write(mainActivityModified)
                        file.close()
                    ui.outputText.append("[*] Main Activity Modified")

                    result = subprocess.run([globalVariables.tmpCompiledApkPath + "gradlew", "-p", globalVariables.tmpCompiledApkPath , "assembleDebug"], capture_output=True, text=True)
                    if(result.returncode == 1):
                        ui.outputText.append(result.stderr)

                    if os.path.exists(globalVariables.tmpCompiledApkPath + "app/build/outputs/apk/debug/app-debug.apk"):
                        ui.outputText.append("[*] APK Creation Succsessfull")
                        result = subprocess.run(["adb", "install", globalVariables.tmpCompiledApkPath + "app/build/outputs/apk/debug/app-debug.apk"], capture_output=True, text=True)
                        if(result.returncode == 1):
                            ui.outputText.append(result.stderr)
                            return
                        if(result.returncode == 0):
                            result = subprocess.run(["adb", "shell", "am", "start", "-n", "com.kaal.exporthunter/.MainActivity"], capture_output=True, text=True)
                            if(result.returncode == 1):
                                ui.outputText.append(result.stderr)
                                return
                        ui.outputText.append("[*] APK installation completed")

                    ui.outputText.append("[*] Launch Tasks completed")
            except Exception as e:
                ExceptionHandler.warning("Error in apkLaunch", str(e))

        try:

            window = QDialog()
            ui = Ui_apkCreate()
            ui.setupUi(window)

            if(globalVariables.apkCode == ""):
                self.generateExtrasCode()
                apkCodeGenerate()
            else:
                ui.apkCodeText.setText(globalVariables.apkCode)

            ui.apkLaunch.clicked.connect(apkLaunch)

            ui.refresh.clicked.connect(lambda: (setattr(globalVariables, "apkCode", ""), apkCodeGenerate()))

            window.exec()

            globalVariables.apkCode= ui.apkCodeText.toPlainText()

        except Exception as e:
            ExceptionHandler.warning("Error in apkCodeWindow", str(e))


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.scrcpy.clicked.connect(self.launchScrcpy)

        # Browse
        self.ui.browse.clicked.connect(self.browseDialog)

        #Double click on Activity
        # self.ui.listExported.addItem("DemoActivity")
        self.ui.listExported.itemDoubleClicked.connect(self.selectActivity)

        #Launch Selected Activity
        self.ui.adbLaunch.clicked.connect(self.adbLaunchActivity)

        #Add Extras
        self.ui.addExtras.clicked.connect(self.addExtrasWindow)

        #Remove Row
        self.ui.removeExtras.clicked.connect(self.removeExtras)

        #apkCodeGenerate
        self.ui.apkCodeGenerate.clicked.connect(self.apkCodeWindow)

        #action change
        self.ui.actionLine.editingFinished.connect(self.getActionValue)

        #data change
        self.ui.dataLine.editingFinished.connect(self.getDataValue)

        #for daster testing
        self.loadJavaClassFile("/tmp/ExportHunter_extract/sources/com/ewmglobal/ewmmobile/settings/SettingsActivity.java")

        self.ui.javaCode.selectionChanged.connect(self.javaCodeSelected)



        # ExceptionHandler.warning("titlie","error")


    def javaCodeSelected(self):
        try:
            globalVariables.searchValues = self.ui.javaCode.textCursor().selectedText()
            # print(globalVariables.searchValues)
            JavaHighlighter(self.ui.javaCode.document())
        except Exception as e:
            ExceptionHandler.warning("Error in launchScrcpy", str(e))


    def launchScrcpy(self):
        try:
            subprocess.Popen("scrcpy")
        except Exception as e:
            ExceptionHandler.warning("Error in launchScrcpy", str(e))

    #get Java Class File Path
    def getJavaClassPath(self, className):
        try:
            javaClassPath = globalVariables.tmpDecompiledApkPath +"sources/"+ className.replace(".","/") +".java"
            return(javaClassPath)
        except Exception as e:
            ExceptionHandler.warning("Error in getJavaClassPath", str(e))

    #load the given java class file
    def loadJavaClassFile(self,classPath):
        try:
            with open(classPath,"r") as file:
                content = file.read()

            self.ui.javaCode.setText(content)
            globalVariables.javaClassCode = content
            JavaHighlighter(self.ui.javaCode.document())

        except Exception as e:
            ExceptionHandler.warning("Error in loadJavaClassFile", str(e))


    #get Package Name
    def getPackageValue(self):
        try:
            #with apktool
            # manifest_path = globalVariables.tmpDecompiledApkPath + "AndroidManifest.xml"

            #with jadx
            manifest_path = globalVariables.tmpDecompiledApkPath + "resources/AndroidManifest.xml"
            if os.path.exists(manifest_path):
                tree = ET.parse(manifest_path)
                root = tree.getroot()
                package_name = root.attrib.get('package')
                globalVariables.packageName = str(package_name)
                return(str(package_name))
            else:
                ExceptionHandler.warning("Error", str("Manifest not found, Browse APK to analyze..."))

        except Exception as e:
            ExceptionHandler.warning("Error in getPackageValue", str(e))

    #get Action Value
    def getActionValue(self):
        try:
            action = self.ui.actionLine.text()
            globalVariables.action = action
            return(str(action))

        except Exception as e:
            ExceptionHandler.warning("Error in getActionValue", str(e))

    #get Data Value
    def getDataValue(self):
        try:
            data = self.ui.dataLine.text()
            globalVariables.data = data
            return(str(data))

        except Exception as e:
            ExceptionHandler.warning( "Error in getDataValue", str(e))


    def browseDialog(self):
        try:
            #Remove this for deployment
            # globalVariables.apkPath, _filter = QFileDialog.getOpenFileName(None, "Open APK File", '/Users/bgajera/Downloads/test/1', "(*.apk)")

            #Use this while deployment
            globalVariables.apkPath, _filter = QFileDialog.getOpenFileName(None, "Open APK File", '', "(*.apk)")
            self.ui.listExported.clear()
            if os.path.exists(globalVariables.apkPath):
                try:
                #Apktool _ Old code
                # command = ["apktool", "d", "-f", apkPath, "-o", globalVariables.tmpDecompiledApkPath ]

                #use Jadx for getting java code also
                    command = ["jadx", "-d", globalVariables.tmpDecompiledApkPath , str(globalVariables.apkPath), "-q","--deobf"]

                    result = subprocess.run(command, capture_output=False, text=True)
                    #with APKtool
                    # globalVariables.manifest_path = "/tmp/ExportHunter_extract/AndroidManifest.xml"

                    #with Jadx
                    globalVariables.manifest_path = globalVariables.tmpDecompiledApkPath + "resources/AndroidManifest.xml"


                    tree = ET.parse(globalVariables.manifest_path)
                    root = tree.getroot()
                    # Find all <activity> tags under <application>
                    activities = root.findall(".//application/activity")
                    # Extract and print the android:name attributes of each activity
                    print("Activities in the AndroidManifest.xml:")
                    for activity in activities:
                        if(activity.attrib.get("{http://schemas.android.com/apk/res/android}exported")) == "true":
                            self.ui.listExported.addItem(activity.attrib.get("{http://schemas.android.com/apk/res/android}name"))

                    self.ui.outputText.setText("Apk Analyzed")
                except Exception as e:
                    ExceptionHandler.warning("Error in browseDialog", str(e))
            else:
                ExceptionHandler.warning("Error", "Select Valid APK")

        except Exception as e:
            ExceptionHandler.warning("Error in browseDialog", str(e))

    def selectActivity(self,item):
        try:
            self.ui.activityText.setText(item.text())
            globalVariables.selectedActivity = str(item.text())
            self.ui.outputText.setText("Activity Selected")

            javaClassPath = self.getJavaClassPath(globalVariables.selectedActivity)
            self.loadJavaClassFile(javaClassPath)

        except Exception as e:
            ExceptionHandler.warning("Error in selectActivity", str(e))


    def generateExtrasCode(self):
        globalVariables.apkCode = ""
        try:
            for i in range(0,self.ui.extrasTable.rowCount()):
                if(self.ui.extrasTable.item(i,0).flags() & Qt.ItemIsEnabled):
                    if(self.ui.extrasTable.item(i,1).text() != ""):
                        # self.ui.apkCodeText.append("intent.putExtra(\""+self.ui.extrasTable.item(i,1).text()+"\", \""+self.ui.extrasTable.item(i,2).text()+"\")")
                        globalVariables.apkCode += "\n"
                        globalVariables.apkCode += "intent.putExtra(\""+self.ui.extrasTable.item(i,1).text()+"\", \""+self.ui.extrasTable.item(i,2).text()+"\")"
                else:
                    bundleId = self.ui.extrasTable.item(i,0).text()

                    if(bundleId in globalVariables.bundleData):
                        if(globalVariables.bundleData[bundleId]):
                            globalVariables.apkCode += "\n"
                            globalVariables.apkCode += "var " + bundleId + "= Bundle()"
                            for rows in globalVariables.bundleData[bundleId]:
                                globalVariables.apkCode += "\n"
                                globalVariables.apkCode += bundleId+".putString(\""+globalVariables.bundleData[bundleId][rows]["key"]+"\", \""+globalVariables.bundleData[bundleId][rows]["value"]+"\")"

                            globalVariables.apkCode += "\nintent.putExtra(\"" + self.ui.extrasTable.item(i,1).text() + "\", "+bundleId+")"

        except Exception as e:
            ExceptionHandler.warning("Error in generateExtrasCode", str(e))

    def adbLaunchActivity(self):
        try:
            globalVariables.packageName = self.getPackageValue()
            self.getActionValue()
            self.getDataValue()
            if(globalVariables.selectedActivity and globalVariables.packageName):
                command = ["adb", "shell", "am", "start"]

                #Get Action
                if(globalVariables.action):
                    command.append("-a")
                    command.append("\""+globalVariables.action+"\"")

                #Get Data
                if(globalVariables.data):
                    command.append("-d")
                    command.append("\""+globalVariables.data+"\"")

                command.append("-n")
                command.append('"'+globalVariables.packageName+'/'+globalVariables.selectedActivity+'"')
                for i in range(0,self.ui.extrasTable.rowCount()):
                    if(self.ui.extrasTable.item(i,0).flags() & Qt.ItemIsEnabled):
                        if(self.ui.extrasTable.item(i,0).text() != "" and self.ui.extrasTable.item(i,1).text() != "" and self.ui.extrasTable.item(i,2).text() !=""):
                            command.append("\""+self.ui.extrasTable.item(i,0).text()+"\"")
                            command.append("\""+self.ui.extrasTable.item(i,1).text()+"\"")
                            command.append("\""+self.ui.extrasTable.item(i,2).text()+"\"")
                print(command)

                result = subprocess.run(command, capture_output=True, text=True)
                self.ui.outputText.setText(result.stdout)
                if(result.returncode == 1):
                    self.ui.outputText.setText(result.stderr)
            else:
                ExceptionHandler.warning("Error", "No Activities Selected")

        except Exception as e:
            ExceptionHandler.warning("Error in adbLaunchActivity", str(e))

    def removeExtras(self):
        try:
            selected= self.ui.extrasTable.selectedItems()[0].row()
            if(self.ui.extrasTable.item(selected,0).flags() & Qt.ItemIsEnabled):
                self.ui.extrasTable.removeRow(selected)
            else:
                globalVariables.bundleData.pop(self.ui.extrasTable.item(selected,0).text(),None)
                self.ui.extrasTable.removeRow(selected)

        except IndexError:
            ExceptionHandler.warning("Error", "Nothing Selected")
        except Exception as e:
            ExceptionHandler.warning("Error in removeExtras", str(e))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
