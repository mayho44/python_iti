inputs = ["aba", "aa", "ad", "vcd", "aba", "abca"]
maxi = -1
lst = []

for i in range(len(inputs)):
    if len(inputs[i]) > maxi:
        if len(lst) != 0:
            lst.pop()
            while lst and len(inputs[i]) > len(lst[-1]):
                lst.pop()
        lst.append(inputs[i])
        maxi = len(inputs[i])
    elif len(inputs[i]) == maxi:
        lst.append(inputs[i])

print(lst)