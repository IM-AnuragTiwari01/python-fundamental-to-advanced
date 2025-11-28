from pydantic import BaseModel
from typing import Optional, List, Union


# OPTIONAL NESTED MODULE

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None  ## nesting of adddress 


class Employee(BaseModel):
    name: str
    company:Optional[Company] = None  ## nesting of company

###################################################################

# MIXED DATA TYPES


class TextContent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]

###################################################################

#  DEEPLy NESTED STRUCTURE

class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str


class Organization(BaseModel):
    name: str
    head_quarter: Address
    branches: List[Address] = []