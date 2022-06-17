## Серверная часть 

### Примерный алгоритм работы
#### 1) Получить запрос от клиента. Запрос содержит код программы.
#### 2) Отправить код анализатору (это не обязательно python программа)
#### 3) Вернуть клиенту представление графа в формате dot

## Код тестировался для python3.10
## Запуск сервера через pipenv
```bash
pip install pipenv
pipenv shell
pipenv install
python ./src/app.py
```
## Запуск через virtualenv
```bash
pip install virualenv
virtualenv venv # создание среды
./venv/Scripts/activate.bat # windows
sourse venv/bin/activate # mac, linux
pip install -r requirements.txt 
python ./src/app.py
```
### По адресу `http://localhost:8000/docs` можно получить доcтуп к интерактивному api сервера.