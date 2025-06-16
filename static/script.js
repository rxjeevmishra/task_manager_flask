document.addEventListener("DOMContentLoaded", () => {
  const taskList = document.getElementById("taskList");
  const form = document.getElementById("taskForm");

  // Fetch and display tasks
  async function loadTasks() {
    const response = await fetch("/tasks");
    const tasks = await response.json();

    taskList.innerHTML = "";
    tasks.forEach(task => {
      const li = document.createElement("li");
      li.className = `list-group-item d-flex justify-content-between align-items-center`;

      li.innerHTML = `
        <div>
          <strong>${task.title}</strong> (${task.priority})
          <div class="text-muted small">${task.desc || ""} ${task.due ? ` | Due: ${task.due}` : ""}</div>
        </div>
        <button class="btn btn-sm ${task.completed ? 'btn-success' : 'btn-outline-success'}" 
                ${task.completed ? "disabled" : ""} 
                onclick="markComplete(${task.id})">
          ${task.completed ? "✓ Completed" : "Mark Done"}
        </button>
      `;
      taskList.appendChild(li);
    });
  }

  // Submit new task
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const task = {
      title: document.getElementById("title").value,
      desc: document.getElementById("desc").value,
      due: document.getElementById("due").value,
      priority: document.getElementById("priority").value
    };

    await fetch("/tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(task)
    });

    form.reset();
    loadTasks();
  });

  // Global function to mark a task complete
  window.markComplete = async function(id) {
    await fetch(`/tasks/${id}/complete`, { method: "POST" });
    loadTasks();
  };

  loadTasks();
});
