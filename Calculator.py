a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("""
========= Calculator =========
1. Addition
2. Division
3. Multiplication
4. Percentage
5. Subtraction
==============================
""")

choice = input("Choose an operation (1-5): ")

if choice == '1':
    print(f"Result: {a + b:.2f}")

elif choice == '2':
    if b != 0:
        print(f"Result: {a / b:.2f}")
    else:
        print("Division by zero is not allowed.")

elif choice == '3':
    print(f"Result: {a * b:.2f}")

elif choice == '4':
    if (a + b) != 0:
        print(f"Percentage of A: {(a/(a+b))*100:.2f}%")
        print(f"Percentage of B: {(b/(a+b))*100:.2f}%")
    else:
        print("Cannot calculate percentage because the total is 0.")

elif choice == '5':
    print(f"Result: {a - b:.2f}")

else:
    print("Invalid choice! Please select a number between 1 and 5.")


    