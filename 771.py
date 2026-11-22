jewels=input()
stones=input()
count=0
for s in stones:
    if s in jewels:
        count+=1
print(count)