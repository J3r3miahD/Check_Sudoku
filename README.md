# Sudoku Validator

This Python project validates a Sudoku solution by checking the following rules:

1. **Matrix Validity**: Ensures the input matrix is 9x9 and contains only numbers between 1 and 9.
2. **Row Validity**: Checks if each row contains unique numbers (1-9) with no duplicates.
3. **Column Validity**: Ensures each column contains unique numbers (1-9) with no duplicates.
4. **3x3 Square Validity**: Ensures each 3x3 sub-grid (square) contains unique numbers (1-9) with no duplicates.

## Features

- Checks if the given Sudoku grid is a valid solution.
- Validates rows, columns, and 3x3 sub-grids for duplicate numbers.
- Provides feedback on whether the solution is valid or not.
- Prints the Sudoku matrix provided by the user.

## How to Use

1. Clone this repository or download the `sudoku_validator.py` file.
2. Run the Python script.
3. Enter the Sudoku matrix row by row when prompted. Each row should contain 9 integers separated by spaces (e.g., `5 3 4 6 7 8 9 1 2`).
4. The script will check if the input matrix is a valid Sudoku solution and will print the result.

## Example
 
Sudoku row 1: 5 3 4 6 7 8 9 1 2 Sudoku row 2: 6 7 2 1 9 5 3 4 8 Sudoku row 3: 1 9 8 3 4 2 5 6 7 Sudoku row 4: 8 5 9 7 6 1 4 2 3 Sudoku row 5: 4 2 6 8 5 3 7 9 1 Sudoku row 6: 7 1 3 9 2 4 8 5 6 Sudoku row 7: 9 6 1 5 3 7 2 8 4 Sudoku row 8: 2 8 7 4 1 9 6 3 5 Sudoku row 9: 3 4 5 2 8 6 1 7 9

Solution Valid 5 3 4 6 7 8 9 1 2 6 7 2 1 9 5 3 4 8 1 9 8 3 4 2 5 6 7 8 5 9 7 6 1 4 2 3 4 2 6 8 5 3 7 9 1 7 1 3 9 2 4 8 5 6 9 6 1 5 3 7 2 8 4 2 8 7 4 1 9 6 3 5 3 4 5 2 8 6 1 7 9