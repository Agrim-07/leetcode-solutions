a=input()
b=input()
l=[]
j=0
for i in a: 
    l.append(i)
for i in range (len(b)+len(a)):
    if i>=len(a):
        l.append(b[i])
    else:
        if i%2==1:
            l.insert(i,b[j])
            j+=1
x=""
for i in l:
    x+=i
print(x)