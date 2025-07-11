from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS
from task_manager import TaskManager
import os

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

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        due_date = request.form["due"]
        priority = request.form["priority"]
        task_manager.update_task(task_id, title, desc, due_date, priority)
        return redirect(url_for("index"))
    task = task_manager.get_task(task_id)
    return render_template("edit_task.html", task=task)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT
    app.run(host="0.0.0.0", port=port)
