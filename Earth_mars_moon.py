import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np


# Set up the duration for your animation
t0=0 # [hrs]
t_end=12 # [s]
dt=0.02 # [s]

# Create array for time
t=np.arange(t0,t_end+dt,dt) 

#gravity constant
g_Earth = -9.81

#position equation
n = 2
y_i = 100
y_Earth = y_i+0.5*g_Earth*t**n

#velocity array
y_Earth_Velocity = n*0.5*g_Earth*t**(n-1)

#acceleration array
y_Earth_Acceleration = (n-1)*g_Earth*t**(n-2)


def create_circle(r):
    degrees = np.arange(0,361,1)
    radians = degrees*np.pi/180
    sphere_x = r*np.cos(radians)
    sphere_y = r*np.sin(radians)
    return sphere_x, sphere_y

radius = 5
sphere_x_Earth, sphere_y_Earth = create_circle(radius)
print(sphere_x_Earth.round(2))
print("\n")
print(sphere_y_Earth.round(2))
print("\n")
