from tkinter import *
from tkinter import filedialog
import customtkinter as cst

from calculations import Calculations
from output_app import ResultWindow
cst.deactivate_automatic_dpi_awareness()


class App(cst.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_entries = []
        self.all_entries_dict = {}
        self.num_sample = 0

        self.button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=20, weight='bold')
        self.plus_button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=30, weight='bold')
        self.label_font = cst.CTkFont(family="Microsoft PhagsPa", size=18, )
        self.into_text_font = cst.CTkFont(family="Bahnschrift SemiBold", size=20)

        self.title('PolyKineticAnalyzer')
        self.geometry("1000x700")

        self.frame_1 = cst.CTkScrollableFrame(
            master=self,
            width=420,
            height=500,
            fg_color='#FFFFFF'
        )
        self.frame_1.place(x=50, y=50)

        self.file_upload_label = cst.CTkLabel(
            master=self.frame_1,
            text='File Uploading',
            width=130,
            font=self.label_font,
            justify=LEFT,
            anchor=cst.W
        )
        self.file_upload_label.grid(row=0, column=0, padx=(0, 10))
        self.add_files_label = cst.CTkLabel(
            master=self.frame_1,
            text='Add Files',
            width=130,
            font=self.label_font,
            justify=CENTER,
            anchor=cst.W
        )
        self.add_files_label.grid(row=1, column=0, padx=(0, 10), pady=10)

        self.plus_button = cst.CTkButton(
            master=self.frame_1,
            width=50,
            height=50,
            text='+',
            fg_color='#575A6C',
            command=self.addBox,
            corner_radius=10,
            hover_color='#888B9E',
            font=self.plus_button_text_font
        )

        self.plus_button.grid(row=1, column=1, padx=(40, 10), pady=10, sticky='w')

        self.frame_2 = cst.CTkFrame(
            master=self,
            width=400,
            height=1400,
            # fg_color='#FFFFFF'
        )
        self.frame_2.place(x=550, y=50)

        # temp_mode

        self.temp_mode_label = cst.CTkLabel(
            master=self.frame_2,
            text='Temperature mode',
            width=300,
            font=self.label_font,
            justify=LEFT,
            anchor=cst.W
        )
        self.temp_mode_label.grid(row=0, column=0, columnspan=2)

        self.temp_mode_combobox = cst.CTkComboBox(
            master=self.frame_2,
            values=['cooling', 'heating'],
            width=300,
            height=50,
            font=self.into_text_font,
            fg_color='#FFFFFF',
            border_color='#888B9E',
            border_width=1,
            dropdown_font=self.into_text_font,
            dropdown_fg_color='#E0E2F0',
            button_color='#575A6C',
            button_hover_color='#888B9E',
        )
        self.temp_mode_combobox.set("cooling")
        self.temp_mode_combobox.grid(row=1, column=0, columnspan=2, pady=10)

        # Units of measurement
        self.unit_label = cst.CTkLabel(
            master=self.frame_2,
            text='Units of measurement',
            width=300,
            font=self.label_font,
            justify=LEFT,
            anchor=cst.W
        )
        self.unit_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.temp_unit_label = cst.CTkLabel(
            master=self.frame_2,
            text='Temperature',
            font=self.label_font,
            width=160,
            justify=LEFT,
            anchor=cst.W
        )
        self.temp_unit_label.grid(row=3, column=0, pady=10)

        self.temp_unit_combobox = cst.CTkComboBox(
            master=self.frame_2,
            values=['K', 'C'],
            width=130,
            height=50,
            font=self.into_text_font,
            fg_color='#E0E2F0',
            border_color='#888B9E',
            border_width=1,
            dropdown_font=self.into_text_font,
            dropdown_fg_color='#E0E2F0',
            button_color='#575A6C',
            button_hover_color='#888B9E',
        )
        self.temp_unit_combobox.set("K")
        self.temp_unit_combobox.grid(row=3, column=1, padx=(10, 0), pady=10)

        self.dsc_unit_label = cst.CTkLabel(
            master=self.frame_2,
            text='DSC',
            font=self.label_font,
            width=160,
            justify=LEFT,
            anchor=cst.W
        )
        self.dsc_unit_label.grid(row=4, column=0, pady=10)

        self.dsc_unit_combobox = cst.CTkComboBox(
            master=self.frame_2,
            values=['mW/mg', 'W/g'],
            width=130,
            height=50,
            font=self.into_text_font,
            fg_color='#E0E2F0',
            border_color='#888B9E',
            border_width=1,
            dropdown_font=self.into_text_font,
            dropdown_fg_color='#E0E2F0',
            button_color='#575A6C',
            button_hover_color='#888B9E',
        )
        self.dsc_unit_combobox.set("mW/mg")
        self.dsc_unit_combobox.grid(row=4, column=1, padx=(10, 0), pady=10)

        self.time_unit_label = cst.CTkLabel(
            master=self.frame_2,
            text='Time',
            font=self.label_font,
            width=160,
            justify=LEFT,
            anchor=cst.W
        )
        self.time_unit_label.grid(row=5, column=0, pady=10)

        self.time_unit_combobox = cst.CTkComboBox(
            master=self.frame_2,
            values=['min', 's'],
            width=130,
            height=50,
            font=self.into_text_font,
            fg_color='#E0E2F0',
            border_color='#888B9E',
            border_width=1,
            dropdown_font=self.into_text_font,
            dropdown_fg_color='#E0E2F0',
            button_color='#575A6C',
            button_hover_color='#888B9E',
        )
        self.time_unit_combobox.set("min")
        self.time_unit_combobox.grid(row=5, column=1, padx=(10, 0), pady=10)

        self.calculate_button = cst.CTkButton(
            master=self.frame_2,
            width=310,
            height=40,
            text='Calculate',
            fg_color='#575A6C',
            command=self.enter_calculate,
            corner_radius=10,
            hover_color='#888B9E',
            font=self.button_text_font
        )

        self.calculate_button.grid(row=7, column=0, columnspan=2, pady=(50, 0), sticky='w')

    def enter_calculate(self):
        # print(self.temp_mode_combobox.get(), self.temp_unit_combobox.get(), self.dsc_unit_combobox.get(),
        #       self.time_unit_combobox.get())
        # for number, (rate_num, rate_mes, filepath) in enumerate(self.all_entries):
        #     print(number, rate_num.get(), rate_mes.get(), filepath.cget("text"))
        # for number, (rate_num, rate_mes, filepath) in enumerate(self.all_entries):
        #     print(number, rate_num.get(), rate_mes.get(), filepath.cget("text"))
        #     a = calculate(filepath.cget("text"), int(rate_num.get()))
        #     print(a)
        self.calculation_results: list = []
        for i in range(len(self.all_entries)):
            calculation_results_dict: dict = {}
            rate_num, _, filepath = self.all_entries[i]
            rate_entry = rate_num.get()
            filepath_entry = filepath.cget("text")
            if rate_entry != '' and filepath_entry != '':
                calculated_cl = Calculations()
                calculated_cl.filepath = filepath_entry
                calculated_cl.cool_speed = int(rate_entry)

                z, n, r2 = calculated_cl.calculate()
                calculation_results_dict['cl'] = calculated_cl
                calculation_results_dict['z'] = z
                calculation_results_dict['n'] = n
                calculation_results_dict['r2'] = r2
                self.calculation_results.append(calculation_results_dict)

        self.toplevel_window = ResultWindow(self)
        self.toplevel_window.after(10, self.toplevel_window.lift)

    def addBox(self):
        def openfile():
            filepath = filedialog.askopenfilename(
                title="Open file okay?",
                filetypes=(
                    ("text files", "*.txt"), ("all files", "*.*")
                )
            )
            filepath_n = str(filepath).split('/')
            filepath_lable.configure(text=filepath_n[-1])
            filepath_lable_ull.configure(text=filepath)

        print("ADD")
        next_column = len(self.all_entries)
        # Heating\cooling  rate
        heat_cool_label = cst.CTkLabel(
            master=self.frame_1,
            text='Heating\cooling  rate',
            width=280,
            font=self.label_font,
            justify=LEFT,
            anchor=cst.W
        )
        heat_cool_label.grid(row=3 + next_column*3, column=0, columnspan=2, pady=(30, 0))

        heat_cool_input = cst.CTkEntry(
            master=self.frame_1,
            width=130,
            height=50,
            fg_color='#E0E2F0',
            placeholder_text_color='#000000',
            font=self.into_text_font,
            border_width=1,
            border_color='#888B9E',
            justify=LEFT
        )
        heat_cool_input.grid(row=4 + next_column*3, column=0, padx=(0, 10))

        heat_cool_combobox = cst.CTkComboBox(
            master=self.frame_1,
            values=['K/min', 'K/s', 'C/min', 'C/s'],
            width=130,
            height=50,
            font=self.into_text_font,
            fg_color='#E0E2F0',
            border_color='#888B9E',
            border_width=1,
            dropdown_font=self.into_text_font,
            dropdown_fg_color='#E0E2F0',
            button_color='#575A6C',
            button_hover_color='#888B9E',
        )
        heat_cool_combobox.set("K/min")
        heat_cool_combobox.grid(row=4 + next_column*3, column=1, padx=(10, 10))

        filepath_button = cst.CTkButton(
            master=self.frame_1,
            width=100,
            height=50,
            text='Open',
            command=openfile,
            fg_color='#575A6C',
            corner_radius=10,
            hover_color='#888B9E',
            font=self.button_text_font
        )
        filepath_button.grid(row=4 + next_column*3, column=2, padx=(10, 0))

        filepath_lable = cst.CTkLabel(
            master=self.frame_1,
            width=280,
            text='',
            font=self.label_font,
            justify=LEFT,
            anchor=cst.W
        )
        filepath_lable.grid(row=5 + next_column*3, column=0, columnspan=2, padx=(10, 0))
        filepath_lable_ull = cst.CTkLabel(
            master=self.frame_1
        )

        self.all_entries.append((
            heat_cool_input, heat_cool_combobox, filepath_lable_ull
        ))


if __name__ == "__main__":
    app = App()
    app.mainloop()
