BEST_PRACTICE = list([
    'android.xml',
    'CallSuperFirst',
    'CallSuperLast',
    'DoNotHardCodeSDCard',
    'AvoidUsingHardCodedIP',
    'BigIntegerInstantiation',
    'AssignmentInOperand',
    'AvoidFinalLocalVariable',
    'AvoidLiteralsInIfCondition',
    'AvoidUsingNativeCode',
    'AvoidUsingShortType',
    'AvoidUsingVolatile',
    'BooleanInversion',
    'DoNotCallGarbageCollectionExplicitly',
    'OneDeclarationPerLine',
    'OnlyOneReturn',
    'AvoidReassigningParameters',
    'ClassWithOnlyPrivateConstructorsShouldBeFinal',
    'ConfusingTernary',
    'DefaultLabelNotLastInSwitchStmt',
    'FieldDeclarationsShouldBeAtStartOfClass',
    'FinalFieldCouldBeStatic',
    'ImmutableField',
    'OptimizableToArrayCall',
    'ReturnEmptyArrayRatherThanNull',
    'SingularField',
    'UseCollectionIsEmpty',
    'UseVarargs',
    'UnnecessaryFullyQualifiedName',
    'DoNotCallSystemExit',
    'StaticEJBFieldShouldBeFinal',
    'javabeans.xml',
    'BeanMembersShouldSerialize',
    'MissingSerialVersionUID',
    'JUnitAssertionsShouldIncludeMessage',
    'JUnitStaticSuite',
    'JUnitTestContainsTooManyAsserts',
    'JUnitTestsShouldIncludeAssert',
    'UseAssertEqualsInsteadOfAssertTrue',
    'UseAssertNullInsteadOfAssertTrue',
    'UseAssertSameInsteadOfAssertTrue',
    'UseAssertTrueInsteadOfAssertEquals',
    'GuardDebugLogging',
    'GuardLogStatement',
    'ProperLogger',
    'GuardLogStatementJavaUtil',
    'LoggerIsNotStaticFinal',
    'MoreThanOneLogger',
    'SystemPrintln',
    'AddEmptyString',
    'AvoidArrayLoops',
    'AvoidInstantiatingObjectsInLoops',
    'LocalVariableCouldBeFinal',
    'MethodArgumentCouldBeFinal',
    'SimplifyStartsWith',
    'UseArrayListInsteadOfVector',
    'UseArraysAsList',
    'UseStringBufferForStringAppends',
    'AppendCharacterWithChar',
    'AvoidStringBufferField',
    'ConsecutiveAppendsShouldReuse',
    'ConsecutiveLiteralAppends',
    'InefficientEmptyStringCheck',
    'InefficientStringBuffering',
    'InsufficientStringBufferDeclaration',
    'StringBufferInstantiationWithChar',
    'StringInstantiation',
    'UnnecessaryCaseChange',
    'UseIndexOfChar',
    'UseStringBufferLength',
    'ArrayIsStoredDirectly',
    'LooseCoupling'
])

CHECK = list([
    'CheckResultSet',
    'CheckSkipResult'
])

CODE_STRUCTURE = list([
    'DontImportSun',
    'DontImportJavaLang',
    'TooManyStaticImports',
    'UnusedImports'
])

CONCURRENCY = list([
    'AvoidThreadGroup',
    'DontCallThreadRun',
    'DoubleCheckedLocking',
    'UseConcurrentHashMap',
    'AvoidSynchronizedAtMethodLevel',
    'NonThreadSafeSingleton',
    'UnsynchronizedStaticDateFormatter',
    'UseNotifyAllInsteadOfNotify',
    'DoNotUseThreads',
    'UseProperClassLoader'
])

DOCUMENTATION_CONVENTIONS = list([
    'comments.xml',
    'CommentContent',
    'CommentRequired',
    # ADDED 14.07.2018 - https://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/comments.html
    'CommentDefaultAccessModifier'
])

ERROR_HANDLING = list([
    'ReturnFromFinallyBlock',
    'AvoidInstanceofChecksInCatchClause',
    'PreserveStackTrace',
    'UseCorrectExceptionLogging',
    'AvoidPrintStackTrace',
    'strictexception.xml',
    'AvoidCatchingGenericException',
    'AvoidCatchingNPE',
    'AvoidCatchingThrowable',
    'AvoidLosingExceptionInformation',
    'AvoidRethrowingException',
    'AvoidThrowingNewInstanceOfSameException',
    'AvoidThrowingNullPointerException',
    'AvoidThrowingRawExceptionTypes',
    'DoNotExtendJavaLangError',
    'DoNotThrowExceptionInFinally',
    'ExceptionAsFlowControl',
    'SignatureDeclareThrowsException',
    'SignatureDeclareThrowsException'
])

