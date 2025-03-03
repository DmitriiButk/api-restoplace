from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime, timedelta

client = TestClient(app)


def test_get_reserves():
    response = client.get("/restaurant/reserves")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_reserve_by_id():
    response = client.get(f"/restaurant/reserves/123")
    assert response.status_code == 200
    assert isinstance(response.json()['responseData'], list)


def test_create_reserve():
    now = datetime.now()
    from_time = now.strftime('%Y-%m-%d %H:%M:%S')
    to_time = (now + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')  # время окончания через 2 часа

    payload = {
        "from_time": from_time,
        "to": to_time,
        "name": "Anton",
        "phone": '79876543211',
        "email": "test@example.com",
        "count": 3,
        "text": "some text",
        "source": "website",
        "waitlist": False,
        "deposit": True
    }
    response = client.post("/restaurant/reserves", json=payload)
    assert response.status_code == 200
    assert response.json()['responseData']['message'] == 'Резерв создан'
