import os

def test_output():
    assert 'Hello, Jenkins!' in os.popen('python src/hello_world.py').read()
