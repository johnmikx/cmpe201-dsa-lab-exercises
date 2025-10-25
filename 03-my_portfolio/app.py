from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/works/toUpperCase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', ''))
            result = 3.14 * radius * radius
        except ValueError:
            result = "Invalid input. Please enter a numeric value."
    return render_template('circle.html', result=result)

@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', ''))
            height = float(request.form.get('height', ''))
            result = 0.5 * base * height
        except ValueError:
            result = "Invalid input. Please enter numeric values."
    return render_template('triangle.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

def has_higher_precedence(op1, op2):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence.get(op1, 0) >= precedence.get(op2, 0)

def infix_to_postfix(expression):
    stack = []
    output = []
    operators = {'+', '-', '*', '/', '^', '(', ')'}
    
    for char in expression.replace(' ', ''):
        if char not in operators:
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
        else:
            while (stack and stack[-1] != '(' and 
                   has_higher_precedence(stack[-1], char)):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        if stack[-1] != '(':
            output.append(stack.pop())
        else:
            stack.pop()
    
    return ' '.join(output)

@app.route('/works/infix-to-postfix', methods=['GET', 'POST'])
def convert_expression():
    result = None
    if request.method == 'POST':
        infix_expr = request.form.get('expression', '')
        try:
            result = infix_to_postfix(infix_expr)
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template('infixtopostfix.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)