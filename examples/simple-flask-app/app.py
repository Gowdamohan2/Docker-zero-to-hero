from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory message store (resets on container restart - great teaching point!)
messages = []

@app.route("/")
def home():
    return render_template("index.html", messages=messages)

@app.route("/add", methods=["POST"])
def add_message():
    msg = request.form.get("message", "").strip()
    if msg:
        messages.append(msg)
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
