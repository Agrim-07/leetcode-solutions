a=input()
b=a.split()
c=""
for i in range(len(b)):
    b[i]=b[i][::-1]
    c+=(b[i]+" ")
print(c)