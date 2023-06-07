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

################# EARTH ###########################

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

############# MARS ######################################

#gravity constant
g_Mars = -3.87

#position equation
n = 2
y_i = 100
y_Mars = y_i+0.5*g_Mars*t**n

#velocity array
y_Mars_Velocity = n*0.5*g_Mars*t**(n-1)

#acceleration array
y_Mars_Acceleration = (n-1)*g_Mars*t**(n-2)

############ MOON ################################
#gravity constant
g_Moon = -1.2

#position equation
n = 2
y_i = 100
y_Moon = y_i+0.5*g_Moon*t**n

#velocity array
y_Moon_Velocity = n*0.5*g_Moon*t**(n-1)

#acceleration array
y_Moon_Acceleration = (n-1)*g_Moon*t**(n-2)


def create_circle(r):
    degrees = np.arange(0,361,1)
    radians = degrees*np.pi/180
    sphere_x = r*np.cos(radians)
    sphere_y = r*np.sin(radians)
    return sphere_x, sphere_y

radius = 5
sphere_x_Earth, sphere_y_Earth = create_circle(radius)
sphere_x_Moon, sphere_y_Moon = create_circle(radius)
sphere_x_Mars, sphere_y_Mars = create_circle(radius)

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

    if y_Earth[num]>=radius:
        sphere_Earth.set_data(sphere_x_Earth,sphere_y_Earth+y_Earth[num])
        alt_E.set_data(t[0:num],y_Earth[0:num])
        Vel_E.set_data(t[0:num],y_Earth_Velocity[0:num])
        Acc_E.set_data(t[0:num],y_Earth_Acceleration[0:num])

    if y_Mars[num]>=radius:
        sphere_Mars.set_data(sphere_x_Mars,sphere_y_Mars+y_Mars[num])
        alt_Mars.set_data(t[0:num],y_Mars[0:num])
        Vel_Mars.set_data(t[0:num],y_Mars_Velocity[0:num])
        Acc_Mars.set_data(t[0:num],y_Mars_Acceleration[0:num])


    if y_Moon[num]>=radius:
        sphere_Moon.set_data(sphere_x_Moon,sphere_y_Moon+y_Moon[num])
        alt_M.set_data(t[0:num],y_Moon[0:num])
        Vel_M.set_data(t[0:num],y_Moon_Velocity[0:num])
        Acc_M.set_data(t[0:num],y_Moon_Acceleration[0:num])


    return sphere_Earth,alt_E,sphere_Mars, alt_Mars,alt_M, sphere_Moon, Vel_E,Vel_Mars,Vel_M,Acc_E, Acc_M, Acc_Mars,

################ EARTH FIGURE #############################

fig = plt.figure (figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(3,4)

ax0 = fig.add_subplot(gs[:,0], facecolor=(0.9,0.9,0.9))
sphere_Earth, = ax0.plot ([],[],'k',linewidth=3)
land_Earth = ax0.plot([-radius*width_ratio,radius*width_ratio],[-5,-5], linewidth=38)

plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f,y_i+dy)
plt.xticks(np.arange(-radius, radius+1,radius))
plt.yticks(np.arange(y_f,y_i+2*dy,dy))
plt.ylabel("Altitude [m]")
plt.title("Earth")

################ MARS FIGURE #############################
ax1 = fig.add_subplot(gs[:,1], facecolor=(0.9,0.9,0.9))
sphere_Mars, = ax1.plot ([],[],'k',linewidth=3)
land_Mars = ax1.plot([-radius*width_ratio,radius*width_ratio],[-5,-5], linewidth=38)

plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f,y_i+dy)
plt.xticks(np.arange(-radius, radius+1,radius))
plt.yticks(np.arange(y_f,y_i+2*dy,dy))
plt.title("Mars")

################ MOON FIGURE #############################
ax2 = fig.add_subplot(gs[:,2], facecolor=(0.9,0.9,0.9))
sphere_Moon, = ax2.plot ([],[],'k',linewidth=3)
land_Moon = ax2.plot([-radius*width_ratio,radius*width_ratio],[-5,-5], linewidth=38)

plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f,y_i+dy)
plt.xticks(np.arange(-radius, radius+1,radius))
plt.yticks(np.arange(y_f,y_i+2*dy,dy))
plt.title("Moon")

################# position ################3
ax3 = fig.add_subplot(gs[0,3],facecolor=(0.9,0.9,0.9))
alt_E,=ax3.plot([],[],'',linewidth=3,label='Alt_Earth = '+str(y_i)+' + ('+str(round(g_Earth/2,1))+')t^'+str(n)+' [m]')
alt_M,=ax3.plot([],[],'',linewidth=3,label='Alt_Moon = '+str(y_i)+' + ('+str(round(g_Moon/2,1))+')t^'+str(n)+' [m]')
alt_Mars,=ax3.plot([],[],'',linewidth=3,label='Alt_Mars = '+str(y_i)+' + ('+str(round(g_Mars/2,1))+')t^'+str(n)+' [m]')

plt.xlim(0,t_end)
plt.ylim(0,y_i)
plt.legend(loc=(0.6,0.7),fontsize='x-small')

################ velocity #############
ax4 = fig.add_subplot(gs[1,3],facecolor=(0.9,0.9,0.9))
Vel_E,=ax4.plot([],[],'',linewidth=3,label='Vel_Earth = '+str(y_i)+' + ('+str(round(g_Earth/2,1))+')t^'+str(n)+' [m]')
Vel_M,=ax4.plot([],[],'',linewidth=3,label='Vel_Moon = '+str(y_i)+' + ('+str(round(g_Moon/2,1))+')t^'+str(n)+' [m]')
Vel_Mars,=ax4.plot([],[],'',linewidth=3,label='Vel_Mars = '+str(y_i)+' + ('+str(round(g_Mars/2,1))+')t^'+str(n)+' [m]')
plt.xlim(0,t_end)
plt.ylim(y_Earth_Velocity[-1],0)
plt.legend(loc=(0.6,0.7),fontsize='x-small')

# ############### acceleration ###########
ax5 = fig.add_subplot(gs[2,3],facecolor=(0.9,0.9,0.9))
Acc_E,=ax5.plot([],[],'',linewidth=3,label='Acc_Earth = '+str(y_i)+' + ('+str(round(g_Earth/2,1))+')t^'+str(n)+' [m]')
Acc_M,=ax5.plot([],[],'',linewidth=3,label='Acc_Moon = '+str(y_i)+' + ('+str(round(g_Moon/2,1))+')t^'+str(n)+' [m]')
Acc_Mars,=ax5.plot([],[],'',linewidth=3,label='Acc_Mars = '+str(y_i)+' + ('+str(round(g_Mars/2,1))+')t^'+str(n)+' [m]')
plt.xlim(0,t_end)
plt.ylim(y_Earth_Acceleration[-1]-2,0)
plt.legend(loc=(0.6,0.7),fontsize='x-small')

plane_ani = animation.FuncAnimation(fig,update_plot,frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()