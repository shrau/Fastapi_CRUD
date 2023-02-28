from service.employee.employee import Employee
from models.employee import EmployeeModel
from typing import Union
from typing import Optional
from fastapi import FastAPI


app = FastAPI()

emp_obj=Employee()


@app.get("/list")
def list_employees(id:Optional[int]=None):
        return emp_obj.list_employee(id)


@app.post("/add")
def add_employee(employee:EmployeeModel):
        id=employee.id
        name=employee.name
        age=employee.age
        company=employee.company
        return emp_obj.add_employee(id,name,age,company)


@app.delete("/delete")
def delete_employee(id:int):
        return emp_obj.delete_employee(id)

@app.put("/update")
def update_employee(id:int,name:str):
        return emp_obj.update_employee(id,name.capitalize())