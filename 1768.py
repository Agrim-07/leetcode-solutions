a=input()
b=input()
s=""
i=len(a)
j=len(b)
k=0
l=0
if (i>j):
    for x in range (2*j):
        if x%2==0:
            s+=a[k]
            k+=1
        else:
            s+=b[l]
            l+=1
    for y in range (k,len(a)):
            s+=a[y]
else:
    for x in range (2*i):
        if x%2==0:
            s+=a[k]
            k+=1
        else:
            s+=b[l]
            l+=1
    for y in range (l,len(b)):
        s+=a[y]
print(s)