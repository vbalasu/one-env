import app

def test_index():
    import requests
    response = requests.get('http://127.0.0.1:5000/')
    assert response.status_code == 200
    assert b'hello' in response.content

def test_put():
    payload = {
        "key": "sample.json",
        "data": {
            "hello": "world"
        }
    }
    import requests
    response = requests.put('http://127.0.0.1:5000/put', json=payload)
    assert response.status_code == 200