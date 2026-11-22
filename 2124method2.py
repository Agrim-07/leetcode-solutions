a = input()
b = a.find("b")
if b == -1:
    print("true")
else:
    c = a.find("a", b)
    if c == -1:
        print("true")
    else:
        print("false")