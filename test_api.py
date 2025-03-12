import requests

BASE_URL = "http://localhost:5000"


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_task():
    task = {"task": "Test task"}
    response = requests.post(f"{BASE_URL}/tasks", json=task)
    assert response.status_code == 201
    assert response.json()['message'] == 'Task added successfully'


def test_delete_task():
    requests.post(f"{BASE_URL}/tasks", json={"task": "Test delete"})
    response = requests.delete(f"{BASE_URL}/tasks/1")
    assert response.status_code == 200
    assert response.json()['message'] == 'Task deleted'


if __name__ == "__main__":
    test_get_tasks()
    test_add_task()
    test_delete_task()
    print("Tests passed!")
