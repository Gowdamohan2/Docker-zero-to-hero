from flask import Flask, render_template, request, redirect, url_for
import uuid
from datetime import datetime

app = Flask(__name__)

# Simple in-memory store — resets when container restarts
# (good talking point about container statefulness)
tasks = []

@app.route("/")
def index():
    total = len(tasks)
    done  = sum(1 for t in tasks if t["done"])
    return render_template("index.html", tasks=tasks, total=total, done=done)

@app.route("/add", methods=["POST"])
def add():
    title    = request.form.get("title", "").strip()
    priority = request.form.get("priority", "medium")
    if title:
        tasks.append({
            "id":         str(uuid.uuid4()),
            "title":      title,
            "priority":   priority,
            "done":       False,
            "created_at": datetime.now().strftime("%d %b, %I:%M %p"),
        })
    return redirect(url_for("index"))

@app.route("/toggle/<task_id>")
def toggle(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = not t["done"]
            break
    return redirect(url_for("index"))

@app.route("/delete/<task_id>")
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
