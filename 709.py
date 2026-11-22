a = input()
result = ""
for i in a:
    num = ord(i)
    if num in range(65, 91):
        num += 32
    result += chr(num)
print(result)