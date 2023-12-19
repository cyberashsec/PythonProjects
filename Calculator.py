num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
operation = input("What type of operation would you like to do? ")

if operation == "+":
    result = float(num1)+float(num2)
elif operation == "-":
    result = float(num1)-float(num2)
elif operation == "*":
    result = float(num1)*float(num2)
elif operation == "/":
    result = float(num1)/float(num2)

print(round(result, 1))
print(input(""))
