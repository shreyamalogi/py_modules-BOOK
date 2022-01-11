# references
# http://tcl.tk/man/tcl8.6/TkCmd/pack.htm    pack
# https://docs.python.org/3/library/tkinter.html#the-packer  docs

# import tkinter
# from typing import Text

#tinkter.<class name> to import singly 



#turtle
import turtle
tim = turtle.Turtle()
tim.write("shreya", font = ("Times New Roman", 80, "bold"))                         #arguments with default values


#tkinter
from tkinter import *                   # to import all the classes of tkinter

window = Tk()
window.title("my first GUI program")
window.minsize(width = 500, height = 300)

#label
my_label = Label(text = "I am label", font = ("Arial", 24, "bold"))         #create component (L is capital )
my_label.pack(expand=True)                                                          #to display in center           #call the method pack to print the above code


#change the label name
my_label["text"] = "New text"
my_label.config(text = "New Text")


#buttons

def button_clicked():                           #event listners
    print("I got clicked")                      #this message will appear in terminal
    new_text = input.get()                      #get methods holds the input
    my_label.config(text = new_text)            #new_text prints the value of input to output


button = Button(text = "click me", command = button_clicked)
button.pack()


#entry
input = Entry(width = 20)                    #to get an input box
input.pack()
print(input.get())                           #to get hold of the input value as a string and print it

button_clicked()














window.mainloop()