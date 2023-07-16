import inspect


def get_current_argspec():
    """Find the current function, print the args."""
    frame = inspect.stack()[1][0]
    return inspect.getargvalues(frame)[-1]


def target(x, y, z=None):
    print("naively got called with x =", x, "y = ", y, "z = ", z)
    print("Rummaged around the stack and got", get_current_argspec())


target(1, 2)
