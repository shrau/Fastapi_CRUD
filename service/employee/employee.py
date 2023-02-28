from service.database.database import DatabaseOperations
class Employee:

    def __init__(self):
        self.db_operation=DatabaseOperations()


    def add_employee(self, id:int, name:str, age:int, company:str):
        try:
            
            sql = f"INSERT INTO employee.employee_details(id,name,age,company) VALUES ({id},'{name}',{age},'{company}')"
            cursor=self.db_operation.execute_query(sql)
            
            self.db_operation.commit_connection()
            return {
                'status': 'Success',
                'result': f"Employee with following details: {id}, {name}, {age}, {company} is inserted."
            }
        except Exception as e:
            return {
                'status': 'Failed',
                'result': str(e)
            }


    def list_employee(self,id:int=None):
        try:

            where_clause=f"where id={id}" if id else ""
            query=f"SELECT * FROM employee.employee_details {where_clause}"

            cursor=self.db_operation.execute_query(query)

            myresult=cursor.fetchall()


            return {
                    'status': 'Success',
                    'result': myresult
            }
        except Exception as e:
            return {
                'status':'Failed',
                'result':str(e)
            }


    def delete_employee(self,id):
        try:
            sql = f"DELETE FROM employee.employee_details WHERE id={id}"

            cursor=self.db_operation.execute_query(sql)

            self.db_operation.commit_connection()

            return{
                        'status':'success',
                        'result':f"Employee with id = {id} deleted"
                      }

        except Exception as e:
            return{
                'status':'Failed',
                'result': str(e)            
            }

    def update_employee(self,id,updated_name):
        
        try:
            sql = f"UPDATE employee.employee_details SET name='{updated_name}' WHERE id={id}"

            cursor=self.db_operation.execute_query(sql)

            self.db_operation.commit_connection()
            
            return{
                        'status':'Success',
                        'result':f"Name is updated by {updated_name}"
                }
            
        except Exception as e:
            return{
            'status':'Failed',
            'result': str(e)
            }
                   






