from abc import ABC
from functools import wraps
from typing import Any, Callable


def change_init_func(func: Callable[..., Any]):
    @wraps(func)
    def new_init(self: AbstractClass, name: str, *args: Any, **kwargs: Any):
        self.__class__.count += 1
        print(
            f"#{self.__class__.count} instance of Class {self.__class__.__name__} inheriting AbstractClass is being created..."
        )
        return func(self, name, *args, **kwargs)

    return new_init


class AbstractClass(ABC):
    count = 0

    def __init__(self, name: str) -> None:
        pass

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()

        print(f"Class {cls.__name__} is inheriting AbstractClass...")
        cls.count = 0
        cls.__init__
        cls.__init__ = change_init_func(cls.__init__)


class BaseClass(AbstractClass):
    def __init__(self, name: str, name2: str) -> None:
        pass


class BaseClass2(AbstractClass):
    def __init__(self, name: str) -> None:
        pass


BaseClass(name="test", name2="test")
BaseClass2(name="test")
BaseClass2(name="test")
BaseClass2(name="test")
BaseClass(name="test", name2="test")
