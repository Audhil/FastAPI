# to validate datatype of props

from pydantic import BaseModel, EmailStr

class Person(BaseModel):
    name: str
    age: int
    email: EmailStr

person = Person(name="John", age=42, email="a@b.com")
print(person)