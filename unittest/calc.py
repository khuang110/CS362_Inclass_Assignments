# In-Class Assignment 3
# Practice Unit Testing
# By: Kyle Huang

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def sub(x, y):
    return x - y


# This function multiplies two numbers
def mul(x, y):
    return x * y


# This function divides two numbers
def div(x, y):
    if y == 0:
        return "Undefined"
    else:
        return x / y


# Calculator function
def calc():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("Enter choice(1/2/3/4):")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", sub(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", mul(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", div(num1, num2))
    else:
        print("Invalid input!")


if __name__=="__main__":
    calc()