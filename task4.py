
while(True):
  user_name = input("enter your name: ")
  user_name = user_name.strip()
  if len(user_name) < 3 or user_name == "" or user_name.isdigit():
    print("enter valid user name")
    continue
  else : break
while(True):
  email = input("enter your email: ")
  email = email.strip()
  if("@" in email and email != "" and len(email) > 10):
    print("valid email")
    break
  else: 
    print("invalid email")
    continue



