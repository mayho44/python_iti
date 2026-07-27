list = [
    "Ahmed",
    "Sara",
    "Omar",
    "Laila",
    "Yassin",
    "Mona",
    "Kareem",
    "Noor",
    "Hassan",
    "Fatima",
    "Ali",
    "Zainab",
    "Mohamed",
    "Aisha",
    "Youssef",
    "Salma",
    "Ibrahim",
    "Nadia",
    "Hussein",
    "Layla"
]
dict = {
    "a": [],
    "b": [],
    "c": [],
    "d": [],
    "e": [],
    "f": [],
    "g": [],
    "h": [],
    "i": [],
    "j": [],
    "k": [],
    "l": [],
    "m": [],
    "n": [],
    "o": [],
    "p": [],
    "q": [],
    "r": [],
    "s": [],
    "t": [],
    "u": [],
    "v": [],
    "w": [],
    "x": [],
    "y": [],
    "z": []
}
for i in list:
  dict[i[0].lower()].append(i)
for key,value in dict.items() :
  if len(value) == 0: continue
  else:print(f"{key} : {value}")
  