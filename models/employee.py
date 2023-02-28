from pydantic import BaseModel

class EmployeeModel(BaseModel):
    id:int
    name:str
    age:int
    company:str