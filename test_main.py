from starlette.testclient import TestClient
from .main import app, create_dict_from_list

def test_create_dict_from_list():
    input_data = ["foobar", "aabb", "baba", "boofar", "test"]
    return_data = {'abfoor': ['foobar', 'boofar'], 'aabb': ['aabb', 'baba'], 'estt': ['test']}
    assert create_dict_from_list(input_data) == return_data

def test_get_anagrams_without_parameters():
    client = TestClient(app, base_url='http://127.0.0.1:8080')
    response = client.get("/get")

    assert response.status_code == 422
    assert response.json() == {"detail":[{"loc":["query","word"],"msg":"field required","type":"value_error.missing"}]}

def test_get_inexistent_anagrams():
    client = TestClient(app, base_url='http://127.0.0.1:8080')
    response = client.get("/get?word=qwerty")

    assert response.status_code == 200
    assert response.json() == None

def test_get_existent_anagrams():
    client = TestClient(app, base_url='http://127.0.0.1:8080')
    client.post("/load", data='["foobar", "aabb", "baba", "boofar", "test"]')
    response = client.get("/get?word=baab")

    assert response.status_code == 200
    assert response.json() == ["aabb","baba"]

def test_load_words():
    client = TestClient(app, base_url='http://127.0.0.1:8080')
    response = client.post("/load", data='["foobar", "aabb", "baba", "boofar", "test"]')

    assert response.status_code == 200
    assert response.json() == {"message": "Слова успешно добавлены."}

def test_load_words_without_data():
    client = TestClient(app, base_url='http://127.0.0.1:8080')
    response = client.post("/load")

    assert response.status_code == 422
    assert response.json() == {'detail': [{'loc': ['body', 'items'], 'msg': 'field required', 'type': 'value_error.missing'}]}

def test_load_words_not_in_list():
    client = TestClient(app, base_url='http://127.0.0.1:8080')
    response = client.post("/load", data='foo, boo')

    assert response.status_code == 400
    assert response.json() == {'detail': 'There was an error parsing the body'}
