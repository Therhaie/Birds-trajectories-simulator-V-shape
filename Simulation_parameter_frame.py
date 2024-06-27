import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from Bird_class import Birds
from datetime import datetime, timedelta
from V_shape_formation import Formation
from File_parser import directional_force
from Writting_file import writting_to_csv
import numpy as np
import customtkinter as ctk

class ParametersFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_widgets()
        self.Text_zones()

    def init_widgets(self):
        ctk.CTkLabel(self, fg_color='red').pack(expand=True, fill='both')
        self.place(x=820, y=0, relwidth=0.07, relheight=0.05)

    def Text_zones(self):
        self.text_num_birds = tk.Text(self, height=1, width=10)
        self.text_num_birds.place(relx=0.95, rely=0.9, anchor='nw')