import tkinter as tk
from tkinter import ttk
import customtkinter as cst


class TableWidget(cst.CTkFrame):
    def __init__(self, parent, table_data, visible_rows='all'):
        super().__init__(master=parent)

        if visible_rows == 'all':
            visible_rows_num = len(table_data)
        elif visible_rows == 'summary':
            if len(table_data) < 7:
                visible_rows_num = len(table_data)
            else:
                visible_rows_num = 6
        table_columns = tuple((i.lower() for i in table_data[0]))
        self.table = ttk.Treeview(
            self, columns=table_columns, show="headings", padding=10, height=visible_rows_num
        )

        for i in table_columns:
            self.table.heading(i, text=i.capitalize())
            self.table.column(i, anchor="center")

        for i in range(1, len(table_data)):
            self.table.insert("", tk.END, values=table_data[i], tag=table_data[i][-1])

        self.table.grid(row=0, column=0, sticky=tk.NSEW)
        self.pack()

    def activate_scrollbar(self):
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
