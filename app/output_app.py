import customtkinter as cst
from tkinter import *
from plots import plot_1, plot_2, plot_3
from calculations import Calculations


cst.set_appearance_mode('light')
cst.set_default_color_theme('dark-blue')
cst.deactivate_automatic_dpi_awareness()


class SCAbstractFrame(cst.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)



class ResultWindow(cst.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('PolyKineticAnalyzer')
        self.geometry("1000x800")

        self.button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=20, weight='bold')
        self.plus_button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=30, weight='bold')
        self.label_font = cst.CTkFont(family="Microsoft PhagsPa", size=18, )
        self.into_text_font = cst.CTkFont(family="Bahnschrift SemiBold", size=20)

        self.abstract_frame = cst.CTkFrame(
            master=self,
            width=900,
            height=800,
            fg_color='#FFFFFF'
        )
        self.abstract_frame.place(x=0, y=0)

        self.frame_4 = cst.CTkFrame(
            master=self.abstract_frame,
            width=400,
            height=320,
            fg_color='#E0E2F0'
        )
        self.frame_4.place(x=50, y=50)

        self.z_label = cst.CTkLabel(
            master=self.frame_4,
            text='Z',
            font=self.into_text_font,
            width=40,
            justify=CENTER,
            anchor=cst.W
        )
        self.z_label.grid(row=0, column=0, pady=(40, 10), padx=(70, 0))

        self.z_label_num = cst.CTkLabel(
            master=self.frame_4,
            text=str(round(self.master.z, 3)),
            font=self.into_text_font,
            width=155,
            height=50,
            justify=CENTER,
            fg_color='#FFFFFF'
        )
        self.z_label_num.grid(row=0, column=1, padx=(60, 70), pady=(30, 10))

        self.n_label = cst.CTkLabel(
            master=self.frame_4,
            text='n',
            font=self.into_text_font,
            width=40,
            justify=CENTER,
            anchor=cst.W
        )
        self.n_label.grid(row=1, column=0, pady=(20, 10), padx=(70, 0))

        self.n_label_num = cst.CTkLabel(
            master=self.frame_4,
            text=str(round(self.master.n, 3)),
            font=self.into_text_font,
            width=155,
            height=50,
            justify=CENTER,
            fg_color='#FFFFFF'
        )
        self.n_label_num.grid(row=1, column=1, padx=(60, 70), pady=(20, 10))

        self.r2_label = cst.CTkLabel(
            master=self.frame_4,
            text='R2',
            font=self.into_text_font,
            width=40,
            justify=CENTER,
            anchor=cst.W
        )
        self.r2_label.grid(row=2, column=0, pady=(20, 10), padx=(70, 0))

        self.r2_label_num = cst.CTkLabel(
            master=self.frame_4,
            text=str(round(self.master.r2, 3)),
            font=self.into_text_font,
            width=155,
            height=50,
            justify=CENTER,
            fg_color='#FFFFFF'
        )
        self.r2_label_num.grid(row=2, column=1, padx=(60, 70), pady=(20, 40))

        self.frame_5 = cst.CTkFrame(
            master=self.abstract_frame,
            width=400,
            height=200,
            fg_color='#E0E2F0'
        )
        self.frame_5.place(x=500, y=50)
        plot_1(
            frame=self.frame_5,
            inflection=self.master.calculated_cl.inflection,
            table=self.master.calculated_cl.table
        )

        self.frame_6 = cst.CTkFrame(
            master=self.abstract_frame,
            width=400,
            height=280,
            fg_color='#E0E2F0'
        )
        self.frame_6.place(x=50, y=400)
        plot_2(
            frame=self.frame_6,
            micro_table=self.master.calculated_cl.micro_table
        )
        self.frame_7 = cst.CTkFrame(
            master=self.abstract_frame,
            width=400,
            height=280,
            fg_color='#E0E2F0'
        )
        self.frame_7.place(x=500, y=400)
        plot_3(
            frame=self.frame_7,
            trimmed=self.master.calculated_cl.trimmed
        )

