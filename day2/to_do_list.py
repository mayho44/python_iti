def verify(op):
 flag = input(f"{op} this task? (yes or no): ")
 flag = flag.lower()
 if(flag == "yes"):
  return True
 else :
  return False

nums_of_checked = 0

def add():
 task = input("enter your new task: ")
 to_do_list[task] = ""
 map_lists[len(to_do_list)] = task
 global nums_of_checked 
 print(f"you added [ {task} ] sucessfully")
 if verify("check"): 
  to_do_list[task] = True
  nums_of_checked += 1
 show()

def delete():
 if len(to_do_list) == 0:
  print("----------------------------")
  print("can't perform this operation because your queue is empty")
 
  return
 while(True):
  task_del = input("enter the number of the tak you want to delete: ")
  if task_del.isdigit() and 1<= int(task_del) <= len(to_do_list):
   if(verify("delete")==False):
    show()
    return
   #actually deleteing
   to_do_list.pop(map_lists[int(task_del)])
   map_lists.pop(int(task_del))
   print("you're task is deleted sucessfully")
   show()
   break
  else:
   print("please enter a valid task number")



def show():
 if len(to_do_list) == 0:
  print("----------------------------")
  print("No available tasks :/")
  return
 i = 0
 print("you available tasks : ")
 print("----------------------------")
 for op , check in to_do_list.items():
  i += 1
  print(f"{i}) {op}", end="\t")
  if check == True :print("✔")
  else: print("")

to_do_list = {}
map_lists = {}

def update():
  if len(to_do_list) == 0:
   print("----------------------------")
   print("can't perform this operation because your queue is empty")
   
   return
  while(True):
   task_upd = input("enter the number of the task you want to update: ")
   if task_upd.isdigit() and 1<= int(task_upd) <= len(to_do_list):
    updated_task = input(f"update task {map_lists[int(task_upd)]}: ")
    if(updated_task ==''):updated_task = map_lists[int(task_upd)]
    if(verify("update") == False): 
     show()
     return
   #actually updating
    to_do_list.pop(map_lists[int(task_upd)])
    map_lists.pop(int(task_upd))
    to_do_list[updated_task] = ""
    map_lists[len(to_do_list)] = updated_task
    global nums_of_checked 
    if verify("check"): 
     to_do_list[updated_task] = True
    nums_of_checked += 1
    print("you're task is updated sucessfully")
    show()
    break
   else:
    print("please enter a valid task number")

def check():
 if not to_do_list:
  print("----------------------------")
  print("can't perform this operation because your queue is empty")
  return
 
 global nums_of_checked 
 while(True):
  if(nums_of_checked == len(to_do_list)):
   print("*********all tasks are checked************ ")
   show()
   break
  task_check = input("enter the number of the task you want to check: ")
  if task_check.isdigit() and 1<= int(task_check) <= len(to_do_list):
   to_do_list[map_lists[int(task_check)]] = True
   nums_of_checked += 1
   print("you're task is marked as done sucessfully")
   show()
  else:
   print("please enter a valid task number")
   

  
  
 
 
def operations():
 print("avaliable to do list operations : ")
 ops = ("show","add","delete", "update","check", "stop")
 for  index, value in enumerate(ops):
  index += 1
  print(str(index) + " : " + value)
 
while(True):
  # flag = False
  operations()
  while(True):
   query = input("enter your operation : ")
   if query.isdigit() and 1<= int(query) <= 6:
    break
   else : print("enter a valid operation number: ")
  match query:
    case "1":
     show()
     print("----------------------------")

    case "2":
     add()
     print("----------------------------")

    case "3":
     delete()
     print("----------------------------")

    case "4":
     update()
     print("----------------------------")

    case "5":
     check()
     print("----------------------------")

    case "6":
     flag = True
     break
  













 



 


  






