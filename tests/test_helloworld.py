from helloworld.helloworld import *

def test_helloworld():
    hello = helloworld()
    assert("Hello World" in hello)