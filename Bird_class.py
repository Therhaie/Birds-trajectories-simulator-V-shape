import numpy as np

class Birds:
    def __init__(self, position, velocity):
        self.position = position #np.array(position)
        self.velocity = np.array(velocity) * 0
        self.time_step = 0

    def update_replace(self, new_position, width, height, depth, directional_force=np.zeros(3), target=None):
        '''this version of the function replace the last position by the new one'''
        #self.flock(boids, target)
        self.velocity += directional_force
        self.position = new_position
        print("position 0", self.position[0])
        self.position[0] %= width
        self.position[1] %= height
        self.position[2] %= depth
    
    def update_by_incrementing(self, diff_position, width, height, depth, directional_force=np.zeros(3), target=None):
        '''this version of the function replace the last position by the new one'''
        #self.flock(boids, target)
        self.velocity += directional_force
        self.position += diff_position
        self.position[0] %= width
        self.position[1] %= height
        self.position[2] %= depth
        

    # def attraction(self, target, attraction_strength=0.01):
    #     return (target - self.position) * attraction_strength

    # def limit_speed(self, max_speed=10):
    #     speed = np.linalg.norm(self.velocity)
    #     if speed > max_speed:
    #         self.velocity = (self.velocity / speed) * max_speed
