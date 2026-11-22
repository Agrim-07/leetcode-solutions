a = input()
b = a.find("b")
if b == -1:
    print("true")
else:
    c = 0
    for i in range(b + 1, len(a)):
        if a[i] == "a":
            c += 1
    if c == 0:
        print("true")
    else:
        print("false")