def pow(x: int, n: int) -> int:
    """pow(x, n) -> x ^ n"""
    return x ** n


def map(func, l: list) -> list:
    """
    Apply a function to each element of l.
    map(func, l) -> [func(x1), ..., func(xn)]
    """
    return [func(i) for i in l]


class Test(object):

    def __init__(self) -> None:
        pass

    def test(self):
        """
        A doc
        test
        .
        """
        return False

        def test2():
            """Un commentaire"""
            pass


test = Test()


class Test2:

    def __init__(self) -> None:
        pass

    def class_func_test(self, x: float) -> Test:
        """A test func in a class."""
        pass


def end_func(x: int):
    """
    Comment.
    """
    pass
