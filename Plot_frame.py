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

# class PlotFrame(ctk.CTkFrame):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.parent = parent
#         self.time = 0
#         self.running = False
#         self.init_widgets()
#         self.create_plot()

#     def init_widgets(self):
#         ctk.CTkLabel(self, fg_color='blue').pack(expand=True, fill='both')
#         self.place(x=0, y=0, relwidth=0.7, relheight=1)
#         self.button_plot()

#     def create_plot(self):
#         self.fig = Figure(figsize=(10, 7))
#         self.ax = self.fig.add_subplot(111, projection='3d')
#         self.canvas = FigureCanvasTkAgg(self.fig, master=self)
#         self.canvas.get_tk_widget().place(relx=0.0, rely=0.0, relwidth=1, relheight=0.7)
#         self.canvas.draw()

#     def update_plot(self):
#         self.ax.clear()
#         for Birds in self.parent.formation:
#             self.ax.scatter(Birds.position[0], Birds.position[1], Birds.position[2], color='b', marker='o')
#         self.ax.set_xlim([0, self.parent.width])
#         self.ax.set_ylim([0, self.parent.height])
#         self.ax.set_zlim([0, self.parent.depth])
#         self.canvas.draw()

#     def plot_graphique_dynamic(self):
#         if not self.running:
#             return

#         path = r'C:\Users\ththy\Desktop\Stage_Thales\birds_trajectories_simulation\Dataset\Local_flight_paths_of_nocturnally_migrating_birds\data_processed\trajectory_0_len160.csv'

#         current_time = str(directional_force(path)[1].iloc[self.time])
#         format_string = '%Y-%m-%d %H:%M:%S.%f'
#         date_current_time = datetime.strptime(current_time, format_string)
#         init_time = datetime.strptime(str(directional_force(path)[1].iloc[0]), format_string)
#         time_diff = date_current_time - init_time
#         total_seconds = time_diff.total_seconds()
#         print("total second", total_seconds)

#         writting_to_csv(self.parent, total_seconds)

#         self.parent.formation.update_birds(self.parent.speed_up * directional_force(path)[0][self.time], self.parent.width, self.parent.height, self.parent.depth, 'incremented')
#         self.time += 1
#         self.update_plot()
#         self.after(self.parent.time_between_refreshing, self.plot_graphique_dynamic)
#   #     self.after(self.parent.time_between_refreshing, self.plot_graphique_dynamic)  # Schedule the next update

#     def start_plotting(self):
#         if not self.running:
#             self.running = True
#             self.plot_graphique_dynamic()

#     def button_plot(self):
#         # start button
#         plot_but = ctk.CTkButton(self, text='Start Plotting', command=self.start_plotting, width=100, height=30)
#         plot_but.configure(font=("Arial", 10))
#         plot_but.place(relx=0.1, rely=0.72, anchor="w")

#         # stop button
#         stop_but = ctk.CTkButton(self, text='Stop Plotting', command=self.stop_plotting, width=100, height=30)
#         stop_but.configure(font=("Arial", 10))
#         stop_but.place(relx=0.2, rely=0.72, anchor="w")

#         # clear button
#         clear_but = ctk.CTkButton(self, text='Clear Plot', command=self.create_plot, width=100, height=30)
#         clear_but.configure(font=("Arial", 10))
#         clear_but.place(relx=0.3, rely=0.72, anchor="w")
#     # def button_plot(self):
#     #     # start button
#     #     plot_but = ctk.CTkButton(self, text='Start Plotting', command=self.start_plotting, width=100, height=30)
#     #     plot_but.configure(font=("Arial", 10))
#     #     plot_but.grid(row=0, column=0, padx=10)

#     #     # stop button
#     #     stop_but = ctk.CTkButton(self, text='Stop Plotting', command=self.stop_plotting, width=100, height=30)
#     #     stop_but.configure(font=("Arial", 10))
#     #     stop_but.grid(row=0, column=1, padx=10)

#     #     # clear button
#     #     clear_but = ctk.CTkButton(self, text='Clear Plot', command=self.create_plot, width=100, height=30)
#     #     clear_but.configure(font=("Arial", 10))
#     #     clear_but.grid(row=0, column=2, padx=10)
            
#     def stop_plotting(self):
#         self.running = False
#         # self.after_cancel(self.plot_graphique_dynamic)
#         # self.time = 0

######################################################################

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

class PlotFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.time = 0
        self.running = False
        self.init_widgets()
        self.create_plot()

    def init_widgets(self):
        ctk.CTkLabel(self, fg_color='blue').grid(row=0, column=0, sticky="nsew")
        self.grid(row=0, column=0, sticky="nsew")
        self.button_plot()

    def create_plot(self):
        self.fig = Figure(figsize=(10, 7))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")
        self.canvas.draw()

    def update_plot(self):
        self.ax.clear()
        for Birds in self.parent.formation:
            self.ax.scatter(Birds.position[0], Birds.position[1], Birds.position[2], color='b', marker='o')
        self.ax.set_xlim([0, self.parent.width])
        self.ax.set_ylim([0, self.parent.height])
        self.ax.set_zlim([0, self.parent.depth])
        self.canvas.draw()

    def plot_graphique_dynamic(self):
        if not self.running:
            return

        path = r'C:\Users\ththy\Desktop\Stage_Thales\birds_trajectories_simulation\Dataset\Local_flight_paths_of_nocturnally_migrating_birds\data_processed\trajectory_0_len160.csv'

        current_time = str(directional_force(path)[1].iloc[self.time])
        format_string = '%Y-%m-%d %H:%M:%S.%f'
        date_current_time = datetime.strptime(current_time, format_string)
        init_time = datetime.strptime(str(directional_force(path)[1].iloc[0]), format_string)
        time_diff = date_current_time - init_time
        total_seconds = time_diff.total_seconds()
        print("total second", total_seconds)

        writting_to_csv(self.parent, total_seconds)

        self.parent.formation.update_birds(self.parent.speed_up * directional_force(path)[0][self.time], self.parent.width, self.parent.height, self.parent.depth, 'incremented')
        self.time += 1
        self.update_plot()
        self.after(self.parent.time_between_refreshing, self.plot_graphique_dynamic)

    def start_plotting(self):
        if not self.running:
            self.running = True
            self.plot_graphique_dynamic()

    def button_plot(self):
    # start button
        plot_but = ctk.CTkButton(self, text='Start Plotting', command=self.start_plotting, width=100, height=30)
        plot_but.configure(font=("Arial", 10))
        plot_but.grid(row=0, column=0, padx=10, sticky="w")

        # stop button
        stop_but = ctk.CTkButton(self, text='Stop Plotting', command=self.stop_plotting, width=100, height=30)
        stop_but.configure(font=("Arial", 10))
        stop_but.grid(row=0, column=1, padx=10, sticky="w")

        # clear button
        clear_but = ctk.CTkButton(self, text='Clear Plot', command=self.create_plot, width=100, height=30)
        clear_but.configure(font=("Arial", 10))
        clear_but.grid(row=0, column=2, padx=10, sticky="w")


    def stop_plotting(self):
        self.running = False