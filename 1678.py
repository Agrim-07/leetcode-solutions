a = input()
result = ""
i = 0
while (i < len(a)):
    match a[i]:
        case 'G' | 'g':
            result += 'G'
            i += 1
        case '(':
            match a[i+1]:
                case ')':
                    result += 'o'
                    i += 2
                case 'a' | 'A':
                    result += 'al'
                    i += 4
                case _:
                    i += 1
        case _:
            i += 1
print(result)