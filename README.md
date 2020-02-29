## Description
HTTP сервис для быстрого поиска анаграмм в словаре.
Два слова считаются анаграммами, если одно можно получить из другого перестановкой букв (без учета регистра).

## Technical specifications
 - python 3.8;
 - fastAPI 0.49.0.

## Getting started
 - `git clone https://github.com/FiLoY/anagramSearch.git` 
 - `cd anagramSearch`
 - `docker-compose up`
 
## Examples
Загрузка словаря: 
  - `curl localhost:8080/load -d '["foobar", "aabb", "baba", "boofar", "test"]'`
  
Поиск анаграмм: 
 - `curl 'localhost:8080/get?word=raboof'` 

## Tests
Для тестирования использовался pytest:
 - `pytest test_mail.py`
