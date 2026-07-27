str = input("enter a string: ")
if(len(str) == 1): print(True)
else:
  if(len(str) % 2 == 0):
   if str[0:int(len(str) / 2)] == str[:-int(len(str) / 2)]:print(True)
   else:
    print(False)
  else :
    if str[0:int(len(str) / 2)] == str[:-int(len(str) / 2) - 1]:print(True)
    else:
      print(False)
   
# print(str[0:int(len(str) / 2)])
# print(str[:-(int(len(str) / 2))])
