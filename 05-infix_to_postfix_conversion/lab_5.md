# **Stack Application: Conversion from Infix to Postfix**

**Infix notation**, operators are written in-between their operands. This is the most common way of writing expressions that we use in everyday mathematics.

Example: For an addition of two numbers A and B, the infix notation would be A + B.
  
- **Operator Precedence**: For example, in the expression 3 + 4 * 5, MDAS rules apply unless parentheses are used to alter this order.
  
- **Parentheses**: Parentheses are often used to explicitly specify the order of operations.

**Postfix notation** (also known as Reverse Polish Notation, RPN): operators are written after their operands.

Example: For the same operation A + B, the postfix notation would be A B +.
  
- **No Need for Parentheses**: Postfix notation is widely used in computer science because of its straightforward and parenthesis-free syntax.

---

### **Precondition**

An expression of the form `<a> <operator> <b>`

### **Postcondition**

The algorithm should return the equivalent expression `<a> <b> <operator>`

| **Infix Expression** | **Postfix Expression** |
| -------------------- | ---------------------- |
| a + b                | a b +                  |
| a - b                | a b -                  |
| a + b * c            | a b c * +              |
| (a + b) * (c + d)    | a b + c d + * *        |

---

## **Order of Precedence**

| Operator | Priority | Property         | Example                              |
|----------|----------|------------------|--------------------------------------|
| ^        | 3        | Right Associative | a^b^c = a^(b^c)                      |
| * /      | 2        | Left Associative  | a/b/c = (a/b)/c                       |
| + -      | 1        | Left Associative  | a - b - c = (a - b) - c              |

---

## **Example**:
Let's convert the infix expression

1. (A+B+C)*D to postfix:
2. A * (B + C) / D to postfix:
3. (A * (B + C)) to postfix:

---

### **Example**:
Let's convert the infix expression A * (B + C) / D to postfix:

1. A is an operand, output: A.
2. '*' is pushed to the ops stack.
3. '(' is pushed to the ops stack.
4. B is an operand, output: A B.
5. '+' is an operand, output: A B +.
6. C is an operand, output: A B C.
7. ')' pop until '(' from ops to output, output: A B C +. Pop the '(' from the ops stack.
8. '/' is an operator. It has lower precedence than '*', so pop '*' from ops to output, output: A B C + * , and then push '/' to ops.
9. D is an operand, output: A B C + * D.
10. End of expression, pop remaining '/' from ops to output.

### **Final Postfix Expression**:
A B C + * D /

---
# **Laboratory 5 Activity: Infix to Postfix Converter**

## **Goal**:
By the end of this activity, your portfolio web app should allow a user to input an infix expression and instantly see its postfix equivalent displayed on the page.

---

## **Instructions**:

### **1. Python Program (Stack Algorithm Implementation)**
- Create a **Python program** that converts an **infix expression** (ex: `A + B * C`) into a **postfix expression** (ex: `A B C * +`) using the **Shunting Yard Algorithm** (as discussed in class).
- The program should accept an infix expression as input and display the equivalent postfix expression as output.

---

### 2. **Web Application Integration**
- Open your **portfolio web application** and go to your “**Works**” page.
- Create a **new page** dedicated to the infix-to-postfix converter.
- This page must include:
  1. A **text box** for users to input an infix expression (string).  
  2. A **button** labeled **“Convert to Postfix”**.  
  3. When the button is clicked, the page should call the **Python function** you created in Step 1 to perform the conversion.  
  4. Display the **converted postfix expression** below the button.