while(True):
  str = input("enter a string: ")
  if(str.isdigit()):
    print("enter a charcters")
    continue
  else:
    break
vowel = 0
for i in range(0, len(str)):
  if str[i].lower() =='a' or str[i].lower() =='u' or str[i].lower() == 'o' or str[i].lower() == 'i' or str[i].lower() == 'y' or str[i].lower() == 'e':
   vowel += 1
print(f"number of vowels in your string {vowel}")

if str.find('i') == -1: print("there is no i in your string")
else: print(f" the location of your first i is {str.find('i') }")

