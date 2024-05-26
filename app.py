from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']
    letter_count = len(text)
    response = f"Processed text: {text}, Number of letters: {letter_count}"
    return response

if __name__ == '__main__':
    app.run(debug=True)
