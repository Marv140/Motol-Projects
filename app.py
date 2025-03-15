import os
import random
import flask
import long_snippets

app = flask.Flask(__name__, static_folder='static')

# Set the secret key for sessions
app.secret_key = "secret_keySIGMASIGMASKIBIDISIGMAsecret_keysecret_keysecret_keysecret_keysecret_keysecret_keysecret_keysecret_key"

questions = long_snippets.LONG_QUESTIONS

# Directory containing MHD images
MHD_IMAGE_DIR = 'static/images/mhd_guesser'

# List of Czech cities with folder names
czech_cities = [
    ("Brno", "brno"),
    ("České Budějovice", "ceske_budejovice"),
    ("Chomutov", "chomutov"),
    ("Děčín", "decin"),
    ("Hradec Králové", "hradec_kralove"),
    ("Jihlava", "jihlava"),
    ("Karlovy Vary", "karlovy_vary"),
    ("Liberec", "liberec"),
    ("Mladá Boleslav", "mlada_boleslav"),
    ("Mariánské Lázně", "marianske_lazne"),
    ("Most", "most"),
    ("Olomouc", "olomouc"),
    ("Ostrava", "ostrava"),
    ("Pardubice", "pardubice"),
    ("Plzeň", "plzen"),
    ("Praha", "praha"),
    ("Teplice", "teplice"),
    ("Ústí nad Labem", "usti_nad_labem"),
    ("Zlín", "zlin")
]

def get_mhd_images():
    images = []
    for city, folder in czech_cities:
        city_dir = os.path.join(MHD_IMAGE_DIR, folder)
        if os.path.isdir(city_dir):
            for filename in os.listdir(city_dir):
                if filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    images.append((folder, os.path.join(city_dir, filename)))  # Use folder name instead of city name
    return images

def create_mhd_question():
    if "used_mhd_images" not in flask.session:
        flask.session["used_mhd_images"] = []

    images = get_mhd_images()
    unused_images = [img for img in images if img[1] not in flask.session["used_mhd_images"]]

    if not unused_images:
        flask.session["used_mhd_images"] = []
        unused_images = images

    if not unused_images:
        return None

    selected_image = random.choice(unused_images)
    flask.session["used_mhd_images"].append(selected_image[1])

    correct_folder = selected_image[0]
    correct_city = next(city for city, folder in czech_cities if folder == correct_folder)
    options = random.sample([city for city, folder in czech_cities], 3)
    if correct_city not in options:
        options[random.randint(0, 2)] = correct_city

    # Shuffle the options to ensure randomness
    random.shuffle(options)

    return {
        "image": selected_image[1],
        "answer": correct_city,
        "options": options
    }

MAINTENANCE_MODE = False

if MAINTENANCE_MODE == True:
    @app.route("/maintenance")
    def maintenance():
        return flask.render_template("maintenance.html")

    @app.before_request
    def check_for_maintenance():
        if flask.request.path != "/maintenance" and not flask.request.path.startswith('/static/'):
            return flask.redirect("/maintenance")
if not MAINTENANCE_MODE:
    @app.before_request
    def redirect_to_index():
        if flask.request.path == "/maintenance":
            return flask.redirect("/")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route('/code_guesser')
def code_guesser():
    return flask.render_template('code_guesser.html')

@app.route('/mhd_guesser')
def mhd_guesser():
    return flask.render_template('mhd_guesser.html')

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
    correct_language = data.get("correct_language")

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

@app.route("/get-mhd-question", methods=["GET"])
def get_mhd_question():
    if "used_mhd_questions" not in flask.session:
        flask.session["used_mhd_questions"] = []

    question = create_mhd_question()
    if not question:
        return flask.jsonify({
            "result": "Nebyly nalezeny žádné obrázky."
        })

    return flask.jsonify(question)

@app.route("/submit-mhd-answer", methods=["POST"])
def submit_mhd_answer():
    data = flask.request.json
    answer = data.get("answer").lower()
    correct_answer = data.get("correct_answer").lower()

    if "mhd_score" not in flask.session:
        flask.session["mhd_score"] = 0

    if answer == correct_answer:
        flask.session["mhd_score"] += 1
        return flask.jsonify({"result": "correct", "score": flask.session["mhd_score"]})
    else:
        return flask.jsonify({"result": "incorrect", "correct_answer": correct_answer, "score": flask.session["mhd_score"]})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=25571)