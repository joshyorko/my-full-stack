# tests/test_allocation.py

import pytest
from fastapi.testclient import TestClient
from app.api.routes.allocation import router
from app.core.config import settings
from app.models import User
from app.api.deps import get_current_active_user
from unittest.mock import patch
import requests

client = TestClient(router)

# Mock user dependency
def mock_get_current_active_user():
    return User(id=1, email="test@example.com", is_active=True)

@pytest.fixture
def override_get_current_active_user():
    router.dependency_overrides[get_current_active_user] = mock_get_current_active_user
    yield
    router.dependency_overrides.pop(get_current_active_user)

def test_get_attachment_success(override_get_current_active_user):
    dcn = "50072560"
    provider = "ehg"
    url = f"{settings.ATTACHMENT_SERVICE_URL}/prod/all/{dcn}?provider={provider.lower()}"
    headers = {"Authorization": f"Bearer {settings.SECRET_TOKEN}"}
    
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "some_data"}
        
        response = client.get(f"/get_attachment/?dcn={dcn}&provider={provider}")
        assert response.status_code == 200
        assert response.json() == {"data": "some_data"}

def test_get_attachment_missing_dcn(override_get_current_active_user):
    response = client.get("/get_attachment/?provider=all")
    assert response.status_code == 400
    assert response.json() == {"detail": "No electronic attachment provided"}

def test_get_attachment_request_exception(override_get_current_active_user):
    dcn = "12345"
    provider = "eims"
    
    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.RequestException
        
        response = client.get(f"/get_attachment/?dcn={dcn}&provider={provider}")
        assert response.status_code == 500