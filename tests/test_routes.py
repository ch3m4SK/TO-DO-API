import pytest
from app import create_app, db
from config import TestingConfig

@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_add_task(client):
    response = client.post(
        '/tasks',
        json={'title': 'Test Task'},
        headers={'Content-Type': 'application/json'}
    )
    assert response.status_code == 201
    assert b'Test Task' in response.data