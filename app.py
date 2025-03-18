from flask import Flask, request, render_template, redirect, url_for, jsonify
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(
    dbname=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host='db'  # Название сервиса db из docker-compose
)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, task TEXT NOT NULL)")
conn.commit()

@app.route('/api/tasks', methods=['GET'])
def get_tasks_api():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return jsonify([{"id": t[0], "task": t[1]} for t in tasks])

@app.route('/api/tasks', methods=['POST'])
def add_task_api():
    task = request.json['task']
    cursor.execute("INSERT INTO tasks (task) VALUES (%s) RETURNING id", (task,))
    task_id = cursor.fetchone()[0]
    conn.commit()
    return jsonify({"id": task_id, "task": task}), 201

@app.route('/', methods=['GET'])
def index():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)