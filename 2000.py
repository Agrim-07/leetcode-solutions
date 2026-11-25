a = input()
ch = input()
l = a.split(ch)
b = l[0]
c = len(b)
ans = ""
if c == len(a):
    print(a)
else:
    ans += (ch + b[::-1])
    for i in range(1, len(l)):
        ans += (l[i] + ch)
    if len(ans) > len(a):
        ans = ans[:len(a)]
    print(ans)