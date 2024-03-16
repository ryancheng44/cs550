'''
Ryan Cheng
11/30/23
Sources: https://youtu.be/OKfra37r4D0?si=eOAzvAINT5CiT4Gh (Tkinter layout tutorial)
Reflection: I don't have much to say. I'm not sure how I feel about Tkinter. I don't think it gives me enough control over the layout of the
            GUI. It doesn't give me any margin or padding options unlike CSS.
On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

from tkinter import *
from tkinter import ttk

def calculate():
    # try to convert the user input into a float, otherwise do nothing
    try:
        value = float(feet.get())
        meters.set(0.3048 * value)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")
root.geometry("400x200")

# feet/user input is StringVar() simply for try/except purposes
feet, meters = StringVar(), DoubleVar()

# I choose to use the grid layout becaue I visualized the example GUI on the Canvas assignment as a table with 3 rows and 3 columns
ttk.Entry(root, textvariable=feet).grid(row=0, column=1)
ttk.Label(root, text="feet").grid(row=0, column=2)

ttk.Label(root, text="is equivalent to").grid(row=1, column=0)
ttk.Label(root, textvariable=meters).grid(row=1, column=1)
ttk.Label(root, text="meters").grid(row=1, column=2)

ttk.Button(root, text="Calculate", command=calculate).grid(row=2, column=2)

root.mainloop()