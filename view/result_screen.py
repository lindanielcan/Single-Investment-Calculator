import tkinter
from tkinter import Toplevel
from view import main_screen
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


class ResultScreen():
    def __init__(self, Tk):
        self.main_screen = Tk
        pass

    def open(self):
        top = Toplevel(self.main_screen, height=500, width=600, bg=main_screen.BACKGROUND_COLOR, highlightthickness=0)
        top.resizable(False, False)
        top.title("Result")
        self.draw_graph(top)
        top.mainloop()

    def draw_graph(self, top):
        """Draws a graph on the screen."""
        # the figure that will contain the plot
        fig = Figure(figsize=(5, 5),
                     dpi=100)

        # list of squares
        y = [i ** 2 for i in range(101)]

        # adding the subplot
        plot1 = fig.add_subplot(111)

        # plotting the graph
        plot1.plot(y)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                   master=top)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().grid(row=0, column=0)