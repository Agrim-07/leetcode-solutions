a = int(input())
l = []
for i in range(a):
    l.append(input())
c = 0
i = 0
while (i < a):
    e = len(l[i].split())
    if e > c:
        c = e
    i += 1
print(c)