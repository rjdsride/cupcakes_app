from typing import List

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


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



DATABASE_URL = "sqlite:///./cupcakes.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    customer_phone = Column(String, nullable=False)
    cupcake_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    delivery_type = Column(String, nullable=False)
    total = Column(Float, nullable=False)
    notes = Column(String, nullable=True)


def init_db() -> None:
    """Cria as tabelas no banco (se não existirem)."""
    Base.metadata.create_all(bind=engine)
