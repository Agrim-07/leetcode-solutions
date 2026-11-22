a = input()
s = ""
for i in a:
    if i == ".":
        s += "[.]"
    else:
        s += i
print(s)