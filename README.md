# kdecorators

~~~~python
@no_raise
def func_that_does_not_raise():
    return 1/1

@suppress_raise
def func_that_would_raise_but_wont_because_of_the_decorator():
    return 1/0

@raises
def func_that_raises(i: int, j: int = 2):
    return 1/0
~~~~
