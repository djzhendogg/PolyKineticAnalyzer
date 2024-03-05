from tkinter import *
from tkinter import filedialog, ttk
import tkinter
import customtkinter as cst
import os


wordir = os.getcwd()


def addBox():
    def openfile():
        filepath = filedialog.askopenfilename(
            initialdir=wordir,
            title="Open file okay?",
            filetypes=(
                ("text files", "*.txt"), ("all files", "*.*")
            )
        )
        filepath = str(filepath).split('/')
        filepath_lable.configure(text=filepath[-1])

    print("ADD")
    next_column = len(all_entries)
    # Heating\cooling  rate
    heat_cool_label = cst.CTkLabel(
        master=frame_1,
        text='Heating\cooling  rate',
        width=280,
        font=label_font,
        justify=LEFT,
        anchor=cst.W
    )
    heat_cool_label.grid(row=3 + next_column*3, column=0, columnspan=2, pady=(30, 0))

    heat_cool_input = cst.CTkEntry(
        master=frame_1,
        width=130,
        height=50,
        fg_color='#E0E2F0',
        placeholder_text_color='#000000',
        font=into_text_font,
        border_width=1,
        border_color='#888B9E',
        justify=LEFT
    )
    heat_cool_input.grid(row=4 + next_column*3, column=0, padx=(0, 10))

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
    heat_cool_combobox.grid(row=4 + next_column*3, column=1, padx=(10, 10))

    filepath_button = cst.CTkButton(
        master=frame_1,
        width=100,
        height=50,
        text='Open',
        command=openfile,
        fg_color='#575A6C',
        corner_radius=10,
        hover_color='#888B9E',
        font=button_text_font
    )
    filepath_button.grid(row=4 + next_column*3, column=2, padx=(10, 0))

    filepath_lable = cst.CTkLabel(
        master=frame_1,
        width=280,
        text = '',
        font=label_font,
        justify=LEFT,
        anchor=cst.W
    )
    filepath_lable.grid(row=5 + next_column*3, column=0, columnspan=2, padx=(10, 0))

    all_entries.append((
        heat_cool_label, heat_cool_input, heat_cool_combobox, filepath_button
    ))
    all_entries_dict[len(all_entries)] = [heat_cool_label, heat_cool_input, heat_cool_combobox, filepath_button]
    print(all_entries_dict)

all_entries = []
all_entries_dict = {}
num_sample = 0

cst.set_appearance_mode('light')
cst.set_default_color_theme('dark-blue')
app = cst.CTk()
app.title('PolyKineticAnalyzer')
app.geometry("1000x700")
# styles
button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=20, weight='bold')
plus_button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=30, weight='bold')
label_font = cst.CTkFont(family="Microsoft PhagsPa", size=18,)
into_text_font = cst.CTkFont(family="Bahnschrift SemiBold", size=20)

# frame settings
frame_1 = cst.CTkScrollableFrame(
    master=app,
    width=420,
    height=500,
    # fg_color='#FFFFFF'
)
frame_1.place(x=50, y=50)

file_upload_label = cst.CTkLabel(
    master=frame_1,
    text='File Uploading',
    width=130,
    font=label_font,
    justify=LEFT,
    anchor=cst.W
)
file_upload_label.grid(row=0, column=0, padx=(0, 10))

# add forms button

add_files_label = cst.CTkLabel(
    master=frame_1,
    text='Add Files',
    width=130,
    font=label_font,
    justify=CENTER,
    anchor=cst.W
)
add_files_label.grid(row=1, column=0, padx=(0, 10), pady=10)

plus_button = cst.CTkButton(
    master=frame_1,
    width=50,
    height=50,
    text='+',
    fg_color='#575A6C',
    command=addBox,
    corner_radius=10,
    hover_color='#888B9E',
    font=plus_button_text_font
)

plus_button.grid(row=1, column=1, padx=(40, 10), pady=10, sticky='w')


# second frame
frame_2 = cst.CTkFrame(
    master=app,
    width=400,
    height=1400,
    # fg_color='#FFFFFF'
)
frame_2.place(x=550, y=50)

# temp_mode

temp_mode_label = cst.CTkLabel(
    master=frame_2,
    text='Temperature mode',
    width=300,
    font=label_font,
    justify=LEFT,
    anchor=cst.W
)
temp_mode_label.grid(row=0, column=0, columnspan=2)

temp_mode_combobox = cst.CTkComboBox(
    master=frame_2,
    values=['cooling', 'heating'],
    width=300,
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
temp_mode_combobox.grid(row=1, column=0, columnspan=2, pady=10)

# Units of measurement
unit_label = cst.CTkLabel(
    master=frame_2,
    text='Units of measurement',
    width=300,
    font=label_font,
    justify=LEFT,
    anchor=cst.W
)
unit_label.grid(row=2, column=0, columnspan=2, pady=10)


temp_unit_label = cst.CTkLabel(
    master=frame_2,
    text='Temperature',
    font=label_font,
    width=160,
    justify=LEFT,
    anchor=cst.W
)
temp_unit_label.grid(row=3, column=0, pady=10)

temp_unit_combobox = cst.CTkComboBox(
    master=frame_2,
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
temp_unit_combobox.grid(row=3, column=1, padx=(10, 0), pady=10)

dsc_unit_label = cst.CTkLabel(
    master=frame_2,
    text='DSC',
    font=label_font,
    width=160,
    justify=LEFT,
    anchor=cst.W
)
dsc_unit_label.grid(row=4, column=0, pady=10)

dsc_unit_combobox = cst.CTkComboBox(
    master=frame_2,
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
dsc_unit_combobox.grid(row=4, column=1, padx=(10, 0), pady=10)


time_unit_label = cst.CTkLabel(
    master=frame_2,
    text='Time',
    font=label_font,
    width=160,
    justify=LEFT,
    anchor=cst.W
)
time_unit_label.grid(row=5, column=0, pady=10)

time_unit_combobox = cst.CTkComboBox(
    master=frame_2,
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
time_unit_combobox.grid(row=5, column=1, padx=(10, 0), pady=10)


app.mainloop()
