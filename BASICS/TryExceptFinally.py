try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")

except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero is not allowed.")

except ValueError:
    # Handle another specific exception
    print("Error: Invalid input. Please enter a valid number.")

finally:
    # Cleanup or final actions
    print("Execution of the program is complete.")

