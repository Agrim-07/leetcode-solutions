list_of_strings=[]
number_of_strings_in_the_list=int(input("Enter number of strings in the array"))
for i in range(number_of_strings_in_the_list):
    print("Enter the string at position " + str(i+1) + " : ")
    list_of_strings.append(input())
