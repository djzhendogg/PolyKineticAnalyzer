from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import numpy as np


def plot_1(frame, inflection, table):
    px = 1 / 100
    fig = Figure(figsize=(400 * px, 280 * px), constrained_layout=True)


    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(table[:, 0], table[:, 2])
    plot1.scatter(inflection[:, 0], inflection[:, 2])
    plot1.plot(inflection[:, 0], inflection[:, 2])
    plot1.set_xlabel("T, C", fontsize=10)
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


def plot_2(frame, micro_table):
    px = 1 / 100
    fig = Figure(figsize=(400 * px, 280 * px), constrained_layout=True)

    # adding the subplot
    plot2 = fig.add_subplot(111)

    # plotting the graph
    plot2.plot(micro_table[:, 0], micro_table[:, 5])
    plot2.set_xlabel("T, C", fontsize=10)
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


def plot_3(frame, trimmed):
    px = 1 / 100
    fig = Figure(figsize=(400 * px, 280 * px), constrained_layout=True)

    # adding the subplot
    plot3 = fig.add_subplot(111)

    # plotting the graph
    plot3.scatter(trimmed[:, 8], trimmed[:, 7])
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


def dsc_plot_summary(frame, table, tab_name_list):
    px = 1 / 100
    fig = Figure(figsize=(900 * px, 400 * px), constrained_layout=True)

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    for table_1, line_label in zip(table, tab_name_list):
        plot1.plot(table_1[:, 0], table_1[:, 2], label=line_label)
    plot1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plot1.set_xlabel("T, C", fontsize=10)
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


def avrami_plot_summary(frame, micro_table, tab_name_list):
    px = 1 / 100
    fig = Figure(figsize=(900 * px, 400 * px), constrained_layout=True)

    # adding the subplot
    plot2 = fig.add_subplot(111)

    # plotting the graph
    for micro_table_1, line_label in zip(micro_table, tab_name_list):
        plot2.plot(micro_table_1[:, 0], micro_table_1[:, 5], label=line_label)
    plot2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plot2.set_xlabel("T, C", fontsize=10)
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


def evolution_plot_summary(frame, trimmed, tab_name_list):
    px = 1 / 100
    fig = Figure(figsize=(900 * px, 400 * px), constrained_layout=True)

    # adding the subplot
    plot3 = fig.add_subplot(111)

    # plotting the graph
    for trimmed_1, line_label in zip(trimmed, tab_name_list):
        plot3.scatter(trimmed_1[:, 8], trimmed_1[:, 7], label=line_label)

    plot3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
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
