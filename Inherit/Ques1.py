class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def display(self):
      print("Id:",self.emp_id,"name:",self.name,"Salary:",self.salary)
class Manager(Employee):
    def __init__(self,emp_id,name,salary,department):
        super().__init__(emp_id,name,salary)
        self.department=department

    def display(self):
        super().display() 
        print("Department:",self.department)
    def annual_salary(self):
        return self.salary*12

mgr=Manager("T3","Nikhil",45000,"IT")   
mgr.display()
print("Annual Salary:",mgr.annual_salary())             