# This Python file uses the following encoding: utf-8
import re
import helper.globalVariables as globalVariables
# if __name__ == "__main__":
#     pass
class javaCodeAnalyzer():
    def __init__():
        print(1)
    def getListOfMethods():
        try:

            method_pattern = re.compile(r'\b(?:public|private|protected|static|final|\s)+\s*[\w\<\>\[\]]+\s+(\w+)\s*\(.*\)\s*{')

            methods = []
            javaCode = globalVariables.javaClassCode
            matches = method_pattern.findall(javaCode)
            return(matches)

        except Exception as e:
            QMessageBox.warning(self, "Error in getListOfMethods", str(e))
