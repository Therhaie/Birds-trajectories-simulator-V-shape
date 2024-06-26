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

class PlotFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.time = 0
        self.running = False
        self.init_widgets()
        self.create_plot()

    def init_widgets(self):
        ttk.Label(self, background='dark gray').pack(expand=True, fill='both')
        self.place(x=0, y=0, relwidth=0.9, relheight=0.9)
        self.button_plot()

    def create_plot(self):
        self.fig = Figure(figsize=(10, 7))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)
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

        writting_to_csv(self.parent, total_seconds)

        self.parent.formation.update_birds(self.parent.speed_up * directional_force(path)[0][self.time], self.parent.width, self.parent.height, self.parent.depth, 'incremented')
        self.time += 1
        self.update_plot()
        self.after(self.parent.time_between_refreshing, self.plot_graphique_dynamic)
    
    
    # def plot_graphique_dynamic(self):
    #     if not self.running:
    #         return
    #     # compute of the directional force
    #     path = r'C:\Users\ththy\Desktop\Stage_Thales\birds_trajectories_simulation\Dataset\Local_flight_paths_of_nocturnally_migrating_birds\data_processed\trajectory_0_len160.csv'
    #     #print(directional_force(path))
    #     print(self.time)
        
    #     #handling the time
    #     current_time = str(directional_force(path)[1].iloc[self.time])
    #     format_string = '%Y-%m-%d %H:%M:%S.%f'
    #     date_current_time = datetime.strptime(current_time, format_string)
    #     init_time = datetime.strptime(str(directional_force(path)[1].iloc[0]), format_string)
    #     print(current_time)

    #     # Writte the point in the file
    #     writting_to_csv(self.parent, date_current_time.minute * 60 + date_current_time.second - init_time)

    #     #input_trajectories = directional_force

    #     self.parent.formation.update_birds(self.parent.speed_up * directional_force(path)[0][self.time],self.parent.width, self.parent.height, self.parent.depth, 'incremented')
    #     self.time += 1
    #     self.update_plot()
    #     # self.after(100, self.plot_graphique_dynamic)  # Schedule the next update
    #     self.after(self.parent.time_between_refreshing, self.plot_graphique_dynamic)  # Schedule the next update

    def start_plotting(self):
        if not self.running:
            self.running = True
            self.plot_graphique_dynamic()

    def button_plot(self):
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10), padding=8)

        # launch simulation button
        plot_but = ttk.Button(self, text='Start Plotting', command=self.start_plotting, style="TButton")
        plot_but.place(relx=0.5, rely=0.95, anchor=tk.NE)

        # stop button
        stop_but = ttk.Button(self, text='Stop Plotting', command=self.stop_plotting, style="TButton")
        stop_but.place(relx=0.6, rely=0.95, anchor=tk.NE)

        # clear button
        clear_but = ttk.Button(self, text='Clear Plot', command=self.create_plot, style="TButton")
        clear_but.place(relx=0.7, rely=0.95, anchor=tk.NE)
    
    def stop_plotting(self):
        self.running = False
        # self.after_cancel(self.plot_graphique_dynamic)
        # self.time = 0