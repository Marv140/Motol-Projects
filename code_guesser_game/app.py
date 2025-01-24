import random
from flask import Flask, render_template, session, jsonify, request
from long_snippets import LONG_QUESTIONS

app = Flask(__name__)
app.secret_key = "some_secret_key"  # Required for session usage

# Sample code snippets for each language
questions = LONG_QUESTIONS


@app.route("/")
def index():
    # Initialize or reset session counters if needed
    session["score"] = 0
    session["questions_answered"] = 0
    return render_template("index.html")

@app.route("/get-question", methods=["GET"])
def get_question():
    question = random.choice(questions)
    return jsonify(question)

@app.route("/submit-answer", methods=["POST"])
def submit_answer():
    data = request.json
    selected_language = data.get("language")
    correct_language  = data.get("correct_language")

    if "score" not in session:
        session["score"] = 0
    if "questions_answered" not in session:
        session["questions_answered"] = 0

    session["questions_answered"] += 1

    if selected_language == correct_language:
        session["score"] += 1
        return jsonify({
            "result": "correct",
            "score": session["score"]
        })
    else:
        return jsonify({
            "result": "incorrect",
            "correct_language": correct_language,
            "score": session["score"]
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
