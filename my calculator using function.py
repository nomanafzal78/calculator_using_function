def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide (a,b):
    if b==0:
      return "error division by zero"
    return a/b

def get_numbers():
    a = float(input("Enter your 1st number: "))
    b = float(input("Enter your 2nd number: "))
    return a, b


def calculator():
    while True:
        print("\nSelect Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == 5:
           print ("exiting the calculator")
           break
        
        if choice in ['1', '2', '3', '4']:
           a,b = get_numbers() 
           
           if choice == '1':
                print(f"The result of addition: {add(a, b)}")
           elif choice == '2':
                print(f"The result of subtraction: {subtract(a, b)}")
           elif choice == '3':
                print(f"The result of multiplication: {multiply(a, b)}")
           elif choice == '4':
                print(f"The result of division: {divide(a, b)}")
        else:
          print("Invalid input. Please enter a number between 1 and 5.")
