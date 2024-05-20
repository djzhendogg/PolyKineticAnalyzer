import customtkinter as cst
from tkinter import *
from plots import (
    plot_1,
    plot_2,
    plot_3,
    plot_fridman
)
from table import TableWidget
from explanation_taker import n_explanation
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
        self.geometry("1070x700")
        self.configure(fg_color='#FFFFFF')
        self.button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=20, weight='bold')
        self.plus_button_text_font = cst.CTkFont(family="Microsoft PhagsPa", size=30, weight='bold')
        self.label_font = cst.CTkFont(family="Microsoft PhagsPa", size=18, )
        self.into_text_font = cst.CTkFont(family="Bahnschrift SemiBold", size=20)

        self.tabview = cst.CTkTabview(
            master=self,
            width=1020,
            height=670,
            # fg_color='#FFFFFF'
        )
        self.tabview.pack()
        summary_avrami_table_data = [
            ('rate', 'z', 'n', 'r2')
        ]
        inflections = []
        tables = []
        micro_tables = []
        trimmed_tables = []
        for number, data_info in enumerate(self.master.calculation_results):
            class_tables_info = data_info.get('cl')
            z = data_info.get('z')
            n = data_info.get('n')
            r2 = data_info.get('r2')
            # tab_name = f'tab {number + 1}'
            tab_name = f'{class_tables_info.cool_speed} {class_tables_info.cool_speed_units}'
            summary_avrami_table_data.append(
                (round(data_info['cl'].cool_speed, 1), round(z, 3), round(n, 3), round(r2, 3))
            )
            self.tabview.add(tab_name)
            abstract_frame = cst.CTkScrollableFrame(
                master=self.tabview.tab(tab_name),
                width=1000,
                height=650,
                fg_color='#FFFFFF'
            )
            abstract_frame.grid(row=0, column=0, padx=(0, 0))
            frame_4_1 = cst.CTkFrame(
                master=abstract_frame,
                width=420,
                height=300,
                fg_color='#E0E2F0'
            )
            frame_4_1.grid(row=0, column=0, padx=(10, 10))

            file_name_label = cst.CTkLabel(
                master=frame_4_1,
                text=f"File name: {class_tables_info.filepath.split('/')[-1]}",
                font=self.into_text_font,
                width=400,
                justify=CENTER,
                anchor=cst.W
            )
            file_name_label.grid(row=0, column=0, pady=(10, 10), padx=(30, 0))

            cs_label = cst.CTkLabel(
                master=frame_4_1,
                text=f"Cool speed: {class_tables_info.cool_speed} {class_tables_info.cool_speed_units}",
                font=self.into_text_font,
                width=400,
                justify=CENTER,
                anchor=cst.W
            )
            cs_label.grid(row=1, column=0, pady=(10, 10), padx=(30, 0))

            cs_temp_label = cst.CTkLabel(
                master=frame_4_1,
                text=f"Crystallization temperature: {class_tables_info.cristal_temp}",
                font=self.into_text_font,
                width=400,
                justify=CENTER,
                anchor=cst.W
            )
            cs_temp_label.grid(row=2, column=0, pady=(10, 10), padx=(30, 0))
            area_label = cst.CTkLabel(
                master=frame_4_1,
                text=f"Area: {round(class_tables_info.area, 4)}",
                font=self.into_text_font,
                width=400,
                justify=CENTER,
                anchor=cst.W
            )
            area_label.grid(row=3, column=0, pady=(10, 10), padx=(30, 0))

            frame_4 = cst.CTkFrame(
                master=abstract_frame,
                width=285,
                height=260,
                fg_color='#E0E2F0'
            )
            frame_4.grid(row=0, column=1, padx=(10, 10), pady=(30, 0))

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
            r2_label.grid(row=2, column=0, pady=(20, 20), padx=(20, 0))
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
            r2_label_num.grid(row=2, column=1, padx=(50, 20), pady=(20, 20))

            plot_1_label = cst.CTkLabel(
                master=abstract_frame,
                text='DSC curve with indication\nof crystallization process boundaries:',
                font=self.into_text_font,
                width=450,
                height=50,
                justify=CENTER,
                fg_color='#FFFFFF'
            )
            plot_1_label.grid(row=1, column=0, padx=(40, 20), pady=(20, 10))

            frame_5 = cst.CTkFrame(
                master=abstract_frame,
                width=450,
                height=300,
                fg_color='#E0E2F0'
            )
            frame_5.grid(row=2, column=0, padx=(10, 10))
            plot_1(
                frame=frame_5,
                inflection=class_tables_info.inflection,
                table=class_tables_info.table
            )
            frame_4_2 = cst.CTkFrame(
                master=abstract_frame,
                width=360,
                height=400,
                fg_color='#E0E2F0'
            )
            frame_4_2.grid(row=2, column=1, padx=(60, 10))

            n_exp_text = n_explanation(round(n))
            n_exp_label = cst.CTkLabel(
                master=frame_4_2,
                text=n_exp_text,
                font=self.into_text_font,
                width=360,
                justify=CENTER,
                anchor=cst.W
            )
            n_exp_label.grid(row=0, column=0, padx=(40, 10), pady=(50, 50))

            inflections.append(class_tables_info.inflection)
            tables.append(class_tables_info.table)
            plot_2_label = cst.CTkLabel(
                master=abstract_frame,
                text='Graph of dependence of ln ln (1 / (1 - X(t)))\non ln(t) according to the Avrami equation:',
                font=self.into_text_font,
                width=400,
                height=50,
                justify=CENTER,
                fg_color='#FFFFFF'
            )
            plot_2_label.grid(row=3, column=0, padx=(40, 20), pady=(50, 10))
            plot_3_label = cst.CTkLabel(
                master=abstract_frame,
                text='Evolution of relative crystallinity\nas a function of temperature:',
                font=self.into_text_font,
                width=400,
                height=50,
                justify=CENTER,
                fg_color='#FFFFFF'
            )
            plot_3_label.grid(row=3, column=1, padx=(40, 20), pady=(50, 10))
            frame_6 = cst.CTkFrame(
                master=abstract_frame,
                width=450,
                height=400,
                fg_color='#E0E2F0'
            )
            frame_6.grid(row=4, column=0, padx=(10, 10))
            plot_2(
                frame=frame_6,
                micro_table=class_tables_info.micro_table
            )
            micro_tables.append(class_tables_info.micro_table)
            frame_7 = cst.CTkFrame(
                master=abstract_frame,
                width=450,
                height=400,
                fg_color='#E0E2F0'
            )
            frame_7.grid(row=4, column=1, padx=(30, 10))
            plot_3(
                frame=frame_7,
                trimmed=class_tables_info.trimmed
            )
            trimmed_tables.append(class_tables_info.trimmed)
        if self.master.show_fridman:
            self.tabview.add('fridman')
            abstract_frame_f = cst.CTkScrollableFrame(
                master=self.tabview.tab('fridman'),
                width=950,
                height=650,
                fg_color='#FFFFFF'
            )
            abstract_frame_f.grid(row=0, column=0, padx=(0, 0))
            # frame_8 = cst.CTkFrame(
            #     master=abstract_frame_f,
            #     width=285,
            #     height=260,
            #     fg_color='#E0E2F0'
            # )
            # frame_8.grid(row=0, column=0, padx=(10, 10))
            #
            # energy_label = cst.CTkLabel(
            #     master=frame_8,
            #     text='E',
            #     font=self.into_text_font,
            #     width=40,
            #     justify=CENTER,
            #     anchor=cst.W
            # )
            # energy_label.grid(row=0, column=0, pady=(20, 10), padx=(20, 0))
            #
            # energy_label_num = cst.CTkLabel(
            #     master=frame_8,
            #     text=str(round(self.master.fridman_energy, 3)),
            #     font=self.into_text_font,
            #     width=155,
            #     height=50,
            #     justify=CENTER,
            #     fg_color='#FFFFFF'
            # )
            # energy_label_num.grid(row=0, column=1, padx=(50, 20), pady=(20, 10))
            fridman_plot_label = cst.CTkLabel(
                master=abstract_frame_f,
                text='Plots of ln(dX/dt) dependence on inverse temperature at different degrees of crystallinity:',
                font=self.into_text_font,
                width=400,
                height=50,
                justify=CENTER,
                fg_color='#FFFFFF'
            )
            fridman_plot_label.grid(row=0, column=0, padx=(10, 10), pady=(30, 0))

            frame_9 = cst.CTkFrame(
                master=abstract_frame_f,
                width=900,
                height=600,
                fg_color='#E0E2F0'
            )
            frame_9.grid(row=1, column=0, padx=(10, 10))
            plot_fridman(
                frame=frame_9,
                fin_dict=self.master.fridman_fin_dict
            )

            table_energy_label = cst.CTkLabel(
                master=abstract_frame_f,
                text='The results of calculations of activation energy values using the Friedman method:',
                font=self.into_text_font,
                width=400,
                height=50,
                justify=CENTER,
                fg_color='#FFFFFF'
            )
            table_energy_label.grid(row=2, column=0, padx=(10, 10), pady=(30, 0))
            frame_10 = cst.CTkFrame(
                master=abstract_frame_f,
                width=900,
                height=600,
                fg_color='#E0E2F0'
            )
            frame_10.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))

            energy_table = TableWidget(frame_10, self.master.summary_energy_table_data)
            # energy_table.activate_scrollbar()

            self.tabview.add('summary')
            summary_frame = cst.CTkScrollableFrame(
                master=self.tabview.tab('summary'),
                width=950,
                height=650,
                fg_color='#FFFFFF'
            )
            summary_frame.grid(row=0, column=0, padx=(0, 0))

            table_avrami_label = cst.CTkLabel(
                master=summary_frame,
                text='Summary table with the results of calculations of crystallization parameters by Avrami algorithm:',
                font=self.into_text_font,
                width=900,
                height=50,
                justify=CENTER,
                fg_color='#FFFFFF'
            )
            table_avrami_label.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(30, 0))

            frame_11 = cst.CTkFrame(
                master=summary_frame,
                width=900,
                height=100,
                fg_color='#E0E2F0'
            )
            frame_11.grid(row=1, column=0, columnspan=2, padx=(10, 10))
            avrami_summary_table = TableWidget(frame_11, summary_avrami_table_data, visible_rows='summary')
            avrami_summary_table.activate_scrollbar()

            graph_1_label = cst.CTkLabel(
                master=summary_frame,
                text='Collaborative graph of the\nevolution of relative crystallinity:',
                font=self.into_text_font,
                width=450,
                height=50,
                justify=CENTER,
                fg_color='#FFFFFF'
            )
            graph_1_label.grid(row=2, column=0, padx=(10, 10), pady=(30, 0))

            frame_13 = cst.CTkFrame(
                master=summary_frame,
                width=450,
                height=280,
                fg_color='#E0E2F0'
            )
            frame_13.grid(row=3, column=0, padx=(10, 10))
            plot_2(
                frame=frame_13,
                micro_table=micro_tables,
                several=True
            )

            graph_2_label = cst.CTkLabel(
                master=summary_frame,
                text='Co-plots the dependence of\nln ln (1 / (1 - Y)) on ln(t)\naccording to the Avrami equation:',
                font=self.into_text_font,
                width=450,
                height=50,
                justify=CENTER,
                fg_color='#FFFFFF'
            )
            graph_2_label.grid(row=2, column=1, padx=(10, 10), pady=(30, 0))

            frame_14 = cst.CTkFrame(
                master=summary_frame,
                width=450,
                height=280,
                fg_color='#E0E2F0'
            )
            frame_14.grid(row=3, column=1, padx=(10, 10))
            plot_3(
                frame=frame_14,
                trimmed=trimmed_tables,
                several=True
            )