INTERFACE = list([
    'ClassCastExceptionWithToArray',
    'OverrideBothEqualsAndHashcode',
    'clone.xml',
    'CloneMethodMustImplementCloneable',
    'CloneThrowsCloneNotSupportedException',
    'ProperCloneImplementation',
    'AtLeastOneConstructor',
    'AbstractClassWithoutAbstractMethod',
    'AbstractClassWithoutAnyMethod',
    'AccessorClassGeneration',
    'ConstructorCallsOverridableMethod',
    'EmptyMethodInAbstractClassShouldBeAbstract',
    'MissingStaticMethodInNonInstantiatableClass',
    'NonStaticInitializer',
    'SimpleDateFormatNeedsLocale',
    'UseLocaleWithCaseConversions',
    'FinalizeDoesNotCallSuperFinalize',
    'FinalizeOverloaded',
    'FinalizeShouldBeProtected',
    'MethodReturnsInternalArray',
    'CloneMethodMustImplementCloneable'
])

LOGIC = list([
    'AvoidBranchingStatementAsLastInLoop',
    'AvoidMultipleUnaryOperators',
    'BrokenNullCheck',
    'JumbledIncrementer',
    'MisplacedNullCheck',
    'UnusedNullCheckInEquals',
    'SuspiciousOctalEscape',
    'BadComparison',
    'CompareObjectsWithEquals',
    'EqualsNull',
    'MissingBreakInSwitch',
    'NonCaseLabelInSwitchStatement',
    'PositionLiteralsFirstInCaseInsensitiveComparisons',
    'PositionLiteralsFirstInComparisons',
    'SwitchStmtsShouldHaveDefault',
    'UseEqualsToCompareStrings'
])

METRIC = list([
    'codesize.xml',
    'CyclomaticComplexity',
    'ExcessiveClassLength',
    'ExcessiveMethodLength',
    'ExcessiveParameterList',
    'ExcessivePublicCount',
    'ModifiedCyclomaticComplexity',
    'NcssConstructorCount',
    'NcssMethodCount',
    'NcssTypeCount',
    'NPathComplexity',
    'StdCyclomaticComplexity',
    'TooManyFields',
    'TooManyMethods',
    'CommentSize',
    'CouplingBetweenObjects',
    'ExcessiveImports',
    'AvoidDeeplyNestedIfStmts',
    'GodClass',
    'SwitchDensity',
    'TooFewBranchesForASwitchStatement'
])

MIGRATION = list([
    'migrating.xml',
    'AvoidAssertAsIdentifier',
    'AvoidEnumAsIdentifier',
    'ByteInstantiation',
    'IntegerInstantiation',
    'JUnit4SuitesShouldUseSuiteAnnotation',
    'JUnit4TestShouldUseAfterAnnotation',
    'JUnit4TestShouldUseBeforeAnnotation',
    'JUnit4TestShouldUseTestAnnotation',
    'JUnitUseExpected',
    'LongInstantiation',
    'ReplaceEnumerationWithIterator',
    'ReplaceHashtableWithMap',
    'ReplaceVectorWithList',
    'ShortInstantiation',
    'migrating_to_13.xml',
    'migrating_to_14.xml',
    'migrating_to_15.xml',
    'migrating_to_junit4.xml'
])

MULTIPLE = list([
    'basic.xml',
    'controversial.xml',
    'coupling.xml',
    'design.xml',
    'finalizers.xml',
    'imports.xml',
    'j2ee.xml',
    'junit.xml',
    'logging-jakarta-commons.xml',
    'logging-java.xml',
    'optimizations.xml',
    'strings.xml',
    'sunsecure.xml',
    'typeresolution.xml'
])

NAMING_CONVENTIONS = list([
    'AvoidPrefixingMethodParameters',
    'LocalHomeNamingConvention',
    'LocalInterfaceSessionNamingConvention',
    'MDBAndSessionBeanNamingConvention',
    'RemoteInterfaceNamingConvention',
    'RemoteSessionInterfaceNamingConvention',
    'JUnitSpelling',
    'TestClassWithoutTestCases',
    'naming.xml',
    'AbstractNaming',
    'AvoidDollarSigns',
    'AvoidFieldNameMatchingMethodName',
    'AvoidFieldNameMatchingTypeName',
    'AvoidNonConstructorMethodsWithClassName',
    'BooleanGetMethodName',
    'ClassNamingConventions',
    'ConstantNamingConventions',
    'ConstructorWithNameAsEnclosingClass',
    'GenericsNaming',
    'LongVariable',
    'MethodNamingConventions',
    'MethodWithSameNameAsEnclosingClass',
    'MisleadingVariableName',
    'NoPackage',
    'PackageCase',
    'ShortClassName',
    'ShortMethodName',
    'ShortVariable',
    'SuspiciousConstantFieldName',
    'SuspiciousEqualsMethodName',
    'SuspiciousHashcodeMethodName',
    'VariableNamingConventions'
])

