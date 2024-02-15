import random
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class User:
    id: int
    ssn: str
    email: str
    birth_date: str = "01-01-1990"
    phone_number: str = "(555) 555-5555"


@dataclass
class Contest:
    user_id: int
    title: str
    score: int = field(init=False)
    id: Optional[int] = None

    def __post_init__(self):
        # We don't care about score, we just want random values
        self.score = random.randint(0, 10)
