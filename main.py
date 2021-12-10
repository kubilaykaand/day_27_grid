from tkinter import *

#Creating a new window and configurations
window = Tk()
window.minsize(width=500, height=500)
window.config(padx=100,pady=200)

#Labels
label=Label(text="this is old",font=("Arial",8,"bold"))
label.config(text="This is new")
#label.place(x=100,y=200)
label.grid(column=0, row=0)
label.config(padx=50,pady=50)

def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me",
                command=action)
button.grid(column=1, row=1)

#Entries
entry = Entry(width=30)
#add some text
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
#puts the entry to the box
entry.grid(column=2,row=2)

#text
text = Text(height=5,width =30)
#puts cursor in textbox
text.focus()
#add some text to begin with
text.insert(END, "Example of multi-line text entry.")
#Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
#text.pack()
text.grid(column=3,row=3)

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox= Spinbox(from_=0, to=10, width=5,
                 command=spinbox_used)
spinbox.grid(column=4,row=5)

def scale_used(value):
    print(value)
scale=Scale(from_=0, to=100,
            command=scale_used)
scale.grid(column=5,row=5)

#Checkbutton
def checkbutton_used():
    #Print 1 if On button checked, otherwise0.
    print(checked_state.get())
#variable to hold on to checked state,0 is off,1 is on.
checked_state = IntVar()
checkbutton= Checkbutton(text="Is On?",
                         variable=checked_state,
                         command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=7,row=5)
def new_button():
    print(new_but_call.get())
new_but_call=Button(text="New Butt",
                command=action)
new_but_call.grid(column=2,row=0)
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1",value=1, variable=radio_state,
                           command=radio_used)
radiobutton2=Radiobutton(text="Option2",
                         value=2, variable=radio_state,command=radio_used)
radiobutton1.grid(column=10,row=5)
radiobutton2.grid(column=11,row=5)

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox= Listbox(height=4)
fruits = ["Apple","Pear","Orange","Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.grid(column=11,row=11)
window.mainloop()