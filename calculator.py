num1 =int(input("Enter first number: "))
num2 =int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case '+':
        print (num1 + num2)
    case '-':
        print (num1 - num2)
    case '*':
        print (num1 * num2)
    case '/':
        print (num1 / num2)
        