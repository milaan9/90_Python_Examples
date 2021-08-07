'''
Python Program to Create Digital Clock
by Dr. Milaan Parmar
'''
# Import necessary modules!
from tkinter import *
from tkinter.ttk import *

# Import time
from time import strftime

# Create UI for our digital clock.
root = Tk()

# Set the title of our clock using title method.
root.title("Digital clock")

# Define a clock function to get the time
# Use strftime method to get the time and store it inside a string and name the string as tick
def clock():
    tick = strftime("%H:%M:%S %p")
    
    # Set the label using config method.
    label.config(text =tick)

    # Call our clock function and use the after method to do the same
    label.after(1000, clock)

# Use label method to store our title.    
label = Label(root, font = ("segoe", 60), foreground = "yellow", background = "black")

# Use pack method to pack our label
# Define the alignment of the label using the anchor method.
label.pack(anchor= "center")

# Call our clock function and at the end we will call it mainloop
clock()
mainloop()