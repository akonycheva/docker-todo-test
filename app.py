from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="db",
    database="todo",
    user="user",
    password="password"
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        task TEXT NOT NULL
    )
""")
conn.commit()


@app.route('/tasks', methods=['GET'])
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json['task']
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    conn.commit()
    return jsonify({'message': 'Task added successfully'}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
