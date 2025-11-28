from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street= "123",
    city = "Kanpur",
    postal_code = "208002"
)

user2 = User(
    id = 1,
    name = "Anurag",
    address = address 
)



# another way of doing this

user_data = {
    "id": 1,
    "name": "Anurag",
    "address": {
        "street" : "321",
        "city": "Kanpur",
        "postal_code": "208001"
    }
}

user = User(**user_data)
print(user)
print(user2.model_dump)