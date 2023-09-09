from pydantic import BaseModel


class Engine(BaseModel):
    name: str


class Car:
    def __init__(self, name: str) -> None:
        self.name = name
        self.engine = Engine(name=f"{self.__class__.__name__}_engine")


class Ship:
    def __init__(self, name: str) -> None:
        self.name = name
        self.engine = Engine(name=f"{self.__class__.__name__}_engine")


car = Car(name="car")
ship = Ship(name="ship")
