from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProfileDataClass:
    id: int
    name: str
    surname: str
    age: int
    created_at: datetime
    updated_at: datetime


@dataclass
class UserDataClass:
    id: int
    email: str
    password: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
    profile: ProfileDataClass


@dataclass
class CarDataClass:
    id: int
    model: str
    year: int
    number_of_seats: int
    body_type: str
    engine_capacity: float
    created_at: datetime
    updated_at: datetime
