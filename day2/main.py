#iterator
# iterable object
# my list =[1,2,34] => iterable object
# for i in my_list => i is iteratror
# *Args when i don't know the number of parameters and that astric tells me thaat, dadta is entered as a tuple
def user_information(*information):
  for i in information:
   print(i)

user_information(100,3556,True)
#**Kwargs data entered as a dictioary


def user_information(**information):
  for key,value in information.items():
   print(key + " " + value)
user_information(name="mariam", age=20)

######################3
pass #explain

