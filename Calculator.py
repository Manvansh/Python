a = float(input("Enter 1st Number "))
b = float(input("Enter 2nd Number "))
print("Which function do you want to perform?")
print("1.+")
print("2.-")
print("3.*")
print("4./")
z = input()
if z == "1.+" or z == "1." or z == "+":
    c=a+b
    print("Addition of",a,"and",b,"is",c)
if z == "2.-" or z == "2." or z == "-":
    c=a-b
    print("Subtraction of",a,"and",b,"is",c)
if z == "3.*" or z == "3." or z == "*":
    c=a*b
    print("Multiplication of",a,"and",b,"is",c)
if z == "4./" or z == "4." or z == "/":
    c=a/b
    print("Division of",a,"and",b,"is",c)
print("Thank you for using calculator!")