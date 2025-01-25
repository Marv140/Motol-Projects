import random
from flask import Flask, render_template, session, jsonify, request
from long_snippets import LONG_QUESTIONS  # your question data

app = Flask(__name__)
app.secret_key = "some_secret_key"

questions = LONG_QUESTIONS

@app.route("/")
def index():
    # Clear the session so each new visit has a fresh quiz
    session.clear()
    return render_template("index.html")


@app.route("/get-question", methods=["GET"])
def get_question():
    # 1) Initialize session keys if missing
    if "used_questions" not in session:
        session["used_questions"] = []
    if "current_question_index" not in session:
        session["current_question_index"] = None

    used = session["used_questions"]
    current_idx = session["current_question_index"]
    all_indices = list(range(len(questions)))

    # 2) If we already have a current question waiting for a correct answer, return it again
    if current_idx is not None:
        return jsonify(questions[current_idx])

    # 3) If no current question, pick from remaining
    remaining = [i for i in all_indices if i not in used]

    # If no remaining, "quiz complete"
    if not remaining:
        return jsonify({
            "code": "Sada hádanek dokončena!\nPro začátek stiskni F5",
            "language": None
        })

    # Otherwise pick a new question at random
    chosen_index = random.choice(remaining)
    session["current_question_index"] = chosen_index
    # DO NOT add to used_questions yet. We only add it AFTER the user answers correctly.

    return jsonify(questions[chosen_index])

@app.route("/submit-answer", methods=["POST"])
def submit_answer():
    data = request.json
    selected_language = data.get("language")
    correct_language  = data.get("correct_language")

    # Initialize counters if missing
    if "score" not in session:
        session["score"] = 0
    if "questions_answered" not in session:
        session["questions_answered"] = 0
    if "used_questions" not in session:
        session["used_questions"] = []
    if "current_question_index" not in session:
        session["current_question_index"] = None

    session["questions_answered"] += 1

    if selected_language == correct_language:
        session["score"] += 1
        # Mark the current question as "used up" since we got it right
        if session["current_question_index"] is not None:
            session["used_questions"].append(session["current_question_index"])
        # Clear the current question so the next /get-question picks a new one
        session["current_question_index"] = None

        return jsonify({
            "result": "correct",
            "score": session["score"]
        })
    else:
        # We do NOT change current_question_index or used_questions,
        # so next time /get-question is called, the user sees the SAME snippet.
        return jsonify({
            "result": "incorrect",
            "correct_language": correct_language,
            "score": session["score"]
        })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=25571)
