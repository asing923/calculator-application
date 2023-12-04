# calculator-application

**Calculator App** is a compact Python application built with Tkinter, featuring both Infix and RPN modes for versatile mathematical computations.

## Infix Mode

In the Infix mode, the calculator adheres to the order of operations, giving priority to multiplication and division over addition and subtraction. Users can enjoy an interactive experience with step-by-step results. For instance, inputting { '3' '+' '(' '5' '-' '2' ')' 'x' '7' '=' } would display '1', '5', '2', '3', '7', and finally, '24'.

## RPN Mode

Switching to RPN mode, the calculator operates with Reverse Polish Notation, incorporating 'enter' instead of '='. For example, entering {'3' 'enter' '5' 'enter' '2' '-' '+' '7' 'x'} would produce '1', '5', '2', '3', '4', '7', and '42'.

## Additional Features

- Acceptance of decimal point '.' for handling both integers and floats.
- Convenient 'CE' and 'CE/C' keys for clearing entries.
- Memory functionality includes 'MS' (store), 'MR' (recall), and 'MC' (clear).

## Tech Stack

- **Language:** Python
- **GUI Library:** Tkinter
