const taskList = document.getElementById('task-list');
const newTaskInput = document.getElementById('new-task');
const addBtn = document.getElementById('add-btn');

let tasks = [];


function loadTasks() {
  const tasksJSON = localStorage.getItem('tasks');
  if (tasksJSON) {
    tasks = JSON.parse(tasksJSON);
  }
  renderTasks();
}


function saveTasks() {
  localStorage.setItem('tasks', JSON.stringify(tasks));
}

function addTask() {
  const newTask = newTaskInput.value.trim();
  if (newTask) {
    tasks.push({
      text: newTask,
      done: false,
    });
    newTaskInput.value = '';
    renderTasks();
    saveTasks();
  }
}


function renderTasks() {
  taskList.innerHTML = '';
  tasks.forEach((task, index) => {
    const taskItem = document.createElement('li');
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = task.done;
    checkbox.addEventListener('change', () => {
      task.done = checkbox.checked;
      saveTasks();
      renderTasks();
    });
    const taskText = document.createTextNode(task.text);
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Удалить';
    deleteBtn.addEventListener('click', () => {
      tasks.splice(index, 1);
      saveTasks();
      renderTasks();
    });
    taskItem.appendChild(checkbox);
    taskItem.appendChild(taskText);
    taskItem.appendChild(deleteBtn);
    if (task.done) {
      taskItem.classList.add('done');
    }
    taskList.appendChild(taskItem);
  });
}

addBtn.addEventListener('click', addTask);

loadTasks();
