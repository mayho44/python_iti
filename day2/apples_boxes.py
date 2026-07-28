apple = [5, 1, 2]
capacity = [4, 3, 7, 9]
capacity.sort(reverse=True)
boxes_used = 0
amount = 0
flag = False
sum_apples = sum(apple)
for i in capacity:
  if(boxes_used >= sum_apples):
    flag = True
    break
  amount += i
  boxes_used += 1
if flag == True:
  print(boxes_used)
else:
  print("not enough boxes")