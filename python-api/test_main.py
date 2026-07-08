from fastapi.testclient import TestClient
# Importieren Sie die FastAPI-App aus Ihrer main.py
from main import app 

client = TestClient(app)

def test_default_placeholder():
    # Testet den Standard-Pfad: /placeholder/300x200
    response = client.get("/placeholder/300x200")
    assert response.status_code == 200
    assert "svg" in response.headers["content-type"]
    assert "<svg" in response.text

def test_custom_colors():
    # Testet Abfrageparameter für Farben
    response = client.get("/placeholder/600x400?bg=0055ff&text_color=ffffff")
    assert response.status_code == 200
    assert "0055ff" in response.text
