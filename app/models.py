from pydantic import BaseModel
from typing import List


class Cupcake(BaseModel):
    id: int
    name: str
    description: str
    price: float


CUPCAKES: List[Cupcake] = [
    Cupcake(
        id=1,
        name="Cupcake de Chocolate",
        description="Cobertura de ganache e granulado.",
        price=7.50,
    ),
    Cupcake(
        id=2,
        name="Cupcake de Morango",
        description="Recheio de geleia de morango e chantilly.",
        price=8.00,
    ),
    Cupcake(
        id=3,
        name="Cupcake Red Velvet",
        description="Massa aveludada com cream cheese.",
        price=9.00,
    ),
]


def get_cupcake_by_id(cupcake_id: int) -> Cupcake | None:
    for cupcake in CUPCAKES:
        if cupcake.id == cupcake_id:
            return cupcake
    return None
