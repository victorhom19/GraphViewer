# GraphViewer

##### Веб-приложение для отрисовки различных моделей представлений кода.
##### На вход подается фрагмент исходного кода, название языка и модель представления.
##### На выходе - дерево или граф
```python
a = 2
b = 3
if a > b:
    a = a + b
else:
    a = a - b
c = a + b

```
### python + control flow graph
```mermaid
graph TD;
    A1[a = 2]-->A2;
    A2[b = 3]-->A3;
    A3{a > b}--yes-->B1;
    A3--no-->C1;
    B1[a = a + b];
    C1[a = a - b];
    D1[c = a + b];
    B1-->D1;
    C1-->D1;
```
## Поддерживаемые языки и модели
#### 1) python
- ast
- cfg
#### 2) kotlin
- ast
#### 3) c
- cfg
- ssa
# Установка

## Требования
- [Docker](https://www.docker.com/get-started/)
- python3
- [graphviz](https://graphviz.org/)

## Поддержка Go
Чтобы приложение работало с кодом на Go необходимо собрать образ Docker:
```bash
docker build -t st-dot server/go/src/github.com/nikiens/st-dot
```

## Алгоритм запуска расположен в папке [server](./server/readme.md)