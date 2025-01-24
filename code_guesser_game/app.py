from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

questions = [
    {"image": "python_code.png", "language": "Python"},
    {"image": "javascript_code.png", "language": "JavaScript"},
    {"image": "c++_code.png", "language": "C++"},
    {"image": "ruby_code.png", "language": "Ruby"},
    {"image": "java_code.png", "language": "Java"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-question', methods=['GET'])
def get_question():
    question = random.choice(questions)
    return jsonify(question)

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    data = request.json
    selected_language = data.get('language')
    correct_language = data.get('correct_language')

    if selected_language == correct_language:
        return jsonify({"result": "correct"})
    else:
        return jsonify({"result": "incorrect"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port="25571")