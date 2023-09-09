from abc import ABC
from functools import wraps
from typing import Any, Callable

from pydantic import BaseModel


def change_init_func(init: Callable[..., Any]):
    @wraps(init)
    def new_init(self: Vehicle, *args: Any, name: str, **kwargs: Any):
        self.name = name
        self.engine = Engine(name=f"{self.__class__.__name__}_engine")
        init(self, *args, name, **kwargs)

    return new_init


class Engine(BaseModel):
    name: str


class Vehicle(ABC):
    name: str
    engine: Engine

    def __init_subclass__(cls) -> None:
        cls.__init__ = change_init_func(cls.__init__)  # type: ignore


class Car(Vehicle):
    def __init__(self, name: str) -> None:
        pass


class Ship(Vehicle):
    def __init__(self, name: str) -> None:
        pass


car = Car(name="car")
ship = Ship(name="ship")
