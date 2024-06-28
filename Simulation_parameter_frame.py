# import tkinter as tk
# from tkinter import ttk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt
# from Bird_class import Birds
# from datetime import datetime, timedelta
# from V_shape_formation import Formation
# from File_parser import directional_force
# from Writting_file import writting_to_csv
# import numpy as np
# import customtkinter as ctk

# class ParametersFrame(ctk.CTkFrame):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.parent = parent
#         self.init_widgets()
#         self.Text_zones()

#     def init_widgets(self):
#         ctk.CTkLabel(self, fg_color='red').pack(expand=True, fill='both')
#         self.place(x=820, y=0, relwidth=0.2, relheight=1)

#     def Text_zones(self):
#         self.Text_zones = ctk.CTkEntry(master=self, placeholder_text="Enter something...")
#         self.Text_zones.place(relx=0.03, rely=0.5, anchor='nw')
#         # self.text_num_birds = ctk.CTkLabel(self, text=str(self.parent.num_birds), height=1, width=10)
#         # self.text_num_birds.place(relx=0.9, rely=0.5, anchor='nw')

import customtkinter as ctk

class ParametersFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_widgets()
        self.Text_zones()

    def init_widgets(self):
        self.place(x=820, y=0, relwidth=0.2, relheight=1)

    def Text_zones(self):
        self.Text_zones = ctk.CTkEntry(master=self, placeholder_text="Enter something...") # plot the current value instead
        self.Text_zones.pack()