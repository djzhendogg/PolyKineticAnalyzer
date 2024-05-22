from tkinter import *
from tkinter import filedialog
import customtkinter as cst
from CTkXYFrame import *
from instruction import instruction_text
from calculations_arrays import Calculations
from output_app import ResultWindow
from fridman_calculations_array import fridman_calculations_

cst.deactivate_automatic_dpi_awareness()


class App(cst.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # для кнопки
        self.files = []
        self.file_labels = []
        self.delete_buttons = []
        self.file_names_short: list = []

        self.num_sample_ever = 0

        self.instruction_frame = None
        self.toplevel_window = None
        self.frame_1 = None
        self.calculate_button_widget = None

        self.button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=20, weight='bold')
        self.delete_button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=16, weight='bold')
        self.plus_button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=30, weight='bold')
        self.label_font = cst.CTkFont(family="Microsoft PhagsPa", size=18, )
        self.instruction_text_font = cst.CTkFont(family="Bahnschrift SemiBold", size=16)
        self.show_fridman: bool = False
        self.title('PolyKineticAnalyzer')
        self.geometry("1200x700")

        self.file_upload_label = cst.CTkLabel(
            master=self,
            text='File Uploading',
            width=200,
            font=self.button_text_font,
            justify=LEFT,
            anchor=cst.W
        )
        self.file_upload_label.grid(row=0, column=0, padx=(40, 10), pady=(40, 0))
        self.add_files_label = cst.CTkLabel(
            master=self,
            text='Add Files',
            width=200,
            font=self.button_text_font,
            justify=LEFT,
            anchor=cst.W
        )
        self.add_files_label.grid(row=1, column=0, padx=(40, 10), pady=10)

        self.plus_button = cst.CTkButton(
            master=self,
            width=50,
            height=50,
            text='+',
            fg_color='#575A6C',
            command=self.openfile,
            corner_radius=10,
            hover_color='#888B9E',
            font=self.plus_button_text_font
        )

        self.plus_button.grid(row=1, column=1, padx=(90, 0), pady=10, sticky='w')
        self.left_frame()
        self.right_frame()
        self.calculate_button()

    def left_frame(self):
        self.frame_1 = CTkXYFrame(
            master=self,
            width=420,
            height=270,
            fg_color='#FFFFFF'
        )
        self.frame_1.grid(row=2, column=0, padx=(40, 10), columnspan=2, pady=(30, 0), sticky='w')

    def calculate_button(self):
        self.calculate_button_widget = cst.CTkButton(
            master=self,
            width=420,
            height=40,
            text='Calculate',
            fg_color='#575A6C',
            command=self.enter_calculate,
            corner_radius=10,
            hover_color='#888B9E',
            font=self.button_text_font
        )

        self.calculate_button_widget.grid(row=3, column=0, padx=(40, 10), columnspan=2, pady=(30, 0), sticky='w')

    def right_frame(self):
        self.instruction_frame = cst.CTkFrame(
            master=self,
            width=480,
            height=600,
            fg_color='#FFFFFF'
        )
        self.instruction_frame.grid(row=0, column=3, padx=(120, 10), rowspan=4, pady=(30, 0), sticky='w')
        n_exp_label = cst.CTkLabel(
            master=self.instruction_frame,
            text=instruction_text,
            font=self.instruction_text_font,
            width=420,
            justify='left',
            anchor=cst.W
        )
        n_exp_label.pack(side="top", padx=30, pady=5)

    def openfile(self):

        filepaths = filedialog.askopenfilenames(
            title="Open file okay?",
            filetypes=(
                ("text files", "*.txt"), ("all files", "*.*")
            )
        )
        for index, filepath in enumerate(filepaths):
            if filepath not in self.files and len(self.files) < 50:
                self.num_sample_ever += 1
                filepath_n = str(filepath).split('/')
                filepath_lable = cst.CTkLabel(
                    master=self.frame_1,
                    width=280,
                    text=f"{len(self.files) + 1}. {filepath_n[-1]}",
                    font=self.label_font,
                    justify=LEFT,
                    anchor=cst.W
                )
                filepath_lable.grid(row=self.num_sample_ever, column=0, padx=(25, 10), pady=(10, 0))

                delete_row_button = cst.CTkButton(
                    master=self.frame_1,
                    width=60,
                    height=30,
                    text='delete',
                    fg_color='#575A6C',
                    command=lambda file=filepath: self.delete_file(file),
                    corner_radius=10,
                    hover_color='#888B9E',
                    font=self.delete_button_text_font
                )

                delete_row_button.grid(row=self.num_sample_ever, column=1, padx=(10, 10), pady=(10, 0))
                self.files.append(filepath)
                self.file_names_short.append(filepath_n[-1])
                self.file_labels.append(filepath_lable)
                self.delete_buttons.append(delete_row_button)

    def delete_file(self, file):
        # Получить индекс удаляемого файла
        index = self.files.index(file)

        # Удалить метку и кнопку "delete"
        self.file_labels[index].destroy()
        self.delete_buttons[index].destroy()

        # Обновить список файлов и меток
        self.files.pop(index)
        self.file_names_short.pop(index)
        self.file_labels.pop(index)
        self.delete_buttons.pop(index)

        # Перестроить оставшиеся файлы
        for i in range(len(self.files)):
            self.file_labels[i].configure(text=f"{i + 1}. {self.file_names_short[i]}")

    def enter_calculate(self):
        self.calculation_results: list = []
        for path_to_file in self.files:
            calculation_results_dict: dict = {}
            calculated_cl = Calculations(filepath=path_to_file)
            z, n, r2 = calculated_cl.calculate()
            calculation_results_dict['cl'] = calculated_cl
            calculation_results_dict['z'] = z
            calculation_results_dict['n'] = n
            calculation_results_dict['r2'] = r2
            self.calculation_results.append(calculation_results_dict)
        if len(self.calculation_results) > 1:
            self.show_fridman = True
            (
                self.fridman_fin_dict,
                self.summary_energy_table_data
            ) = fridman_calculations_(self.calculation_results)
        self.toplevel_window = ResultWindow(self)
        self.toplevel_window.after(10, self.toplevel_window.lift)


if __name__ == "__main__":
    app = App()
    app.mainloop()
