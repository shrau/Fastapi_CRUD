from service.employee.employee import Employee
emp_obj=Employee()
while True:
    

    op= int(input("\nselect operation\n1.Add Employee\n2.List Operation\n3.Delete Employee\n4.Update Employee\n"))
    if op==1:
        id,name,age,company=input("\nPlease fill the detail = ").split(',')
        print(emp_obj.add_employee(int(id),name.capitalize(),age,company))
    elif op==2:
        id=(input("\nEnter the specific id or * for all record = "))
        if id=='*':
            print(emp_obj.list_employee())
        else:
            print(emp_obj.list_employee(int(id)))
    elif op==3:
        id=(input("\nEnter the specific id to delete "))
        print(emp_obj.delete_employee(int(id)))
    elif op==4:
        id,update_name=input("\nEnter the id and name ").split(',')
        print(emp_obj.update_employee(int(id),update_name.capitalize()))








    

