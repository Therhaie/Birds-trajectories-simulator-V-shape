import tkinter as tk
import numpy as np
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import customtkinter as ctk

from Bird_class import Birds
from Plot_frame import PlotFrame
from V_shape_formation import Formation
from Simulation_parameter_frame import ParametersFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Birds Simulation")
        self.geometry_x = 1000
        self.geometry_y = 700
        self.geometry(f"{self.geometry_x}x{self.geometry_y}]")
        self.minsize(1000, 600)
        
        # Parameters for the simulation
        self.width, self.height, self.depth = 10000, 10000, 10000
        self.distance_x, self.distance_y, self.distance_z = 50, 50, 0
        self.num_birds = 15
        self.time_between_refreshing = 100
        
        # every code under this will have to move because the parameters will need to be actualized
        # creation fo the flock
        self.formation = Formation(np.zeros(3), self.num_birds, self.distance_x, self.distance_y, self.distance_z)
        self.formation.create_flock()
        self.speed_up = 20
        

        # start of the plot
        self.plot_frame = PlotFrame(self)
        self.parameters_frame = ParametersFrame(self)
        # self.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()
