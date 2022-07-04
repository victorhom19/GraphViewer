import tempfile
from pathlib import Path

import docker


def make(code: str):
    with tempfile.TemporaryDirectory() as dir:
        name = Path(dir) / 'code.js'
        with open(name, 'w') as file:
            file.write(code)

        client = docker.from_env()

        return client.containers.run("jsast",
                                ["java", "-jar", "/home/compiler.jar", "--js", 'code/code.js', "--print_ast"],
                                remove=True,
                                working_dir='/home',
                                volumes=[f'{Path(dir)}:/home/code']
                                ).decode('utf-8')
