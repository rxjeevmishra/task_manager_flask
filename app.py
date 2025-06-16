from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS
from task_manager import TaskManager

app = Flask(__name__)
CORS(app)

task_manager = TaskManager()

@app.route("/")
def index():
    tasks = task_manager.list_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]
    desc = request.form.get("desc", "")
    due = request.form.get("due", "")
    priority = request.form.get("priority", "low")
    task_manager.add_task(title, desc, due, priority)
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete(task_id):
    task_manager.complete_task(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
