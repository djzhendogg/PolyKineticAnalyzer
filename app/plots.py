import customtkinter as cst
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import numpy as np
import matplotlib.pyplot as plt


def plot_1(frame, inflection, table, several=False):
    px = 1 / 100
    fig = Figure(figsize=(400 * px, 280 * px), constrained_layout=True)


    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    if several:
        for inflection_1, table_1 in zip(inflection, table):
            plot1.plot(table_1["Temp"], table_1["DSC"])
            plot1.scatter(inflection_1["Temp"], inflection_1["DSC"])
            plot1.plot(inflection_1["Temp"], inflection_1["DSC"])
    else:
        plot1.plot(table["Temp"], table["DSC"])
        plot1.scatter(inflection["Temp"], inflection["DSC"])
        plot1.plot(inflection["Temp"], inflection["DSC"])
        plot1.set_xlabel("T, K", fontsize=10)
        plot1.set_ylabel("DSC", fontsize=10)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=frame)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def plot_2(frame, micro_table, several=False):
    px = 1 / 100
    fig = Figure(figsize=(400 * px, 280 * px), constrained_layout=True)

    # adding the subplot
    plot2 = fig.add_subplot(111)

    # plotting the graph
    if several:
        for micro_table_1 in micro_table:
            plot2.plot(micro_table_1["Temp"], micro_table_1["Conversion_rate"])
    else:
        plot2.plot(micro_table["Temp"], micro_table["Conversion_rate"])
    plot2.set_xlabel("T, K", fontsize=10)
    plot2.set_ylabel("Conversion rate", fontsize=10)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=frame)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def plot_3(frame, trimmed, several=False):
    px = 1 / 100
    fig = Figure(figsize=(400 * px, 280 * px), constrained_layout=True)

    # adding the subplot
    plot3 = fig.add_subplot(111)

    # plotting the graph
    if several:
        for trimmed_1 in trimmed:
            plot3.scatter(trimmed_1["ln_Time"], trimmed_1["ln_min_ln_Conversion_rate"])
    else:
        plot3.scatter(trimmed["ln_Time"], trimmed["ln_min_ln_Conversion_rate"])
    plot3.set_xlabel("ln(t)", fontsize=10)
    plot3.set_ylabel("ln(-ln(1-X(t)))", fontsize=10)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=frame)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


def plot_fridman(frame, fin_dict):
    px = 1 / 100
    fig = Figure(figsize=(900 * px, 400 * px), constrained_layout=True)

    # adding the subplot
    plot4 = fig.add_subplot(111)

    # plotting the graph
    for key, value in fin_dict.items():
        x = value.get('x')
        y = value.get('y')
        plot4.scatter(x, y)
        m, b = np.polyfit(x, y, 1)
        plot4.plot(x, m * np.array(x) + b, label=f'{key}')
        plot4.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plot4.set_xlabel("1000/T, (1/K)", fontsize=10)
        plot4.set_ylabel("ln(dX/dt)", fontsize=10)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=frame)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

