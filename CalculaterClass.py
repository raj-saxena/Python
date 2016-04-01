class Calculator:
    
    def __init__(self):
        print("calculator initialized")

    def addition(self, x, y):
        added = x + y
        return added

    def subtraction(self, x, y):
        subtracted = x - y
        return subtracted

    def multiplication(self, x, y):
        multiplied = x * y
        return multiplied

    def division(self, x, y):
        divided = x / y
        return divided

    def perform_operation(self):
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice of operation: ")

        x = int(input("Give the first no. ?"))
        y = int(input("Give the second no. ?"))

        if choice == 1:
            result = self.addition(x,y)
            print(result)

        elif choice == 2:
            result = self.subtraction(x,y)
            print(result)

        elif choice == 3:
            result = self.multiplication(x,y)
            print(result)

        elif choice == 4:
            result = self.division(x,y)
            print(result)

        else:
            print("Operation not found")

cal = Calculator()
cal.perform_operation()
