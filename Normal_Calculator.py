print("what type of operation do you choose? \n"
      "type + for addition\n"
      "type - for substraction\n"
      "type * for multiplication\n"
      "type / for division \n")

type_of_calculation =input()
print ("enter the first number")
A =int(input())
print("enter the second number")
B =int(input())

a ="+"
b ="-"
c ="*"
d ="/"

if type_of_calculation == a :
    print(A+B)
elif type_of_calculation ==b :
    print(A-B)
elif type_of_calculation ==c :
    print(A*B)
elif type_of_calculation == d:
    print(A/B)