OBJECT_ORIENTED_DESING = list([
    'ExtendsObject',
    'AvoidAccessibilityAlteration',
    'CallSuperInConstructor',
    'DefaultPackage',
    'UseObjectForClearerAPI',
    'LawOfDemeter',
    'LooseCoupling',
    'LoosePackageCoupling',
    'AvoidConstantsInterface',
    'AvoidProtectedFieldInFinalClass',
    'AvoidProtectedMethodInFinalClassNotExtending',
    'InstantiationToGetClass',
    'UseUtilityClass'
])

REFACTORINGS_REDUNDANCIES = list([
    'EmptyCatchBlock',
    'EmptyFinallyBlock',
    'EmptyIfStmt',
    'EmptyInitializer',
    'EmptyStatementBlock',
    'EmptyStatementNotInLoop',
    'EmptyStaticInitializer',
    'EmptySwitchStatements',
    'EmptySynchronizedBlock',
    'EmptyTryBlock',
    'EmptyWhileStmt',
    'UnconditionalIfStatement',
    'UnnecessaryConversionTemporary',
    'UnnecessaryFinalModifier',
    'UnnecessaryReturn',
    'UselessOperationOnImmutable',
    'UselessOverridingMethod',
    'UselessParentheses',
    'NullAssignment',
    'UnnecessaryConstructor',
    'UnnecessaryParentheses',
    'IdempotentOperations',
    'UncommentedEmptyConstructor',
    'UncommentedEmptyMethod',
    'UncommentedEmptyMethodBody',
    'UnnecessaryLocalBeforeReturn',
    'empty.xml',
    'EmptyCatchBlock',
    'EmptyFinallyBlock',
    'EmptyIfStmt',
    'EmptyInitializer',
    'EmptyStatementBlock',
    'EmptyStatementNotInLoop',
    'EmptyStaticInitializer',
    'EmptySwitchStatements',
    'EmptySynchronizedBlock',
    'EmptyTryBlock',
    'EmptyWhileStmt',
    'EmptyFinalizer',
    'FinalizeOnlyCallsSuperFinalize',
    'DuplicateImports',
    'ImportFromSamePackage',
    'UnusedImports',
    'UnnecessaryBooleanAssertion',
    'PrematureDeclaration',
    'RedundantFieldInitializer',
    'UnnecessaryWrapperObjectCreation',
    'AvoidDuplicateLiterals',
    'StringToString',
    'UselessStringValueOf',
    'unnecessary.xml',
    'UnnecessaryConversionTemporary',
    'UnnecessaryFinalModifier',
    'UnnecessaryReturn',
    'UnusedNullCheckInEquals',
    'UselessOperationOnImmutable',
    'UselessOverridingMethod',
    'UselessParentheses',
    'unusedcode.xml',
    'UnusedFormalParameter',
    'UnusedLocalVariable',
    'UnusedModifier',
    'UnusedPrivateField',
    'UnusedPrivateMethod'
])
REFACTORINGS_SIMPLIFICATIONS = list([
    'BooleanInstantiation',
    'CollapsibleIfStatements',
    'ForLoopShouldBeWhileLoop',
    'LogicInversion',
    'SimplifyBooleanExpressions',
    'SimplifyBooleanReturns',
    'SimplifyConditional',
    'SimplifyBooleanAssertion'
])

RESOURCE = list([
    'AvoidDecimalLiteralsInBigDecimalConstructor',
    'AvoidUsingOctalValues',
    'DontUseFloatTypeForLoopIndices',
    'DataflowAnomalyAnalysis',
    'AssignmentToNonFinalStatic',
    'CloseResource',
    'AvoidCallingFinalize'
])

STYLE_CONVENTIONS = list([
    'braces.xml',
    'ForLoopsMustUseBraces',
    'IfElseStmtsMustUseBraces',
    'IfStmtsMustUseBraces',
    'WhileLoopsMustUseBraces'
])
