from flask import Flask, render_template, request, jsonify
import AI_PRED

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload

@app.route("/")


def index() -> str:
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or "note" not in data:
        return jsonify({"error": "Missing 'text' in JSON"}), 400

    text = data["note"].strip()
    if len(text) < 50:
        return jsonify({"error": "Text too short (min 50 chars)"}), 400

    result = AI_PRED.generate_summary(text)
    print(result)
    return result


