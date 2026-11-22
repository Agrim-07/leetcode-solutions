s = input()
seen = []
answer = -1
for i in range(len(s)):
    ch = s[i]
    if ch in seen:
        continue
    if ch in s[i+1:]:
        seen.append(ch)
    else:
        answer = i
        break
print(answer)