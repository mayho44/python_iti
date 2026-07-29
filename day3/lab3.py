id_lst=[]
update_lst = ["name", "age", "role", "rate"]
roles = ["full time", "part time", "Freelance"]
def check_id_existance(new_id):
  new_id = int(new_id)
  if id_lst == False:
    return False
  for i in id_lst:
    if i == new_id:
      return True
  return False

def updating(id, op_num):
  match op_num:
    case 1:
      while True:
       new_val = input("new_name: ").strip()
       if len(new_val) < 3 or new_val.isalpha() == False:
         print("please enter a valid name: ")
       else:
         Employee.update_employee(id,update_lst[op_num - 1],new_val)
         break
    case 2:
      while True:
       new_val = input("new_age: ").strip()
       if new_val.isdigit() and 16 <= int(new_val) <= 65:
        Employee.update_employee(id,update_lst[op_num - 1],int(new_val))
        break
       else: print("enter a valid age") 
    case 3:

      for i in range(len(roles)):
        print(f"{i + 1 }) {roles[i]}", end="\t")

      while True:
        new_val = input("\nenter your employee's role number: ").strip()
        if new_val.isdigit() and 1 <= int(new_val) <= 3:
          Employee.update_employee(id,update_lst[op_num - 1],roles[int(new_val) - 1])
          break
        else:print("Enter a valid operation number: ")
    case 3:
      while True:
       new_val = input("update hours worked/dayoffs/project completed")
       if new_val.isdigit() and int(new_val) >= 0:
         Employee.update_employee(id,update_lst[op_num - 1],roles[int(new_val) - 1])
         break
       else:print("enter a valid rate")
    
def validate_employee():
  dict = {}
  while True:
    id = input("enter employee's id: ").strip()
    if id.isdigit() and check_id_existance(id) == False: 
      dict["id"] = int(id)
      break
    else: print("enter a valid id ")
   
  while True:
    name = input("enter employee's name: ").strip()
    if name.isalpha() and len(name) >=3 : 
      dict["name"] = name
      break
    else :print("enter a valid name")

  while True:
    age = input("enter employee's age: ").strip()
    if age.isdigit() and 16 <= int(age) <= 65:
      dict["age"] = int(age)
      break
    else: print("enter a valid age ") 

  while True:
    print("-------------------")
    
    for i in range(len(roles)):
      print(f"{i + 1 }) {roles[i]}", end="\t")

    role = input("\nenter your employee's role number: ").strip()
    if role.isdigit() and 1 <= int(role) <= 3:
      dict["role"] = roles[int(role) - 1]
      break
    else:
      print("Enter a valid operation number: ")


  while True:
    rate = input("enter hours worked/dayoffs/projects completed : ").strip()
    if rate.isdigit() and int(rate) >= 0:
      dict["rate"] = int(rate)
      break
    else:print("enter a valid rate")
    
  return dict

################################classes

class Employee:
  employee_list=[]
  counter = 0
  def __init__(self, id, name, age, role, rate):
    self.id = id
    self.name = name
    self.age = age
    self.role = role
    self.rate = rate
    Employee.counter += 1
    self.employee_list.append(self)
    id_lst.append(self.id)
    
  @classmethod
  def display_all(cls):
    print("id \t name\t age\trole\t salary")
    for i in cls.employee_list:
     print(f"{i.id}\t{i.name}\t{i.age}\t{i.role}\t{i.calculate_salary():.4f}")
    
    
  def calculate_salary(self):
    return self.rate
  
  @classmethod
  def update_employee(cls,id ,op_name, new_val):
    for i in cls.employee_list:
      if i.id == id:setattr(i, op_name, new_val)
  
  @classmethod
  def get_report(cls):
    maxi = -1
    total_payroll = 0
    max_emp = []
    
    for emp in cls.employee_list:
      current_salary = emp.calculate_salary()
      total_payroll += current_salary
        
      if current_salary >= maxi:
        maxi = current_salary
        while max_emp and max_emp[-1].calculate_salary() < maxi:
          max_emp.pop()
        max_emp.append(emp)
    
    print("***  -- full report --   ***")
    print(f"total count of employees: {cls.counter}")
    print(f"total payroll: {total_payroll:.4f}")
    print("------------------------------------")
    print("employees with the highest salary")
    print("id \t name\t age\trole\t salary")
    for emp in max_emp:
     print(f"{emp.id}\t{emp.name}\t{emp.age}\t{emp.role}\t{emp.calculate_salary():.4f}")
  @classmethod
  def delete(cls, id):
    for emp in cls.employee_list:
      if emp.id == id:
        cls.employee_list.remove(emp)
        cls.counter -= 1
        return True
    return False
  
