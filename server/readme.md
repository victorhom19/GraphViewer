## Серверная часть 

### Примерный алгоритм работы 
#### 1) В *app.py* принять запрос с клиента, содержащий код, язык и название дерева и перенаправить в handler нужного модуля
#### 2) Получить вызов от *app.py* в методе *handler*. Вызов содержит код программы и название дерева
#### 3) Отправить код анализатору через handler (это не обязательно python программа, возможно использование *docker*)
#### 4) Вернуть клиенту представление графа в формате *dot*

## Код тестировался для python3.10

## GUI запуск сервера в pycharm и т.п.
* Установка всех зависимостей (либо через pip install, либо через GUI среды и тд)
* Запуск метода main в /server/app.py
## Запуск сервера через pipenv
```bash
pip install pipenv
pipenv shell
pipenv install
python ./app.py
```
## Запуск через virtualenv
```bash
pip install virualenv
virtualenv venv # создание среды
./venv/Scripts/activate.bat # windows
source venv/bin/activate # mac, linux
pip install -r requirements.txt 
python ./app.py
```
### По адресу `http://localhost:8000/docs` можно получить доcтуп к интерактивному api сервера.
### По адресу `http://localhost:8000/` основная страница *index.html*.