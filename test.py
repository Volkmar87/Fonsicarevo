import requests

def test_recom():
    url = 'http://localhost:8000/recomendaciones'
    data = {'marca': 'BMW', 'modelo': 'Serie 1'}
    response = requests.post(url, json=data)
    print("Recomendaciones enviadas")
    assert response.status_code == 200
    assert 'recommendations' in response.json()
    print(response.json())

if __name__ == "__main__":
    test_recom()
