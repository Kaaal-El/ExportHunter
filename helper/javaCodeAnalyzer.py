# This Python file uses the following encoding: utf-8
import re
import helper.globalVariables as globalVariables
from helper.ExceptionHandler import ExceptionHandler

# if __name__ == "__main__":
#     pass
class javaCodeAnalyzer():
    def __init__():
        print()

    def getListOfMethods():
        try:

            method_pattern = re.compile(r'\b(?:public|private|protected|static|final|\s)+\s*[\w\<\>\[\]]+\s+(\w+)\s*\(.*\)\s*{')

            methods = []
            javaCode = globalVariables.javaClassCode
            matches = method_pattern.findall(javaCode)
            return(matches)

        except Exception as e:
            ExceptionHandler.warning("Error in getListOfMethods", str(e))
