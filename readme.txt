The provided code consists of an ANTLR grammar (`Calculadora.g4`) for defining a calculator language and a corresponding listener class (`CalculadoraListener`) in Python. Let's break down each part and explain its functionality:

### ANTLR Grammar (`Calculadora.g4`)

1. **Grammar Definition**: Defines the syntax and rules of the calculator language using ANTLR grammar notation.

2. **Lexer Rules**:
   - `NUMBER`, `INTEGER`: Define rules for recognizing numbers and integers.
   - `SUM`, `SUBTRACTION`, `MULTIPLY`, `DIVISION`, `INTEGER_DIVISION`, `MODULO`, `POTENTIATION`: Define tokens for arithmetic operators.
   - `RES`, `MEM`: Define tokens for memory access operations.
   - `ENTER`: Define token for newline character.
   - `WS`: Define rule for skipping whitespaces.

3. **Parser Rules**:
   - `start`: Defines the start rule for parsing.
   - `line`, `expression`, `res`, `mem`: Define parser rules for different types of expressions.

### Listener Class (`CalculadoraListener`)

1. **Initialization**: Initializes the listener class with attributes `stack`, `stackFile`, and `memory` to track intermediate results, file contents, and memory value.

2. **Arithmetic Operation Resolution**: Implements the `resolve` method to perform arithmetic operations (`+, -, *, /, //, %, ^`) and handle special cases such as division by zero or negative exponents.

3. **Methods for Parse Tree Events**:
   - `enterStart`, `exitStart`: Define entry and exit points for the start rule.
   - `enterLine`, `exitLine`: Define entry and exit points for the line rule, handling the stack operations for each line.
   - `enterExpression`, `exitExpression`: Define entry and exit points for the expression rule, handling arithmetic operations and value pushes onto the stack.
   - `enterRes`, `exitRes`: Define entry and exit points for the res rule, handling memory retrieval from the file stack.
   - `enterMem`, `exitMem`: Define entry and exit points for the mem rule, handling memory storage and retrieval operations.

4. **Error Handling**: Raises exceptions for invalid memory access or arithmetic operations.

### Overall Functionality:
- The ANTLR grammar defines the syntax of the calculator language.
- The listener class parses the input using ANTLR-generated parser and processes arithmetic operations and memory access based on the parse tree events.
- It maintains a stack to evaluate expressions and tracks memory operations using a separate file stack.

### Explanation:
The provided code defines a calculator language and a listener class in Python using ANTLR. The grammar specifies the syntax, while the listener class processes input expressions and memory operations based on parse tree events.

### Class:
Construction of Interpreters