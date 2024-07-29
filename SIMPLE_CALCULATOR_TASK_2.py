def simple_calculator():
        print("Enter '+' to perform addition")
        print("Enter '-' to perform substraction")
        print("Enter '*' to perform multiplication")
        print("Enter '/' to perform divisison")
        print("Enter 'Exit' to end the program")
        user = input("Enter the operation that you want to perform: ")
        while user == "Exit":
            break
        if user in ["+", "-", "*", "/"]:
            n1 = float(input("Enter the First Number: "))
            n2 = float(input("Enter the Second number: "))
            if user == "+":
                result = n1 + n2
                print(n1, "+", n2, "=", result)
            elif user == "-":
                result = n1 - n2
                print(n1, "-", n2, "=", result)
            elif user == "*":
                result = n1 * n2
                print(n1, "*", n2, "=", result)
            elif user == "/":
                result = n1 / n2
                print(n1, "/", n2, "=", result)
        else:
            print("No such operations can be performed! ")
simple_calculator()