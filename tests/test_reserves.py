from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_reserves():
    response = client.get("/restaurant/reserves")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# def test_get_reserve_by_id():
#     reserve_id = "some_reserve_id"
#     response = client.get(f"/restaurant/reserves/{reserve_id}")
#     assert response.status_code == 200
#     assert "id" in response.json()
#
#
# def test_create_reserve():
#     payload = {
#         "from_time": "2025-05-20 18:00:00",
#         "to": "2025-05-20 20:00:00",
#         "name": "Иван",
#         "phone": "79991234567",
#         "email": "ivan@example.com",
#         "count": 2,
#         "text": "Окно у окна",
#         "source": "test_source",
#         "item_ids": [101, 102],
#         "waitlist": False,
#         "deposit": True
#     }
#     response = client.post("/restaurant/reserves", json=payload)
#     assert response.status_code in [200, 201]
#     assert "method" in response.json()
