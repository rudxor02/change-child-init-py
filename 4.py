from abc import ABC, ABCMeta
from functools import wraps
from typing import Any, Callable, Optional, dataclass_transform


@dataclass_transform()
class NewModelMetaclass(ABCMeta):
    ...


def change_vehicle_child_init_func(init: Callable[..., Any]):
    @wraps(init)
    def new_init(
        self: Vehicle,
        *args: Any,
        name: str,
        engine: Optional[Engine] = None,
        **kwargs: Any,
    ):
        self.name = name
        if engine is None:
            self.engine = Engine(name=f"{name}_engine")
        else:
            self.engine = engine

    return new_init


def change_new_base_model_child_init_func(init: Callable[..., Any]):
    @wraps(init)
    def new_init(self: NewBaseModel, *args: Any, **kwargs: Any):
        self.__dict__.update(kwargs)

    return new_init


class NewBaseModel(metaclass=NewModelMetaclass):
    def __init_subclass__(cls) -> None:
        cls.__init__ = change_new_base_model_child_init_func(cls.__init__)  # type: ignore

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"


class Engine(NewBaseModel):
    name: str


mock_engine = Engine(name="mock_engine")


print(mock_engine)
# Engine({'name': 'mock_engine'})


class Vehicle(NewBaseModel, ABC):
    name: str
    engine: Engine = mock_engine

    def __init_subclass__(cls) -> None:
        cls.__init__ = change_vehicle_child_init_func(cls.__init__)  # type: ignore


class Car(Vehicle):
    pass


class Ship(Vehicle):
    pass


car = Car(name="car")
ship = Ship(name="ship")
print(car)
# Car({'name': 'car', 'engine': Engine({'name': 'car_engine'})})
print(ship)
# Ship({'name': 'ship', 'engine': Engine({'name': 'ship_engine'})})
