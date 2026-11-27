a=input()
b=input()
l=[]
for i in a: 
    l.append(i)
for i in range (len(b)):
    if i>=len(a):
        l.append(b[i])
    else:
        if i%2==1:
            l.insert(i,b[i])
x=""
for i in l:
    x+=i
print(x)