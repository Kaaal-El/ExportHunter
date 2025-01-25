# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

numberOfBundles = 0
# bundleData = {"bundleName":{"0",{"type":"","key":"","value":""}}}
bundleData = {}

apkPath = ""
manifest_path = ""

tmpDecompiledApkPath = "/tmp/ExportHunter_extract/"
tmpCompiledApkPath ="/tmp/ExportHunter_build/"

javaClassCode = ""
selectedActivity = ""
action = ""
data = ""
packageName = ""

apkCode = ""


#for Highlighting
keywords = [
   "_", "abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class",
   "const", "continue", "default", "do", "double", "else", "enum", "extends", "false", "final",
   "finally", "float", "for", "goto", "if", "implements", "import", "instanceof", "int",
   "interface", "long", "native", "new", "null", "package", "private", "protected", "public",
   "return", "short", "static", "strictfp", "super", "switch", "synchronized", "this", "throw",
   "throws", "transient", "true", "try", "void", "volatile", "while"
]

builtInTypes = [
    "byte","short","int","long","float","double","char","boolean"
]

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

extrasTypesValues = [
"getIntExtra","getLongExtra","getFloatExtra","getDoubleExtra","getBooleanExtra","getByteExtra","getCharExtra","getShortExtra","getStringExtra","getCharSequenceExtra","getIntArrayExtra","getLongArrayExtra","getFloatArrayExtra","getDoubleArrayExtra","getBooleanArrayExtra","getByteArrayExtra","getCharArrayExtra","getShortArrayExtra","getStringArrayExtra","getCharSequenceArrayExtra","getParcelableExtra","getParcelableArrayExtra","getParcelableArrayListExtra","getSerializableExtra","getBundleExtra","getSparseParcelableArrayExtra","getIntegerArrayListExtra","getStringArrayListExtra","getCharSequenceArrayListExtra","getExtras","hasExtra",

"getInt","getLong","getFloat","getDouble","getBoolean","getByte","getChar","getShort","getString","getCharSequence","getIntArray","getLongArray","getFloatArray","getDoubleArray","getBooleanArray","getByteArray","getCharArray","getShortArray","getStringArray","getCharSequenceArray","getParcelable","getParcelableArray","getParcelableArrayList","getSerializable","getBundle","getSparseParcelableArray","getIntegerArrayList","getStringArrayList","getCharSequenceArrayList"
]


searchValues=""






