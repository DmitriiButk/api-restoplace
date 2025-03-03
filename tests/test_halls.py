from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_get_halls():
    response = client.get('/restaurant/halls')
    assert response.status_code == 200


def test_get_halls_with_query():
    params = {
        'query': 'banquet=1',
        'page': 1
    }
    response = client.get('/restaurant/halls', params=params)
    assert response.status_code == 200


def test_get_hall_by_id():
    response = client.get('/restaurant/halls/123')
    assert response.status_code == 200
