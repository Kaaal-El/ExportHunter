# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QTextCharFormat, QColor, QFont, QSyntaxHighlighter
from helper.ExceptionHandler import ExceptionHandler
from PySide6.QtCore import QRegularExpression
import helper.globalVariables as globalVariables

class JavaHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        try:
            super().__init__(document)  # This ensures that QSyntaxHighlighter is initialized correctly
            self.highlightingRules = []

            # Define the keyword format
            keywordFormat = QTextCharFormat()
            keywordFormat.setForeground(QColor("#0000FF"))  # Orange
            keywordFormat.setFontWeight(QFont.Bold)


            for keyword in globalVariables.keywords:
                self.highlightingRules.append((r"\b" + keyword + r"\b", keywordFormat))  # Apply word boundary

            # String formatting (Strings enclosed in double quotes)
            stringFormat = QTextCharFormat()
            stringFormat.setForeground(QColor("#C71585"))  # Pink for strings
            self.highlightingRules.append((r'"([^"\\]|\\.)*"', stringFormat))  # Strings between double quotes

            # Single-line comment formatting
            singleLineCommentFormat = QTextCharFormat()
            singleLineCommentFormat.setForeground(QColor("#006400"))  # Green for comments
            self.highlightingRules.append(("//[^\n]*", singleLineCommentFormat))

            # Multi-line comment formatting
            multiLineCommentFormat = QTextCharFormat()
            multiLineCommentFormat.setForeground(QColor("#006400"))  # Green for comments
            self.commentStartExpression = QRegularExpression(r"/\*")
            self.commentEndExpression = QRegularExpression(r"\*/")
            self.multiLineCommentFormat = multiLineCommentFormat

            # Brackets coloring
            bracketFormat = QTextCharFormat()
            bracketFormat.setForeground(QColor("#FF0000"))  # Red
            self.highlightingRules.append((r"\{|\}|\(|\)", bracketFormat))

            # Highlight built-in return types (Boolean, File, etc.) using the same woody
            builtInTypeFormat = QTextCharFormat()
            builtInTypeFormat.setForeground(QColor("#328277"))  # Same woody  color
            builtInTypeFormat.setFontWeight(QFont.Bold)
            for builtInType in globalVariables.builtInTypes:
                self.highlightingRules.append((r"\b" + builtInType + r"\b", builtInTypeFormat))

            # Highlight java.util  types (Boolean, etc.) using the  woody
            utilTypeFormat = QTextCharFormat()
            utilTypeFormat.setForeground(QColor("#8B4513"))  # Same woody  color

            for utilTypes in globalVariables.utilTypes:
                self.highlightingRules.append((r"\b" + utilTypes + r"\b", utilTypeFormat))



            #Intent/Bundle Coloring
            extrasTypeFormat = QTextCharFormat()
            extrasTypeFormat.setBackground(QColor("yellow"))  # Same yello  color
            # extrasTypeFormat.setFontWeight(QFont.Bold)
            extrasTypes = [
            "getIntent","getBundle","getExtras","hasExtras"
            ]
            for extrasTypes in extrasTypes:
                self.highlightingRules.append((r"\b" + extrasTypes + r"\b", extrasTypeFormat))

            #Intent/Bundle Coloring
            extrasValueTypeFormat = QTextCharFormat()
            extrasValueTypeFormat.setBackground(QColor("#FF8080"))#  red  color
            # extrasValueTypeFormat.setFontWeight(QFont.Bold)
            for extrasTypesValues in globalVariables.extrasTypesValues:
                self.highlightingRules.append((r"\b" + extrasTypesValues + r"\b", extrasValueTypeFormat))

            #Search call
            searchFormat = QTextCharFormat()
            searchFormat.setBackground(QColor("#9CCCFC"))#  red  color
            # extrasValueTypeFormat.setFontWeight(QFont.Bold)
            if(globalVariables.searchValues!=""):
                self.highlightingRules.append((r"\b" + globalVariables.searchValues + r"\b", searchFormat))




        except Exception as e:
            ExceptionHandler.warning("Error in getListOfMethods", str(e))






    def highlightBlock(self, text):
        try:
            """Highlight the block of text with matching rules."""
            for pattern, format in self.highlightingRules:
                expression = QRegularExpression(pattern)
                match = expression.match(text)
                while match.hasMatch():
                    self.setFormat(match.capturedStart(), match.capturedLength(), format)
                    match = expression.match(text, match.capturedEnd())

            # Handle multi-line comments
            self.setCurrentBlockState(0)  # Reset block state
            startIndex = 0
            if self.previousBlockState() != 1:
                match = self.commentStartExpression.match(text)
                startIndex = match.capturedStart() if match.hasMatch() else -1

            while startIndex >= 0:
                match = self.commentEndExpression.match(text, startIndex)
                endIndex = match.capturedStart()
                commentLength = 0
                if endIndex == -1:
                    self.setCurrentBlockState(1)
                    commentLength = len(text) - startIndex
                else:
                    commentLength = endIndex - startIndex + match.capturedLength()
                self.setFormat(startIndex, commentLength, self.multiLineCommentFormat)
                startIndex = self.commentStartExpression.match(text, startIndex + commentLength).capturedStart()
        except Exception as e:
            ExceptionHandler.warning("Error in getListOfMethods", str(e))
