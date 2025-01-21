print("A program created to perform simple calculations and print them.")


# A function used to validate user input for a number as a float.
def input_valid_number(prompt):
    """
    Prompt the user to input a valid number, ensuring proper error handling.

    Continuously asks the user for input until a valid number is provided.
    Converts the input to a float and returns it.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        float: The valid number input by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Function for calculations based on user inputs.
def perform_calculation():
    """
    Perform a basic arithmetic calculation and save the result to a file.

    Prompts the user for two numbers and an arithmetic operation
    (+, -, *, /). Performs the specified operation and displays the result.
    If the operation is valid, saves the calculation to a file named
    'equations.txt'.

    Workflow:
    1. Prompts the user to input two numbers using the `input_valid_number`
    function.
    2. Prompts the user for an operation (+, -, *, /).
    3. Validates the operation and performs the calculation.
    4. Handles division by zero if the '/' operation is chosen.
    5. If the operation is valid, saves the calculation in the format:
       "<num1> <operation> <num2> = <result>"
       to 'equations.txt', creating the file if it does not exist.
    """
    num1 = input_valid_number("Enter 1st number: ")
    operation = input("Enter an operation (+, -, *, /): ")
    num2 = input_valid_number("Enter 2nd number: ")

    # Results always calculated in respect to user input.
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Check for division by zero before getting result.
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    # Check performed to validate if correct operation selected.
    else:
        print("Invalid operation. Please enter one of +, -, *, or /.")
        return

    # Variable equation created to store full calculation performed.
    equation = f"{num1} {operation} {num2} = {result}"
    print(f"Result: {equation}")

    # Save the equation to equations.txt
    with open("equations.txt", "a") as file:
        # File opened for writing, file created if it does not exist.
        file.write(equation + "\n")


# Function created to read from equations.txt and print equations.
def print_previous_equations():
    """
    Display previous calculations saved in 'equations.txt'.

    Reads and prints all the equations from the 'equations.txt' file.
    If the file does not exist or is empty, appropriate messages are displayed.
    Handles potential errors during the file reading process.

    Workflow:
    1. Attempts to open 'equations.txt' in read mode.
    2. Reads all lines from the file.
        - If lines are found, prints each saved calculation.
        - If the file exists but is empty, notifies the user.
    3. Handles the following exceptions:
        - FileNotFoundError: If 'equations.txt' does not exist.
        - Other exceptions: If any error occurs while reading the file.
    """
    try:
        with open("equations.txt", "r") as file:
            equations = file.readlines()
            if equations:
                print("Previous calculations:")
                for equation in equations:
                    print(equation.strip())
            else:
                print("No previous calculations found.")

    # Exceptions created if user has no input for calculations.
    except FileNotFoundError:
        print("No previous calculations found (equations.txt does not exist).")
    except Exception as err:
        print("An error occurred while reading the file:", err)


# Function created in order to maintain loop for user inputs based on choices.
def main():
    while True:
        print("\nCalculator Menu:")
        print("1. Perform a calculation")
        print("2. Print previous equations")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        # Used to call perform_calculation function.
        if choice == '1':
            perform_calculation()
        # Used to call print_previous_equations function.
        elif choice == '2':
            print_previous_equations()
        # Used to stop program.
        elif choice == '3':
            print("Exiting the calculator.")
            break
        # Check performed to validate user input choice.
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Statement created to always bring user back to the main function.
if __name__ == "__main__":
    main()
