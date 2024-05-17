from tkinter import *
from tkinter import filedialog
import customtkinter as cst

from calculations import Calculations
from output_app import ResultWindow
from fridman_calculations import fridman_calculations_
cst.deactivate_automatic_dpi_awareness()


class Instraction(cst.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_entries = []
        self.all_entries_dict = {}
        self.fridman_fin_dict: dict = {}
        self.fridman_energy = 0
        self.num_sample = 0

        self.button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=20, weight='bold')
        self.plus_button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=30, weight='bold')
        self.label_font = cst.CTkFont(family="Microsoft PhagsPa", size=18, )
        self.into_text_font = cst.CTkFont(family="Bahnschrift SemiBold", size=20)
        self.title('PolyKineticAnalyzer')
        self.geometry("1000x700")
        self.frame_1 = cst.CTkScrollableFrame(
            master=self,
            width=850,
            height=550,
            fg_color='#FFFFFF'
        )
        self.frame_1.place(x=50, y=50)


if __name__ == "__main__":
    app = Instraction()
    app.mainloop()
