from pydantic import BaseModel, Field
# inheriting the base model class
class User(BaseModel):
    id: int

    name: str = Field(
        ...,
        min_length = 3,
        max_length = 50,
        description = "Employee Name",
        example = "Anurag Tiwari"
    )

    is_active: bool

input_data = {'id': 101, 'name': "chaicode", 'is_active': True}


user = User(**input_data)  # now the dictionary will not be treated as one objectv all the values will be scattered around
print(user)