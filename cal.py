num1 = int(input("input integer1: "))
num2 = int(input("input integer2: "))
op = input("input operator(+ / - / * / /): ")

if op == '+':
    print(num1, "+", num2, "=", num1 + num2)
elif (op == '-'):
    print(num1, "-", num2, "=", num1-num2)
elif (op == '*'):
    print(num1, "*", num2, "=", num1*num2)
elif (op == '/'):
    print(num1, "/", num2, "=", num1/num2)
else:
    print("error")