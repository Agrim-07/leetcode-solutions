a=input()
b=input()
l=[]
for i in a: 
    l.append(i)
for i in range (len(b)):
    if i>=len(a):
        l.insert(i,b[i])
    else:
        l.insert(i+1,b[i])
x=""
for i in l:
    x+=i
print(x)