a=input()
b=a.split()
c=""
for i in range(len(b)):
    b[i].reverse()
    c+=(b[i]+" ")
print(c)

