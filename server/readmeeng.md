## Server side 

### Operation algorithm
#### 1) In *app.py* accept a request from the client containing the code, language and name of the tree and redirect it to the handler of the desired module
#### 2) Get a call from *app.py* in the *handler* method. The call contains the program code and the name of the tree
#### 3) Send the code to the analyzer via handler (this is not necessarily a python program, it is possible to use *docker*)
#### 4) Return the graph representation in *dot* format to the client

## The code was tested for python3.10

## GUI server startup in pycharm, etc.
* Installing all dependencies (either via pip install, or via GUI environments, etc.)
* Running the main method in /server/app.py
## Starting the server via pipenv
```bash
pip install pipenv
pipenv shell
pipenv install
python ./app.py
```
## Starting the server via virtualenv
```bash
pip install virualenv
virtualenv venv # creating an environment
./venv/Scripts/activate.bat # windows
source venv/bin/activate # mac, linux
pip install -r requirements.txt 
python ./app.py
```
### At the address `http://localhost:8000/docs ` it is possible to access the interactive api of the server.
### At the address `http://localhost:8000 /` main page *index.html *.