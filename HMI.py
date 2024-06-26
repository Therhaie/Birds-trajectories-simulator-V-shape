import tkinter as tk
import numpy as np
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from Bird_class import Birds
from Plot_frame import PlotFrame
from V_shape_formation import Formation

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Birds Simulation")
        self.geometry("1000x700")
        self.minsize(1000, 600)
        
        # Parameters for the simulation
        self.width, self.height, self.depth = 10000, 10000, 10000
        self.distance_x, self.distance_y, self.distance_z = 50, 50, 0
        self.num_birds = 15
        self.time_between_refreshing = 100
        
        # creation fo the flock
        self.formation = Formation(np.zeros(3), self.num_birds, self.distance_x, self.distance_y, self.distance_z)
        self.formation.create_flock()
        self.speed_up = 20
        

        # start of the plot
        self.plot_frame = PlotFrame(self)
        self.mainloop()

if __name__ == "__main__":
    App()
