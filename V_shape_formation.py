import numpy as np
from Bird_class import *

class Formation():
    def __init__(self, beginning_position, number_of_birds, d_x, d_y, d_z=0):
        self.leader = beginning_position
        self.number_of_birds = number_of_birds
        self.list_birds = []
        self.dist_x = d_x
        self.dist_y = d_y
        self.dist_z = d_z

    def create_flock(self):
        self.list_birds.append(Birds(self.leader, np.array([0, 0, 0])))
        for i in range(1, self.number_of_birds):
            self.leader = self.leader + (-1)**i * i * np.array([self.dist_x, 0, 0]) - np.array([0, self.dist_y, self.dist_z])
            self.list_birds.append(Birds(self.leader, np.array([0, 0, 0])))
    
    def update_birds(self, position_value ,width, height, depth, mode='position_value'):
        if mode == 'update_replace':
            for b in self.list_birds:
                b.update_replace(position_value ,width, height, depth, np.array([0, 0, 0]), np.array([500, 500, 500]))
        else:
            for b in self.list_birds:
                b.update_by_incrementing(position_value, width, height, depth, np.array([0, 0, 0]), np.array([500, 500, 500]))
                print(b.position)


    def __iter__(self):
        return iter(self.list_birds)

if __name__ == "__main__":
    creat = Formation(np.zeros(3), 10, 2, 2, 0)
    creat.create_flock()
    for b in creat:
        print(b.position)