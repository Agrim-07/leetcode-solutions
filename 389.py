s = input()
t = input()
count_s = {}
count_t = {}
for i in range(26):
    letter = chr(97 + i)  
    count_s[letter] = 0
    count_t[letter] = 0
for ch in s:
    count_s[ch] += 1
for ch in t:
    count_t[ch] += 1
for letter in count_t:
    if count_t[letter] > count_s[letter]:
        print(letter)
        break