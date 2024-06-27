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
from tools.Pattern_Observer import Subject, Observer

class App(ctk.CTk, Subject):
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
    
    def update_paremeters(self, num_birds, distance_x, distance_y, distance_z, time_between_refreshing, speed_up):
        self.num_birds = num_birds
        self.distance_x = distance_x
        self.distance_y = distance_y
        self.distance_z = distance_z
        self.time_between_refreshing = time_between_refreshing
        self.speed_up = speed_up
        self.notify((num_birds, distance_x, distance_y, distance_z, time_between_refreshing, speed_up))

    # getter and setter
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self.update_parameters()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self.update_parameters()

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value
        self.update_parameters()

    @property
    def distance_x(self):
        return self._distance_x

    @distance_x.setter
    def distance_x(self, value):
        self._distance_x = value
        self.update_parameters()

    @property
    def distance_y(self):
        return self._distance_y

    @distance_y.setter
    def distance_y(self, value):
        self._distance_y = value
        self.update_parameters()

    @property
    def distance_z(self):
        return self._distance_z

    @distance_z.setter
    def distance_z(self, value):
        self._distance_z = value
        self.update_parameters()

    @property
    def num_birds(self):
        return self._num_birds

    @num_birds.setter
    def num_birds(self, value):
        self._num_birds = value
        self.update_parameters()

    @property
    def time_between_refreshing(self):
        return self._time_between_refreshing

    @time_between_refreshing.setter
    def time_between_refreshing(self, value):
        self._time_between_refreshing = value
        self.update_parameters()

    @property
    def speed_up(self):
        return self._speed_up

    @speed_up.setter
    def speed_up(self, value):
        self._speed_up = value
        self.update_parameters()

    def update_parameters(self):
        self.notify((self._num_birds, self._distance_x, self._distance_y, self._distance_z, self._time_between_refreshing, self._speed_up))

if __name__ == "__main__":
    app = App()
    app.mainloop()
