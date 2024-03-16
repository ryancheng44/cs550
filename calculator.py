'''
Ryan Cheng
12/11/23
Sources: https://www.tutorialspoint.com/python/tk_grid.htm (padx, pady, ipadx, ipady, sticky)
         https://www.pythontutorial.net/tkinter/tkinter-grid/ (grid_columnconfigure,
         grid_rowconfigure)
Reflection: This assignment was actually more challenging than I thought and thoroughly tested my
            research skills. It was not hard to program the calculator itself, but I had to do a lot
            of research to figure out how to make the GUI look the way I wanted it to. I was already
            familiar with grid, but by default there is no padding and everything is centered, which
            I wanted to change. I tried using pack, but that just complicated things even more and
            made it worse. I went back to grid and eventually discovered padx, pady, ipadx, ipady,
            and sticky. From there, it was smooth sailing and I was able to tinker with the values
            to get the GUI to look how I wanted it to. In addition, to address Leon's comment about
            the GUI not updating when the window is resized, I did some research and found that I
            needed to use grid_columnconfigure and grid_rowconfigure. I'm starting to warm up to
            tkinter but still a bit apprehensive about it. 😔
Peer Reviews:
    1. Leon Gopaul: I liked your comments. They helped me understand your code a lot better,
                    especially the dictionary of operations. I also liked how you used the
                    dictionary to create the radio buttons. However, you may want to look into
                    having your widgets update automatically when you change the window size.
    2. Sebastian Plunkett: I liked how you used grid. Your GUI is well organized. However, you
                           may want to add a clear button just for user convenience.
On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

from tkinter import *
from tkinter import ttk

# Dictionary of operations (not necessary but makes the project more scalable)
operations = {
    "Add" : 0,
    "Subtract" : 1,
    "Multiply" : 2,
    "Divide" : 3
}

# Function to calculate the result
def calculate():
    # Try to convert the inputs to floats
    try:
        first = float(first_number.get())
        second = float(second_number.get())
        op = operation.get()
        # Compare value of operation to dictionary to determine which operation to perform
        if op == 0:
            result.set(first + second)
        elif op == 1:
            result.set(first - second)
        elif op == 2:
            result.set(first * second)
        elif op == 3:
            # If operation is division, check if second number is zero
            if second == 0:
                result.set("Cannot divide by zero")
            else:
                result.set(first / second)
    # If inputs are not numbers, set result to error message
    except ValueError:
        result.set("Please enter numbers only")

# Function to clear all inputs and result
def clear():
    first_number.set("")
    second_number.set("")
    operation.set(0)
    result.set("")

# Create the window
root = Tk()
root.title("Calculator")
root.geometry("425x125")

# Create input, operation, and result variables
first_number, second_number, operation, result = StringVar(), StringVar(), IntVar(), StringVar()

# First row
# sticky="w" means the widget is left-aligned within its grid cell ("n" = north, "e" = east, "s" =
# south, "w" = west), west = left
# padx is the padding on the left and right of the widget
ttk.Label(root, text="First Number").grid(row=0, column=0, sticky="w", padx=10)
# sticky="ew" means the widget is expanded horizontally to fill the entire cell
ttk.Entry(root, textvariable=first_number).grid(row=0, column=1, sticky="ew")

# Second row
ttk.Label(root, text="Second Number").grid(row=1, column=0, sticky="w", padx=10)
ttk.Entry(root, textvariable=second_number).grid(row=1, column=1, sticky="ew")

# Third row
# Added clear button for user convenience as suggested by Sebastian Plunkett
ttk.Button(root, text="Clear", command=clear).grid(row=2, column=0, sticky="w", padx=10)
ttk.Button(root, text="Calculate", command=calculate).grid(row=2, column=1)

# Fourth row
ttk.Label(root, text="Result").grid(row=3, column=0, sticky="w", padx=10)
ttk.Label(root, textvariable=result).grid(row=3, column=1)

# Operations in far right column
for (text, value) in operations.items():
    # For each operation in the dictionary, create a radio button with the text and value
    # ipady is the padding on the top and bottom of the widget
    ttk.Radiobutton(root, text=text, variable=operation, value=value).grid(row=value, column=2, sticky="w", ipady=5, padx=10)

# The following three lines of code update the GUI when the window is resized as suggested by Leon
# Gopaul

# This gives all the extra space to the second column (indexing starts at 0)
root.grid_columnconfigure(1, weight=1)

# This evenly distributes the extra space between the four rows
for i in range(4):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()