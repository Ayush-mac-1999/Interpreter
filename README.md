# **Python Interpreter for a Simple Programming Language**

## **Project Overview**
This project implements a fully functional Python-based interpreter for a simplified programming language. The interpreter processes source code by tokenizing input, building an Abstract Syntax Tree (AST), and executing the parsed instructions. It provides a hands-on understanding of core interpreter concepts, including lexical analysis, parsing, and AST-based execution.

The project is being developed as part of the **CS 609: Final Project Assignment** Southeast Missouri State University and adheres to the requirements outlined in the project guidelines.  

---

## **Features**
1. **Variable Assignments**  
   - Supports declaring and initializing variables.  
   - Example:  
     ```python
     let a = 5;
     let b = a + 3;
     ```

2. **Arithmetic Operations**  
   - Handles addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).  
   - Example:  
     ```python
     let c = a * b;
     ```

3. **Output Printing**  
   - Prints variable values using the `print` statement.  
   - Example:  
     ```python
     print(a);
     print(c);
     ```

4. **Sequential Statements**  
   - Parses and executes multiple statements in order.  
   - Example:  
     ```python
     let x = 10;
     let y = x * 2;
     print(x);
     print(y);
     ```

5. **Whitespace and Semicolon Handling**  
   - Ignores whitespace and requires semicolons (`;`) to separate statements.  

---

## **Project Structure**
1. **`lexer.py`**  
   - Tokenizes the source code into meaningful symbols such as keywords, identifiers, numbers, and operators.  
2. **`parser.py`**  
   - Builds an Abstract Syntax Tree (AST) from tokens to represent the program's hierarchical structure.  
3. **`ast_nodes.py`**  
   - Defines classes for AST nodes, including `AssignNode`, `BinOpNode`, and `PrintNode`.  
4. **`interpreter.py`**  
   - Traverses the AST and executes operations such as variable assignments, arithmetic computations, and print commands.  
5. **`examples/`**  
   - Contains sample programs and test cases demonstrating the interpreter’s functionality.  

---

## **How to Run**
### **Prerequisites**
- Python 3.7 or higher.  

### **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/parastiware/Interpreter.git
   cd interpreter
   ```
2. Write a sample program in the input format, such as:
    ```python
    let x = 10 + 5;
    let y = x * 2;
    print(x);
    print(y);
    ```
    Save it in a file (e.g., program.txt).
3. Run the interpreter:
    ```bash
    python main.py program.txt
    ```