import customtkinter as cst
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import matplotlib.pyplot as plt


def plot_1(frame, inflection, table):
    px = 1 / 100
    fig = Figure(figsize=(400 * px, 280 * px))


    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(table["Temp"], table["DSC"])
    plot1.scatter(inflection["Temp"], inflection["DSC"])
    plot1.plot(inflection["Temp"], inflection["DSC"])

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
    fig = Figure(figsize=(400 * px, 280 * px))

    # adding the subplot
    plot2 = fig.add_subplot(111)

    # plotting the graph
    plot2.plot(micro_table["Temp"], micro_table["Conversion_rate"])

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
    fig = Figure(figsize=(400 * px, 280 * px))

    # adding the subplot
    plot3 = fig.add_subplot(111)

    # plotting the graph
    plot3.scatter(trimmed["ln_Time"], trimmed["ln_min_ln_Conversion_rate"])

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
