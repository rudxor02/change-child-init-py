from inspect import signature


def add(x: int, y: int) -> int:
    return x + y


print(signature(add))

# (x: int, y: int) -> int
