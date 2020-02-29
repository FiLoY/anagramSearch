from collections import defaultdict

import uvicorn
from fastapi import FastAPI
app = FastAPI()

# here we save sorted words
lite_dict_db = {}

def create_dict_from_list(items: list):
    '''
    Convert list with words to dict and sort for quick search anagrams
    Example:
    get: ["foobar", "aabb", "baba", "boofar", "test"]
    return: {'abfoor': ['foobar', 'boofar'], 'aabb': ['aabb', 'baba'], 'estt': ['test']}
    '''
    ddict = defaultdict(list)
    for item in items:
        sorted_str = ''.join(sorted(item.lower()))
        ddict[sorted_str].append(item)
    return ddict


@app.post("/load")
def load_words(items: list):
    '''
    Load words in format: ["foobar", "aabb", "baba", "boofar", "test"]
    example: curl localhost:8080/load -d '["foobar", "aabb", "baba", "boofar", "test"]'
    '''
    global lite_dict_db
    lite_dict_db = create_dict_from_list(items)
    return {'message': 'Слова успешно добавлены.'}

@app.get("/get")
def find_anagrams(word: str):
    '''
    Find anagrams by word in dict
    example: curl 'localhost:8080/get?word=test'
    '''
    sorted_str = ''.join(sorted(word.lower()))
    return lite_dict_db.get(sorted_str, None)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
