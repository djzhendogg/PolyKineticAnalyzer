from tkinter import *
from tkinter import filedialog, ttk
import tkinter
import customtkinter as cst
import os


wordir = os.getcwd()


def openfile():
    filepath = filedialog.askopenfilename(
        initialdir=wordir,
        title="Open file okay?",
        filetypes=(
            ("text files", "*.txt"), ("all files", "*.*")
        )
    )
    filepath_var.set(str(filepath))


def place_upload_file():
    next_column = len(all_entries)
    print(next_column)
    file_upload_label = cst.CTkLabel(
        master=frame_1,
        text='File Uploading',
        width=450,
        font=label_font,
        justify=LEFT,
        anchor=cst.W
    )
    file_upload_label.grid(row=2+next_column*4, column=0, columnspan=2, padx=(40, 10), pady=(30, 0))

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
    filepath_input.grid(row=3+next_column*4, column=0, padx=(40, 10), pady=0)

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
    filepath_button.grid(row=3+next_column*4, column=1, padx=(10, 10), pady=10)

    # Heating\cooling  rate
    heat_cool_label = cst.CTkLabel(
        master=frame_1,
        text='Heating\cooling  rate',
        width=450,
        font=label_font,
        justify=LEFT,
        anchor=cst.W
    )
    heat_cool_label.grid(row=4+next_column*4, column=0, columnspan=2, pady=(10, 0), padx=(40, 10))

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
    heat_cool_input.grid(row=5+next_column*4, column=0, padx=(40, 10), pady=10)

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
    heat_cool_combobox.grid(row=5+next_column*4, column=1, padx=(10, 10), pady=10)

    all_entries.append((
        file_upload_label, filepath_input.get(), filepath_button,
        heat_cool_label, heat_cool_input, heat_cool_combobox
    ))

    plus_button = cst.CTkButton(
        master=frame_1,
        width=50,
        height=50,
        text='+',
        fg_color='#575A6C',
        command=place_upload_file,
        corner_radius=10,
        hover_color='#888B9E',
        font=plus_button_text_font
    )

    plus_button.grid(row=6 + next_column * 4, column=0, padx=(40, 10), pady=10, sticky='w')

cst.set_appearance_mode('light')
cst.set_default_color_theme('dark-blue')
app = cst.CTk()
app.title('PolyKineticAnalyzer')
app.geometry("2000x2000")
all_entries = []
# styles
button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=20, weight='bold')
plus_button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=30, weight='bold')
label_font = cst.CTkFont(family="Microsoft PhagsPa", size=18,)
into_text_font = cst.CTkFont(family="Bahnschrift SemiBold", size=20)

# frame settings
frame_1 = cst.CTkFrame(
    master=app,
    width=2000,
    height=2000,
    # fg_color='#FFFFFF'
)
frame_1.pack(padx=(40, 0))
frame_1.place(x=0, y=0)

frame_1.grid(row=0, column=0)
# temp_mode

temp_mode_label = cst.CTkLabel(
    master=frame_1,
    text='Temperature mode',
    width=450,
    font=label_font,
    justify=LEFT,
    anchor=cst.W
)
temp_mode_label.grid(row=0, column=0, columnspan=2, padx=(40, 10), pady=(30, 0))

temp_mode_combobox = cst.CTkComboBox(
    master=frame_1,
    values=['cooling', 'heating'],
    width=450,
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
temp_mode_combobox.set("cooling")
temp_mode_combobox.grid(row=1, column=0, columnspan=2, padx=(40, 10), pady=10)


# File Uploading
file_upload_label = cst.CTkLabel(
    master=frame_1,
    text='File Uploading',
    width=450,
    font=label_font,
    justify=LEFT,
    anchor=cst.W
)
file_upload_label.grid(row=2, column=0, columnspan=2, padx=(40, 10), pady=(30, 0))

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
filepath_input.grid(row=3, column=0, padx=(40, 10), pady=0)

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
filepath_button.grid(row=3, column=1, padx=(10, 10), pady=10)

# Heating\cooling  rate
heat_cool_label = cst.CTkLabel(
    master=frame_1,
    text='Heating\cooling  rate',
    width=450,
    font=label_font,
    justify=LEFT,
    anchor=cst.W
)
heat_cool_label.grid(row=4, column=0, columnspan=2, pady=(10, 0), padx=(40, 10))


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
heat_cool_input.grid(row=5, column=0, padx=(40, 10), pady=10)

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
heat_cool_combobox.grid(row=5, column=1, padx=(10, 10), pady=10)
all_entries.append((
    file_upload_label, filepath_input, filepath_button,
    heat_cool_label, heat_cool_input, heat_cool_combobox
))

# add forms button
plus_button = cst.CTkButton(
    master=frame_1,
    width=50,
    height=50,
    text='+',
    fg_color='#575A6C',
    command=place_upload_file,
    corner_radius=10,
    hover_color='#888B9E',
    font=plus_button_text_font
)

plus_button.grid(row=6, column=0, padx=(40, 10), pady=10, sticky='w')

# Units of measurement
unit_label = cst.CTkLabel(
    master=frame_1,
    text='Units of measurement',
    width=250,
    font=label_font,
    justify=LEFT,
    anchor=cst.W
)
unit_label.grid(row=0, column=4, columnspan=2, padx=(100, 10), pady=(30, 0))


temp_unit_label = cst.CTkLabel(
    master=frame_1,
    text='Temperature',
    font=label_font,
    width=100,
    justify=LEFT,
    anchor=cst.W
)
temp_unit_label.grid(row=1, column=4, padx=(100, 10), pady=10)

temp_unit_combobox = cst.CTkComboBox(
    master=frame_1,
    values=['K', 'C'],
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
temp_unit_combobox.set("K")
temp_unit_combobox.grid(row=1, column=5, padx=(10, 10), pady=10)

dsc_unit_label = cst.CTkLabel(
    master=frame_1,
    text='DSC',
    font=label_font,
    width=100,
    justify=LEFT,
    anchor=cst.W
)
dsc_unit_label.grid(row=2, column=4, padx=(100, 10), pady=10)

dsc_unit_combobox = cst.CTkComboBox(
    master=frame_1,
    values=['mW/mg', 'W/g'],
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
dsc_unit_combobox.set("mW/mg")
dsc_unit_combobox.grid(row=2, column=5, padx=(10, 10), pady=10)


time_unit_label = cst.CTkLabel(
    master=frame_1,
    text='Time',
    font=label_font,
    width=100,
    justify=LEFT,
    anchor=cst.W
)
time_unit_label.grid(row=3, column=4, padx=(100, 10), pady=10)

time_unit_combobox = cst.CTkComboBox(
    master=frame_1,
    values=['min', 's'],
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
time_unit_combobox.set("min")
time_unit_combobox.grid(row=3, column=5, padx=(10, 10), pady=10)


app.mainloop()
