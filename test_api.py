import requests
import time

BASE_URL = "http://backend:5000"


def test_get_tasks():
    max_retries = 10
    for i in range(max_retries):
        try:
            response = requests.get(f"{BASE_URL}/api/tasks")
            print(f"Status Code: {response.status_code}")
            print(f"Response Content: {response.text}")
            assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
            print("GET test passed!")
            break
        except requests.exceptions.ConnectionError:
            if i < max_retries - 1:
                print(f"Backend not ready, retrying in 5 seconds... ({i+1}/{max_retries})")
                time.sleep(5)
            else:
                raise Exception("Failed to connect to backend after maximum retries")

test_get_tasks()


def test_add_task():
    max_retries = 10
    for i in range(max_retries):
        try:
            response = requests.post(f"{BASE_URL}/api/tasks", json={"task": "Test task from test"})
            print(f"POST Status Code: {response.status_code}")
            print(f"POST Response Content: {response.text}")
            assert response.status_code == 201, f"Expected status 201, got {response.status_code}"
            print("POST test passed!")
            break
        except requests.exceptions.ConnectionError:
            if i < max_retries - 1:
                print(f"Backend not ready, retrying in 5 seconds... ({i+1}/{max_retries})")
                time.sleep(5)
            else:
                raise Exception("Failed to connect to backend after maximum retries")

if __name__ == "__main__":
    test_get_tasks()
    test_add_task()
    print("Tests passed!")
