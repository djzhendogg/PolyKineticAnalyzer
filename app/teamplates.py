import customtkinter as cst
from commands import openfile
from tkinter import *


def place_upload_file(frame, all_entries_, add_row_state):
    add_row_state += 1
    file_upload_label = cst.CTkLabel(
        master=frame_1,
        text='File Uploading',
        width=450,
        font=label_font,
        justify=LEFT,
        anchor=cst.W
    )
    file_upload_label.grid(row=add_row_state, column=0, columnspan=2, padx=(40, 10), pady=(30, 0))

    filepath_var = StringVar()

    filepath_input = cst.CTkEntry(
        master=frame_1,
        textvariable=filepath_var,
        placeholder_text='file path',
        width=300,
        height=50,
        fg_color='#E0E2F0',
        placeholder_text_color='#000000',
        border_width=1,
        font=into_text_font,
        border_color='#888B9E'
    )
    filepath_input.grid(row=add_row_state + 1, column=0, padx=(40, 10), pady=0)

    filepath_button = cst.CTkButton(
        master=frame_1,
        width=130,
        height=50,
        text='Open',
        command=openfile,
        fg_color='#575A6C',
        corner_radius=10,
        hover_color='#888B9E',
        font=button_text_font
    )
    filepath_button.grid(row=add_row_state + 1, column=1, padx=(10, 10), pady=10)

    # Heating\cooling  rate
    heat_cool_label = cst.CTkLabel(
        master=frame_1,
        text='Heating\cooling  rate',
        width=450,
        font=label_font,
        justify=LEFT,
        anchor=cst.W
    )
    heat_cool_label.grid(row=add_row_state + 2, column=0, columnspan=2, pady=(10, 0), padx=(40, 10))

    heat_cool_input = cst.CTkEntry(
        master=frame_1,
        width=300,
        height=50,
        fg_color='#E0E2F0',
        placeholder_text_color='#000000',
        font=into_text_font,
        border_width=1,
        border_color='#888B9E'
    )
    heat_cool_input.grid(row=add_row_state + 3, column=0, padx=(40, 10), pady=10)

    heat_cool_combobox = cst.CTkComboBox(
        master=frame_1,
        values=['K/min', 'K/s', 'C/min', 'C/s'],
        width=130,
        height=50,
        font=into_text_font,
        fg_color='#E0E2F0',
        border_color='#888B9E',
        border_width=1,
        dropdown_font=into_text_font,
        dropdown_fg_color='#E0E2F0',
        button_color='#575A6C',
        button_hover_color='#888B9E',
    )
    heat_cool_combobox.set("K/min")
    heat_cool_combobox.grid(row=add_row_state + 3, column=1, padx=(10, 10), pady=10)

    all_entries.append((
        file_upload_label, filepath_input, filepath_button,
        heat_cool_label, heat_cool_input, heat_cool_combobox
    ))
