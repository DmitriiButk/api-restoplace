from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_get_items():
    response = client.get('/restaurant/items')
    assert response.status_code == 200


def test_get_items_with_query():
    params = {
        'query': 'floorid=100',
        'page': 1
    }
    response = client.get('/restaurant/items', params=params)
    assert response.status_code == 200


def test_get_item_by_id():
    response = client.get('/restaurant/items/123')
    print(response.json())
    assert response.status_code == 200
