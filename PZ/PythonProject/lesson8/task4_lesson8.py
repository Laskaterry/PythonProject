from functools import wraps


def val_checker(func):
    def val_check(check):
        @wraps(check)
        def wrapped(x):
            if func(x):
                return check(x)
            else:
                msg = f'wrong val {x}'
                raise ValueError(msg)

        return wrapped
    return val_check


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
print(calc_cube.__name__)

a = calc_cube(-5)
print(a)
print(calc_cube.__name__)
