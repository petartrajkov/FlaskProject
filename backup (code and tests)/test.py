import requests

ENDPOINT = "https://todo.pixegami.io/"

# to write a test we need to start a function that begins with test_
# to run the test in terminal we write pytest or pytest <name of file> example "pytest test.py"


def test_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass


def test_can_create_task():
    payload = {
        "content": "some test content",
        "user_id": "test_user",
        "is_done": False,
    }

    create_task_response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    print(data)

    task_id = data["task"]["task_id"]
    get_task_response = requests.get(ENDPOINT + f"/get-task/{task_id}")
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)


# to check the data one can use the command in Terminal: "pytest -v -s"
