print("Select operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
choice = input("Enter choice (1/2/3/4/5): ")

if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            z = x + y
            print(x, "+", y, "=", z)
        elif choice == '2':
            z = x - y
            print(x, "-", y, "=", z)
        elif choice == '3':
            z = x * y
            print(x, "x", y, "=", z)
        elif choice == '4':
            z = x / y
            print(x, "/", y, "=", z)
        elif choice == '5':
            z = x % y
            print(x, "%", y, "=", z)  
    except Exception as e:
        print("Error: ", e)
else: 
    print("Please enter a number between (1-5)")