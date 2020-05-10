from kdecorators.decorators import no_raise, suppress_raise, raises

@no_raise
def func_that_does_not_throw():
    return 1/1
func_that_does_not_throw()

@suppress_raise
def func_that_throws_1():
    return 1/0
func_that_throws_1()

@raises
def func_that_throws_3(i: int, j: int = 2):
    print(i, j)
    return 1/0
func_that_throws_3(1, j=3)