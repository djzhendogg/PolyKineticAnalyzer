from tkinter import *
from tkinter import filedialog, ttk
import tkinter
import customtkinter as cst
import os
from main import calculate

wordir = os.getcwd()


def openFile():
    filepath = filedialog.askopenfilename(
        initialdir=wordir,
        title="Open file okay?",
        filetypes=(
            ("text files", "*.txt"), ("all files", "*.*")
        )
    )
    # r = calculate(filepath)
    # print(r)
    filepath_var.set(str(filepath))


cst.set_appearance_mode('light')
cst.set_default_color_theme('dark-blue')
app = cst.CTk()
app.title('PolyKineticAnalyzer')
app.geometry("1000x800")

# styles
button_text_font = cst.CTkFont(family="Arial Rounded MT Bold", size=20, weight='bold')
label_font = cst.CTkFont(family="Microsoft PhagsPa", size=18,)
into_text_font = cst.CTkFont(family="Bahnschrift SemiBold", size=20)

# frame settings
frame_1 = cst.CTkFrame(
    master=app,
    width=600,
    height=600,
    # fg_color='#FFFFFF'
)
frame_1.pack(padx=(40, 0))
frame_1.place(x=0, y=0)

frame_1.grid(row=0, column=0)
# temp_mode

temp_mode_label = cst.CTkLabel(
    master=frame_1,
    text='Temperature mode',
    width=420,
    font=label_font,
    justify=RIGHT,
    anchor=cst.W
)
temp_mode_label.grid(row=0, column=0, columnspan=2, padx=(40, 10), pady=(30, 0))

temp_mode_combobox = cst.CTkComboBox(
    master=frame_1,
    values=['cooling', 'heating'],
    width=420,
    height=50,
    font=into_text_font,
    fg_color='#E0E2F0',
    border_color='#888B9E',
    border_width=0,
    dropdown_font=into_text_font,
    dropdown_fg_color='#E0E2F0',
    button_color='#575A6C',
    button_hover_color='#888B9E',
)
temp_mode_combobox.set("cooling")
temp_mode_combobox.grid(row=1, column=0, columnspan=2, padx=(40, 10), pady=10)


# File Uploading
file_upload_label = cst.CTkLabel(
    master=frame_1,
    text='File Uploading',
    width=450,
    font=label_font,
    justify=RIGHT,
    anchor=cst.W
)
file_upload_label.grid(row=2, column=0, columnspan=2, pady=(20, 0), padx=(40, 10))

filepath_var = StringVar()

filepath_input = cst.CTkEntry(
    master=frame_1,
    textvariable=filepath_var,
    placeholder_text='file path',
    width=300,
    height=50,
    fg_color='#E0E2F0',
    placeholder_text_color='#000000',
    border_width=0,
    font=into_text_font,
    border_color='#888B9E'
)
filepath_input.grid(row=3, column=0, padx=(40, 10), pady=10)

filepath_button = cst.CTkButton(
    master=frame_1,
    width=130,
    height=50,
    text='Open',
    command=openFile,
    fg_color='#575A6C',
    corner_radius=10,
    hover_color='#888B9E',
    font=button_text_font
)
filepath_button.grid(row=3, column=1, padx=(10, 10), pady=10)


# Heating\cooling  rate
heat_cool_label = cst.CTkLabel(
    master=frame_1,
    text='Heating\cooling  rate',
    width=420,
    font=label_font,
    justify=RIGHT,
    anchor=cst.W
)
heat_cool_label.grid(row=4, column=0, columnspan=2, pady=(20, 0), padx=(40, 10))


heat_cool_input = cst.CTkEntry(
    master=frame_1,
    width=300,
    height=50,
    fg_color='#E0E2F0',
    placeholder_text_color='#000000',
    font=into_text_font,
    border_width=0,
    border_color='#888B9E'
)
heat_cool_input.grid(row=5, column=0, padx=(40, 10), pady=10)

heat_cool_combobox = cst.CTkComboBox(
    master=frame_1,
    values=['K/min', 'K/s', 'C/min', 'C/s'],
    width=130,
    height=50,
    font=into_text_font,
    fg_color='#E0E2F0',
    border_color='#888B9E',
    border_width=0,
    dropdown_font=into_text_font,
    dropdown_fg_color='#E0E2F0',
    button_color='#575A6C',
    button_hover_color='#888B9E',
)
heat_cool_combobox.set("K/min")
heat_cool_combobox.grid(row=5, column=1, padx=(10, 10), pady=10)
#
# # Units of measurement
# unit_label = cst.CTkLabel(
#     master=frame_1,
#     text='Units of measurement',
#     width=420,
#     font=label_font,
#     justify=RIGHT,
#     anchor=cst.W
# )
# unit_label.grid(row=0, column=2, columnspan=2, padx=(40, 10), pady=(30, 0))
