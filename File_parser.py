import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from Bird_class import Birds
import numpy as np
import pandas as pd

'''
File to parse the data and create the directional force
the actual file only focus on csv file that as been pre processed'''

def directional_force(path):
    df = pd.read_csv(path)

    # print(df.columns)

    X = df['x']
    Y = df['y']
    Z = df['z']
    
    X_diff = [X[n+1] - X[n] for n in range(len(X)-1)]
    Y_diff = [Y[n+1] - Y[n] for n in range(len(Y)-1)]
    Z_diff = [Z[n+1] - Z[n] for n in range(len(Z)-1)]

    directional_forces = [np.array((X_diff[i], Y_diff[i], Z_diff[i])) for i in range(len(X_diff))]
    return directional_forces

    

if __name__ == "__main__":
    path = r'C:\Users\ththy\Desktop\Stage_Thales\birds_trajectories_simulation\Dataset\Local_flight_paths_of_nocturnally_migrating_birds\data_processed\trajectory_0_len160.csv'
    print(directional_force(path))