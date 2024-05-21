import customtkinter as cst
from tkinter import *


def uploaded_files_names(file_name, frame, row):
    button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=20, weight='bold')
    label_font = cst.CTkFont(family="Microsoft PhagsPa", size=18, )
    filepath_lable = cst.CTkLabel(
        master=frame,
        width=280,
        text=file_name,
        font=label_font,
        justify=LEFT,
        anchor=cst.W
    )
    filepath_lable.grid(row=row, column=1, padx=(20, 0), pady=(20, 0))

    delete_row_button = cst.CTkButton(
        master=frame,
        width=60,
        height=40,
        text='delete',
        fg_color='#575A6C',
        command=filepath_lable.destroy,
        corner_radius=10,
        hover_color='#888B9E',
        font=button_text_font
    )

    delete_row_button.grid(row=row, column=2, padx=(20, 0), pady=(20, 0))
