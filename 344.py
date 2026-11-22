a = input()
s = list(a)                 # strings can't be changed in place, so make a list of characters
left = 0
right = len(s) - 1
while (left < right):
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
print("".join(s))           # join the characters back into one string