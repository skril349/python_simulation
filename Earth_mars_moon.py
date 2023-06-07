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
# print(sphere_x_Earth.round(2))
# print("\n")
# print(sphere_y_Earth.round(2))
# print("\n")

################# ANIMATION #######################
frame_amount = len(t)
width_ratio = 1.2
y_f = -10 # [m]
dy = 10 # [m]


def update_plot(num):

    sphere_Earth.set_data(sphere_x_Earth,sphere_y_Earth)


    return sphere_Earth,

fig = plt.figure (figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(3,4)

ax0 = fig.add_subplot(gs[:,0], facecolor=(0.9,0.9,0.9))
sphere_Earth, = ax0.plot ([],[],'k',linewidth=3)
land_Earth = ax0.plot([-radius*width_ratio,radius*width_ratio],[-5,-5], linewidth=38)

plt.xlim = (-radius*width_ratio, radius*width_ratio)
plt.ylim = (y_f,y_i+dy)
plt.xticks(np.arange(-radius, radius+1,radius))
plt.yticks(np.arange(y_f,y_i+2*dy,dy))
plt.ylabel("Altitude [m]")
plt.title("Earth")


plane_ani = animation.FuncAnimation(fig,update_plot,frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()