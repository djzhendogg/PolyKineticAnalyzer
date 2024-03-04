from tkinter import *

#------------------------------------

def addBox():
    print("ADD")

    frame = Frame(root)
    frame.pack()

    Label(frame, text='From').grid(row=0, column=0)

    ent1 = Entry(frame)
    ent1.grid(row=1, column=0)

    Label(frame, text='To').grid(row=0, column=1)

    ent2 = Entry(frame)
    ent2.grid(row=1, column=1)

    all_entries.append( (ent1, ent2) )

#------------------------------------

def showEntries():

    for number, (ent1, ent2) in enumerate(all_entries):
        print(number, ent1.get(), ent2.get())

#------------------------------------

all_entries = []

root = Tk()

showButton = Button(root, text='Show all text', command=showEntries)
showButton.pack()

addboxButton = Button(root, text='<Add Time Input>', fg="Red", command=addBox)
addboxButton.pack()

root.mainloop()
