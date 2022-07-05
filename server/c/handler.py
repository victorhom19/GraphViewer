from .c_ast import get_ast
from .maker import make

example_code = """
int main()
{

    int a = 2;
    int b = 3;
    if (a > b - 2)
    {
        a = a + b - 4;
    }
    else
    {
        b = b + b + 4;
    }
    a = b + 5;
    b -= 4;
}"""


def handler(code: str, model: str):
    if model == 'ast':
        return get_ast(code)
    return make(code, model=model)
