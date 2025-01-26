import random
import flask
import long_snippets

app = flask.Flask(__name__)

# Set the secret key for sessions
app.secret_key = "secret_keySIGMASIGMASKIBIDISIGMAsecret_keysecret_keysecret_keysecret_keysecret_keysecret_keysecret_keysecret_key"

questions = long_snippets.LONG_QUESTIONS

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route('/code_guesser')
def code_guesser():
    return flask.render_template('code_guesser.html')

@app.route('/public_transport_guesser')
def public_transport_guesser():
    return flask.render_template('public_transport_guesser.html')

@app.route('/coming_soon')
def coming_soon():
    return flask.render_template('coming_soon.html')


@app.route("/get-question", methods=["GET"])
def get_question():
    if "used_questions" not in flask.session:
        flask.session["used_questions"] = []
    if "current_question_index" not in flask.session:
        flask.session["current_question_index"] = None

    used = flask.session["used_questions"]
    current_idx = flask.session["current_question_index"]
    all_indices = list(range(len(questions)))

    if current_idx is not None:
        return flask.jsonify(questions[current_idx])

    remaining = [i for i in all_indices if i not in used]

    if not remaining:
        return flask.jsonify({
            "code": "Sada hádanek dokončena!\nPro začátek stiskni F5",
            "language": None
        })

    chosen_index = random.choice(remaining)
    flask.session["current_question_index"] = chosen_index

    return flask.jsonify(questions[chosen_index])

@app.route("/submit-answer", methods=["POST"])
def submit_answer():
    data = flask.request.json
    selected_language = data.get("language")
    correct_language  = data.get("correct_language")

    if "score" not in flask.session:
        flask.session["score"] = 0
    if "questions_answered" not in flask.session:
        flask.session["questions_answered"] = 0
    if "used_questions" not in flask.session:
        flask.session["used_questions"] = []
    if "current_question_index" not in flask.session:
        flask.session["current_question_index"] = None

    flask.session["questions_answered"] += 1

    if selected_language == correct_language:
        flask.session["score"] += 1
        if flask.session["current_question_index"] is not None:
            flask.session["used_questions"].append(flask.session["current_question_index"])
        flask.session["current_question_index"] = None

        return flask.jsonify({
            "result": "correct",
            "score": flask.session["score"]
        })
    else:
        return flask.jsonify({
            "result": "incorrect",
            "correct_language": correct_language,
            "score": flask.session["score"]
        })

@app.route("/reset-quiz", methods=["POST"])
def reset_quiz():
    flask.session.clear()  # Clear the session to reset progress
    return "", 204  # Respond with no content

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=25571)