a=input()
c=d=0
for i in range(len(a)//2):
    if (a[i]=='a'||a[i]=='e'||a[i]=='i'||a[i]=='o'||a[i]=='u'||
       a[i]=='A'||a[i]=='E'||a[i]=='I'||a[i]=='O'||a[i]=='U'):
        c+=1
for i in range(len(a)//2,len(a)):
    if (a[i]=='a'||a[i]=='e'||a[i]=='i'||a[i]=='o'||a[i]=='u'||
       a[i]=='A'||a[i]=='E'||a[i]=='I'||a[i]=='O'||a[i]=='U'):
        d+=1
if c==d:
    print("True")
else:
    print("False")