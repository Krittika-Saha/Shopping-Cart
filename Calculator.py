def calc(a, b, operator):
    if operator == "-":
        print(a - b)
    elif operator == "+":
        print(a + b)
    elif operator == "*":
        print(a * b)
    

calc(int(input("Enter first no.: ")), int(input("Enter second no.:")), input("Enter operator:"))
