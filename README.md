SIMPLE CALCULATOR APPLICATION

A user-friendly Python-based calculator app that performs basic arithmetic operations, saves calculations for future reference, and allows users to view previous calculations. This lightweight program is perfect for quick mathematical operations and maintaining a log of your calculations.

Features
- Perform Calculations: Supports addition, subtraction, multiplication, and division.
- Error Handling: Includes input validation for numbers and operations, preventing errors like division by zero.
- Save Results: Automatically saves all calculations in a text file (equations.txt) for future reference.
- View History: Displays previously performed calculations stored in equations.txt.
- User-Friendly Menu: Easy navigation through options to calculate, view history, or exit.

How It Works
- Input Validation: Users are prompted to enter valid numerical inputs.
- Operation Selection: Supports operations +, -, *, and /.
- Result Storage: Each calculation is saved in equations.txt in the format:
	number1 operation number2 = result.
- History Retrieval: Users can view previous calculations or start new ones.
- Persistent Storage: Even after the program is closed, calculations are preserved in equations.txt.
