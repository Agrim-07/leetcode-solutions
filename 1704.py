a=input()
c=d=0
b=len(a)
for i in range(0,b//2,1):
    if (a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U"):
        c+=1
for i in range(b//2,b,1):
    if (a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U"):
        d+=1
if c==d:
    print("True")
else:
    print("False")