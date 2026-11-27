a=input()
b=input()
s=""
j=0
i=0
for x in range (len(a)+len(b)):
    if x%2==0:
        s+=a[i]
        i+=1
    else:
        s+=b[j]
        j+=1
print(s)