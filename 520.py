word = input()
count = 0
for ch in word:
    if ch.isupper():
        count += 1
if count == len(word):
    print(True)
elif count > 1:
    print(False)
elif count == 1:
    if word[0].isupper():
        print(True)
    else:
        print(False)
elif count == 0:
    print(True)