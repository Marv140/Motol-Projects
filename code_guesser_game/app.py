from flask import Flask, render_template, request, jsonify, session
import random
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

questions = [
    {"image": "python_code.png", "language": "Python"},
    {"image": "javascript_code.png", "language": "JavaScript"},
    {"image": "c++_code.png", "language": "C++"},
    {"image": "ruby_code.png", "language": "Ruby"},
    {"image": "java_code.png", "language": "Java"},
    # Add more questions as needed
]

@app.route('/')
def index():
    session['score'] = 0
    session['questions_answered'] = 0
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

    if 'score' not in session:
        session['score'] = 0
    if 'questions_answered' not in session:
        session['questions_answered'] = 0

    session['questions_answered'] += 1

    if selected_language == correct_language:
        session['score'] += 1
        return jsonify({"result": "correct", "score": session['score']})
    else:
        return jsonify({"result": "incorrect", "correct_language": correct_language, "score": session['score']})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port="25571")
