from pydantic import BaseModel


class Engine(BaseModel):
    name: str


class Car(BaseModel):
    name: str
    engine: Engine


class Ship(BaseModel):
    name: str
    engine: Engine


car_engine = Engine(name="car_engine")
car = Car(name="car", engine=car_engine)

ship_engine = Engine(name="ship_engine")
ship = Ship(name="ship", engine=ship_engine)
