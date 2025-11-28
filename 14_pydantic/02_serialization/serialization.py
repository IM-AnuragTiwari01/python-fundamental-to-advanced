from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders = {datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id = 1,
    name = "Anurag Tiwari",
    email = "anurag.tiwari.en@gmail.com",
    createdAt = datetime(2025, 3, 15, 14, 30, 20),
    address = Address(
        street = "Hasting",
        city = "Kanpur",
        zip_code = "208002"
    ),
    is_active = False,
    tags = ["premium", "subscriber"]

)

python_dict = user.model_dump()
print(python_dict)

print("--" * 30)

print(user)

json_str = user.model_dump_json()

print("--" * 30)
print(json_str)
