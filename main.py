from flask import Flask, render_template, request, jsonify
import ai_pred

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload

@app.route("/")


def index() -> str:
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in JSON"}), 400

    text = data["text"].strip()
    if len(text) < 50:
        return jsonify({"error": "Text too short (min 50 chars)"}), 400

    result = ai_pred.generate_summary(text)
    print(result)
    return result


if __name__ == "__main__":
    app.run("127.0.0.1", port=8080, debug=True)