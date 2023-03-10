import app

def test_index():
    import requests
    response = requests.get('http://127.0.0.1:5000/')
    assert response.status_code == 200
    assert b'Entity Resolution' in response.content
    assert b'bootstrap' in response.content
    assert b'axios' in response.content
    assert b'handlebars' in response.content

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

def test_get_similar():
    from pandas import DataFrame
    result = app.get_similar('Mary Larsen')
    assert type(result) == list
    assert len(result) == 3

def test_get_random_name():
    result = app.get_random_name()
    assert type(result) == str
    assert ' ' in result

