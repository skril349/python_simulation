import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation


#set up the duration for animation
t0 = 0
t_end = 2
dt = 0.005

#create array for time

t = np.arange(t0,t_end+dt,dt)
print(t)
#set up X array
x = 800*t
#as we can see, t is an array and we multiply every value with 800
print(x)
#set up y array
altutide = 2
#np.ones create an array with t array length
y = np.ones(len(t))*altitude
print(y)

################ANIMATION##################

#frame quantity
frame_amount = len(t)
#function update_plot
def update_plot(num):
    
    return

plane_ani = animation.FuncAnimation(fig,update_plot,frames=frame_amount, interval=20,repeat=True,blit=True)

plt.show()