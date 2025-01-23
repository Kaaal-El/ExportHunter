# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QTextCharFormat, QColor, QFont, QSyntaxHighlighter

from PySide6.QtCore import QRegularExpression

class JavaHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)  # This ensures that QSyntaxHighlighter is initialized correctly
        self.highlightingRules = []

        # Define the keyword format
        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor("#0000FF"))  # Orange
        keywordFormat.setFontWeight(QFont.Bold)
        keywords = [
           "_", "abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class",
           "const", "continue", "default", "do", "double", "else", "enum", "extends", "false", "final",
           "finally", "float", "for", "goto", "if", "implements", "import", "instanceof", "int",
           "interface", "long", "native", "new", "null", "package", "private", "protected", "public",
           "return", "short", "static", "strictfp", "super", "switch", "synchronized", "this", "throw",
           "throws", "transient", "true", "try", "void", "volatile", "while"
        ]

        for keyword in keywords:
            self.highlightingRules.append((r"\b" + keyword + r"\b", keywordFormat))  # Apply word boundary

        # String formatting (Strings enclosed in double quotes)
        stringFormat = QTextCharFormat()
        stringFormat.setForeground(QColor("#C71585"))  # Pink for strings
        self.highlightingRules.append(("\".*\"", stringFormat))  # Strings between double quotes

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
        builtInTypes = [
            "byte","short","int","long","float","double","char","boolean"
        ]
        for builtInType in builtInTypes:
            self.highlightingRules.append((r"\b" + builtInType + r"\b", builtInTypeFormat))

        # Highlight java.util  types (Boolean, etc.) using the  woody
        utilTypeFormat = QTextCharFormat()
        utilTypeFormat.setForeground(QColor("#8B4513"))  # Same woody  color
        utilTypes = [
            "AbstractCollection","AbstractList","AbstractMap","AbstractQueue","AbstractSequentialList",
            "AbstractSet","ArrayDeque","ArrayList","Arrays","BitSet","Calendar","Collections","Currency",
            "Date","Dictionary","EnumMap","EnumSet","EventListenerProxy","EventObject","FormattableFlags",
            "Formatter","GregorianCalendar","HashMap","HashSet","Hashtable","IdentityHashMap",
            "LinkedHashMap","LinkedHashSet","LinkedList","ListResourceBundle","Locale","Objects",
            "Observable","PriorityQueue","Properties","PropertyPermission","PropertyResourceBundle",
            "Random","ResourceBundle","Scanner","ServiceLoader","SimpleTimeZone","Stack","StringTokenizer",
            "Timer","TimerTask","TimeZone","TreeMap","TreeSet","UUID","Vector","WeakHashMap",
            "BufferedInputStream","BufferedOutputStream","BufferedReader","BufferedWriter",
            "ByteArrayInputStream","ByteArrayOutputStream","CharArrayReader","CharArrayWriter",
            "Console","DataInputStream","DataOutputStream","File","FileDescriptor","FileInputStream",
            "FileOutputStream","FilePermission","FileReader","FileWriter","FilterInputStream",
            "FilterOutputStream","FilterReader","FilterWriter","InputStream","InputStreamReader",
            "LineNumberInputStream","LineNumberReader","ObjectInputStream","ObjectInputStream.GetField",
            "ObjectOutputStream","ObjectOutputStream.PutField","ObjectStreamClass","ObjectStreamField",
            "OutputStream","OutputStreamWriter","PipedInputStream","PipedOutputStream","PipedReader",
            "PipedWriter","PrintStream","PrintWriter","PushbackInputStream","PushbackReader",
            "RandomAccessFile","Reader","SequenceInputStream","SerializablePermission","StreamTokenizer",
            "StringBufferInputStream","StringReader","StringWriter","Writer", "String",

            "AclNotFoundException", "ActivationException", "AlreadyBoundException", "ApplicationException",
            "AWTException", "BackingStoreException", "BadAttributeValueExpException", "BadBinaryOpValueExpException",
            "BadLocationException", "BadStringOperationException", "BrokenBarrierException", "CertificateException",
            "CloneNotSupportedException", "DataFormatException", "DatatypeConfigurationException", "DestroyFailedException",
            "ExecutionException", "ExpandVetoException", "FontFormatException", "GeneralSecurityException", "GSSException",
            "IllegalClassFormatException", "InterruptedException", "IntrospectionException", "InvalidApplicationException",
            "InvalidMidiDataException", "InvalidPreferencesFormatException", "InvalidTargetObjectTypeException",
            "IOException", "JAXBException", "JMException", "KeySelectorException", "LambdaConversionException",
            "LastOwnerException", "LineUnavailableException", "MarshalException", "MidiUnavailableException",
            "MimeTypeParseException", "MimeTypeParseException", "NamingException", "NoninvertibleTransformException",
            "NotBoundException", "NotOwnerException", "ParseException", "ParserConfigurationException",
            "PrinterException", "PrintException", "PrivilegedActionException", "PropertyVetoException",
            "ReflectiveOperationException", "RefreshFailedException", "RemarshalException", "RuntimeException",
            "SAXException", "ScriptException", "ServerNotActiveException", "SOAPException", "SQLException",
            "TimeoutException", "TooManyListenersException", "TransformerException", "TransformException",
            "UnmodifiableClassException", "UnsupportedAudioFileException", "UnsupportedCallbackException",
            "UnsupportedFlavorException", "UnsupportedLookAndFeelException", "URIReferenceException",
            "URISyntaxException", "UserException", "XAException", "XMLParseException", "XMLSignatureException",
            "XMLStreamException", "XPathException",

            "AnnotationTypeMismatchException", "ArithmeticException", "ArrayStoreException",
            "BufferOverflowException", "BufferUnderflowException", "CannotRedoException",
            "CannotUndoException", "ClassCastException", "CMMException", "CompletionException",
            "ConcurrentModificationException", "DataBindingException", "DateTimeException", "DOMException",
            "EmptyStackException", "EnumConstantNotPresentException", "EventException",
            "FileSystemAlreadyExistsException", "FileSystemNotFoundException", "IllegalArgumentException",
            "IllegalMonitorStateException", "IllegalPathStateException", "IllegalStateException",
            "IllformedLocaleException", "ImagingOpException", "IncompleteAnnotationException",
            "IndexOutOfBoundsException", "JMRuntimeException", "LSException", "MalformedParameterizedTypeException",
            "MalformedParametersException", "MirroredTypesException", "MissingResourceException",
            "NegativeArraySizeException", "NoSuchElementException", "NoSuchMechanismException",
            "NullPointerException", "ProfileDataException", "ProviderException", "ProviderNotFoundException",
            "RasterFormatException", "RejectedExecutionException", "SecurityException", "SystemException",
            "TypeConstraintException", "TypeNotPresentException", "UncheckedIOException", "UndeclaredThrowableException",
            "UnknownEntityException", "UnmodifiableSetException", "UnsupportedOperationException",
            "WebServiceException", "WrongMethodTypeException"

        ]
        for utilTypes in utilTypes:
            self.highlightingRules.append((r"\b" + utilTypes + r"\b", utilTypeFormat))




    def highlightBlock(self, text):
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
