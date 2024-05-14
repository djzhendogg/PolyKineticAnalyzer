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
        self.geometry("1020x700")
        self.configure(fg_color='#FFFFFF')

        self.button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=20, weight='bold')
        self.plus_button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=30, weight='bold')
        self.label_font = cst.CTkFont(family="Microsoft PhagsPa", size=18, )
        self.into_text_font = cst.CTkFont(family="Bahnschrift SemiBold", size=20)

        self.tabview = cst.CTkTabview(
            master=self,
            width=970,
            height=670,
            # fg_color='#FFFFFF'
        )
        self.tabview.pack()
        for number, data_info in enumerate(self.master.calculation_results):
            class_tables_info = data_info.get('cl')
            z = data_info.get('z')
            n = data_info.get('n')
            r2 = data_info.get('r2')
            tab_name = f'tab {number + 1}'
            self.tabview.add(tab_name)
            abstract_frame = cst.CTkScrollableFrame(
                master=self.tabview.tab(tab_name),
                width=950,
                height=650,
                fg_color='#FFFFFF'
            )
            abstract_frame.grid(row=0, column=0, padx=(0, 0))

            frame_4 = cst.CTkFrame(
                master=abstract_frame,
                width=285,
                height=260,
                fg_color='#E0E2F0'
            )
            frame_4.grid(row=0, column=0, padx=(10, 10))

            z_label = cst.CTkLabel(
                master=frame_4,
                text='Z',
                font=self.into_text_font,
                width=40,
                justify=CENTER,
                anchor=cst.W
            )
            z_label.grid(row=0, column=0, pady=(20, 10), padx=(20, 0))

            z_label_num = cst.CTkLabel(
                master=frame_4,
                text=str(round(z, 3)),
                font=self.into_text_font,
                width=155,
                height=50,
                justify=CENTER,
                fg_color='#FFFFFF'
            )
            z_label_num.grid(row=0, column=1, padx=(50, 20), pady=(20, 10))

            n_label = cst.CTkLabel(
                master=frame_4,
                text='n',
                font=self.into_text_font,
                width=40,
                justify=CENTER,
                anchor=cst.W
            )
            n_label.grid(row=1, column=0, pady=(20, 10), padx=(20, 0))

            n_label_num = cst.CTkLabel(
                master=frame_4,
                text=str(round(n, 3)),
                font=self.into_text_font,
                width=155,
                height=50,
                justify=CENTER,
                fg_color='#FFFFFF'
            )
            n_label_num.grid(row=1, column=1, padx=(50, 20), pady=(20, 10))

            r2_label = cst.CTkLabel(
                master=frame_4,
                text='R2',
                font=self.into_text_font,
                width=40,
                justify=CENTER,
                anchor=cst.W
            )
            r2_label.grid(row=2, column=0, pady=(10, 50), padx=(20, 0))
            #
            r2_label_num = cst.CTkLabel(
                master=frame_4,
                text=str(round(r2, 3)),
                font=self.into_text_font,
                width=155,
                height=50,
                justify=CENTER,
                fg_color='#FFFFFF'
            )
            r2_label_num.grid(row=2, column=1, padx=(50, 20), pady=(10, 20))

            frame_5 = cst.CTkFrame(
                master=abstract_frame,
                width=450,
                height=200,
                fg_color='#E0E2F0'
            )
            frame_5.grid(row=0, column=1, padx=(10, 10))
            plot_1(
                frame=frame_5,
                inflection=class_tables_info.inflection,
                table=class_tables_info.table
            )

            frame_6 = cst.CTkFrame(
                master=abstract_frame,
                width=450,
                height=280,
                fg_color='#E0E2F0'
            )
            frame_6.grid(row=1, column=0, padx=(10, 10))
            plot_2(
                frame=frame_6,
                micro_table=class_tables_info.micro_table
            )
            frame_7 = cst.CTkFrame(
                master=abstract_frame,
                width=450,
                height=280,
                fg_color='#E0E2F0'
            )
            frame_7.grid(row=1, column=1, padx=(10, 10))
            plot_3(
                frame=frame_7,
                trimmed=class_tables_info.trimmed
            )
