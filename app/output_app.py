import customtkinter as cst
from tkinter import *
from fonts import Fontcl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

cst.set_appearance_mode('light')
cst.set_default_color_theme('dark-blue')


class ResultWindow(cst.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('PolyKineticAnalyzer')
        self.geometry("1000x900")

        self.button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=20, weight='bold')
        self.plus_button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=30, weight='bold')
        self.label_font = cst.CTkFont(family="Microsoft PhagsPa", size=18, )
        self.into_text_font = cst.CTkFont(family="Bahnschrift SemiBold", size=20)

        self.frame_4 = cst.CTkFrame(
            master=self,
            width=245,
            height=280,
            fg_color='#E0E2F0'
        )
        self.frame_4.place(x=50, y=50)

        self.z_label = cst.CTkLabel(
            master=self.frame_4,
            text='Z',
            font=self.into_text_font,
            width=20,
            justify=CENTER,
            anchor=cst.W
        )
        self.z_label.grid(row=0, column=0, pady=(30, 10), padx=(50, 0))

        self.z_label_num = cst.CTkLabel(
            master=self.frame_4,
            text='0.38723',
            font=self.into_text_font,
            width=155,
            height=50,
            justify=CENTER,
            fg_color='#FFFFFF'
        )
        self.z_label_num.grid(row=0, column=1, padx=(60, 50), pady=(20, 10))

        self.n_label = cst.CTkLabel(
            master=self.frame_4,
            text='n',
            font=self.into_text_font,
            width=20,
            justify=CENTER,
            anchor=cst.W
        )
        self.n_label.grid(row=1, column=0, pady=(20, 10), padx=(50, 0))

        self.n_label_num = cst.CTkLabel(
            master=self.frame_4,
            text='0.38723',
            font=self.into_text_font,
            width=155,
            height=50,
            justify=CENTER,
            fg_color='#FFFFFF'
        )
        self.n_label_num.grid(row=1, column=1, padx=(60, 50), pady=(20, 10))

        self.r2_label = cst.CTkLabel(
            master=self.frame_4,
            text='R2',
            font=self.into_text_font,
            width=20,
            justify=CENTER,
            anchor=cst.W
        )
        self.r2_label.grid(row=2, column=0, pady=(20, 10), padx=(50, 0))

        self.r2_label_num = cst.CTkLabel(
            master=self.frame_4,
            text='0.38723',
            font=self.into_text_font,
            width=155,
            height=50,
            justify=CENTER,
            fg_color='#FFFFFF'
        )
        self.r2_label_num.grid(row=2, column=1, padx=(60, 50), pady=(20, 30))

        self.frame_5 = cst.CTkFrame(
            master=self,
            width=245,
            height=280,
            fg_color='#E0E2F0'
        )
        self.frame_5.place(x=300, y=50)
