import os
from tkinter import *
from tkinter import filedialog, ttk
from main import calculate

wordir = os.getcwd()


def openfile(text_var):
    filepath = filedialog.askopenfilename(
        initialdir=wordir,
        title="Open file okay?",
        filetypes=(
            ("text files", "*.txt"), ("all files", "*.*")
        )
    )
    text_var.set(str(filepath))