class FullTimeEmployee(Employee):
  monthly_salary = 100
  
  def __init__(self, id, name, age, role, rate):
    super().__init__(id, name, age, role, rate)
    self.days_off = rate

  def calculate_salary(self):
    return self.monthly_salary - self.monthly_salary*(self.days_off / 30)
  
  @classmethod
  def  display_all(cls):
    return super().display_all()
    
class PartTimeEmployee(Employee):
  hours_rate = 30
  def __init__(self, id, name, age, role, rate):
    super().__init__(id, name, age, role, rate)
    self.hours_worked = rate

  def calculate_salary(self):
    return self.hours_rate * self.hours_worked


class Freelancer(Employee):
  project_rate = 50
  def __init__(self, id, name, age, role, rate):
    super().__init__(id, name, age, role, rate)
    self.completed_projects = rate

  def calculate_salary(self):
    return self.project_rate * self.completed_projects  
  pass

ops = ["add employee", "diplay all employees", "update employee","delete", "get report","exit"]
while(True):
  print("------------------")
  print("available operations")
  print("---------------------------------------------------------")
  for i in range(len(ops)):
    print(f"{i + 1 }) {ops[i]}", end="\t")
  print("\n---------------------------------------------------------")
  query = input("enter your operation number: ")
  if query.isdigit() == False or 1 > int(query) and int(query) > len(ops):
    print("enter a valid operation number: ")
    continue
  match query:

    case "1":
      print("*** adding a new employee ***")
      result = validate_employee()
      # adding a match function to check on roles
      match result["role"]:
        case "full time":
          FullTimeEmployee(result["id"], result["name"], result["age"], result["role"], result["rate"])
        case "part time":
          PartTimeEmployee(result["id"], result["name"], result["age"], result["role"], result["rate"])
        case "Freelance" :
          Freelancer(result["id"], result["name"], result["age"], result["role"], result["rate"])
    case "2":
      print("***      --- ALL EMPLOYEES ---      ***")
      Employee.display_all()

      pass
    case "3":
      print("*** updating employee ***")
      print("--------------\navailable operations")
     
      for i in range(len(update_lst)):
        print(f"{i + 1 }) {update_lst[i]}", end="\t")
        op_num =''

      while True:
        op_num = input("\nenter your operation number: ").strip()
        if op_num.isdigit() and 1 <= int(op_num) <= 4:break
        else : print("enter a valid operation number")

      while True:
       selected_id = input("enter employee's id: ").strip()
       if selected_id.isdigit() and check_id_existance(selected_id):
        updating(int(selected_id), int(op_num))
        break
       else: 
        print("id doesn't exist")
    case "4":
      while True:
       selected_id = input("enter employee's id: ").strip()
       if selected_id.isdigit() and check_id_existance(selected_id):
        flag = input(f"are you sure you want to delete employee with {selected_id}: (Y / N)").strip().lower()
        if(flag == "n"):continue
        Employee.delete(int(selected_id))
        print("employee deleted sucessfuly")
        break
       else: print("id doesn't exist")

    case "5":
      Employee.get_report()
    case  "6":
      break

