import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        with app.app_context():
            # Initialize the database or any other setup here
            pass
        yield client

def test_get_words(client):
    response = client.get('/words')
    assert response.status_code == 200
    data = response.get_json()
    assert 'words' in data
    assert 'total_pages' in data
    assert 'current_page' in data

def test_get_words_with_pagination(client):
    response = client.get('/words?page=2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['current_page'] == 2

def test_get_words_with_sorting(client):
    response = client.get('/words?sort_by=romaji&order=desc')
    assert response.status_code == 200
    data = response.get_json()
    assert 'words' in data
    assert len(data['words']) > 0
    assert data['words'][0]['romaji'] >= data['words'][-1]['romaji']