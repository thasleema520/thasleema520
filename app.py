from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['userInput']
    processed_output = user_input.upper()  # Example: process the input
    return f'You entered: {user_input}. Processed output: {processed_output}'

if __name__ == '__main__':
    app.run(debug=True)
