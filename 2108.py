list_of_strings=[]
number_of_strings_in_the_list=int(input("Enter number of strings in the array"))
for i in range(number_of_strings_in_the_list):
    print("Enter the string at position " + str(i+1) + " : ")
    list_of_strings.append(input())
h=0
for i in list_of_strings:
    if i[::1]==i[::-1]:
        print(i)
        h+=1
        break
if h==0:
    print("")