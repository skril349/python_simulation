import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np


# Set up the duration for your animation
t0=0 # [hrs]
t_end=60 # [s]
dt=0.04 # [s]

# Create array for time
t=np.arange(t0,t_end+dt,dt) 

########### create zero arrays for the motions #############

volume_Tank1 = np.zeros(len(t))
volume_Tank2 = np.zeros(len(t))
volume_Tank3 = np.zeros(len(t))

for i in range (0,len(t)):
    #Tank 1
    if t[i] <= 22.5:
        volume_Tank1[i]=50+2*t[i]
    elif t[i] <= 32.5:
        volume_Tank1[i]=95
        templ1= i
    elif t[i] <= 32.5+45**0.5:
        volume_Tank1[i]=95-(t[i]-t[templ1])**2
        templ2=i
    elif t[i] <=42.5+45**0.5:
        volume_Tank1[i]=50+np.sin(2*np.pi*1*(t[i]-t[templ2]))
    else:
        volume_Tank1[i]=50

#Tank 2
    if t[i] <= 27.5:
        volume_Tank2[i]=40+2*t[i]
    elif t[i] <= 32.5:
        volume_Tank2[i]=95
        templ21= i
    elif t[i] <= 32.5+45**0.5:
        volume_Tank2[i]=95-(t[i]-t[templ21])**2
        templ22=[i]
    elif t[i] <=37.5+45**0.5:
        volume_Tank2[i]=50+3*np.sin(2*np.pi*1*(t[i]-t[templ22]))
        templ23 = i
    elif t[i] <=42.5+45**0.5:
        volume_Tank2[i]=50+np.sin(2*np.pi*1*(t[i]-t[templ23]))        
    else:
        volume_Tank2[i]=50

    #Tank 3
    if t[i] <= 32.5:
        volume_Tank3[i]=30+2*t[i]
        templ31= i
    elif t[i] <= 32.5+45**0.5:
        volume_Tank3[i]=95-(t[i]-t[templ31])**2
        templ32=i
    elif t[i] <=42.5+45**0.5:
        volume_Tank3[i]=50-np.sin(2*np.pi*1*(t[i]-t[templ32]))
    else:
        volume_Tank3[i]=50
######################## ANIMATION ##############################
frame_amount=len(t)

###########create water tanks ################

radius = 5
volume_i = 0
volume_f = 100
dVol = 10


def update_plot(num):

    # Tank 1:
    tank_1.set_data([-radius,radius],[volume_Tank1[num],volume_Tank1[num]])
    tank_12.set_data([0,0],[-64,volume_Tank1[num]-64])
    tnk_1.set_data([t[0:num], volume_Tank1[0:num]])
    tnk_1Z.set_data([t[0:num], volume_Tank1[0:num]])

    # Tank 2:
    tank_2.set_data([-radius,radius],[volume_Tank2[num],volume_Tank2[num]])
    tank_22.set_data([0,0],[-64,volume_Tank2[num]-64])
    tnk_2.set_data([t[0:num], volume_Tank2[0:num]])
    tnk_2Z.set_data([t[0:num], volume_Tank2[0:num]])



    #Tank 3:
    tank_3.set_data([-radius,radius],[volume_Tank3[num],volume_Tank3[num]])
    tank_32.set_data([0,0],[-64,volume_Tank3[num]-64])
    tnk_3.set_data([t[0:num], volume_Tank3[0:num]])
    tnk_3Z.set_data([t[0:num], volume_Tank3[0:num]])



    return tank_1, tank_2, tank_3, tank_12, tank_22, tank_32, tnk_1, tnk_2, tnk_3, tnk_1Z, tnk_2Z, tnk_3Z, 

fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,3)

############ subplot 0 ##########################

ax0 = fig.add_subplot(gs[0,0],facecolor=(0.9,0.9,0.9))
tank_1, = ax0.plot([],[],'r',linewidth=4)
tank_12, = ax0.plot([],[],'royalblue',linewidth=260)
plt.xlim(-radius,radius)
plt.ylim(volume_i, volume_f)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(volume_i,volume_f+dVol,dVol))
plt.ylabel('tank volume [m^3]')
plt.title('Tank 1')
############ subplot 1 ##########################

ax1 = fig.add_subplot(gs[0,1],facecolor=(0.9,0.9,0.9))
tank_2, = ax1.plot([],[],'r',linewidth=4)
tank_22, = ax1.plot([],[],'royalblue',linewidth=260)
plt.xlim(-radius,radius)
plt.ylim(volume_i, volume_f)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(volume_i,volume_f+dVol,dVol))
plt.ylabel('tank volume [m^3]')
plt.title('Tank 2')
############ subplot 2 ##########################

ax2 = fig.add_subplot(gs[0,2],facecolor=(0.9,0.9,0.9))
tank_3, = ax2.plot([],[],'r',linewidth=4)
tank_32, = ax2.plot([],[],'royalblue',linewidth=260)
plt.xlim(-radius,radius)
plt.ylim(volume_i, volume_f)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(volume_i,volume_f+dVol,dVol))
plt.ylabel('tank volume [m^3]')
plt.title('Tank 3')
############ subplot 3 ##########################

ax3 = fig.add_subplot(gs[1,:2],facecolor=(0.9,0.9,0.9))
tnk_1, =ax3.plot([],[],'blue',linewidth=3,label="Tank 1")
tnk_2, =ax3.plot([],[],'green',linewidth=3,label="Tank 2")
tnk_3, =ax3.plot([],[],'red',linewidth=3,label="Tank 3")
plt.xlim(t0,t_end)
plt.ylim(volume_i, volume_f)
plt.xticks([0,22.5, 27.5,32.5,32.5+45**0.5,37.5+45**0.5,42.5+45**0.5, 60])
plt.yticks(np.arange(volume_i,volume_f+dVol,dVol))
plt.ylabel('tank volume [m^3]')
plt.xlabel("Time [s]")
plt.title('Tanks')
plt.legend(loc='upper right',fontsize='small')
plt.grid(True)
############ subplot 4 ##########################

ax4 = fig.add_subplot(gs[1,2],facecolor=(0.9,0.9,0.9))
tnk_1Z, =ax4.plot([],[],'blue',linewidth=3,label="Tank 1")
tnk_2Z, =ax4.plot([],[],'green',linewidth=3,label="Tank 2")
tnk_3Z, =ax4.plot([],[],'red',linewidth=3,label="Tank 3")
plt.xlim(50,t_end)
plt.ylim(volume_i, volume_f)
plt.xticks([0,22.5, 27.5,32.5,32.5+45**0.5,37.5+45**0.5,42.5+45**0.5, 60])
plt.yticks(np.arange(volume_i,volume_f+dVol,dVol))
plt.ylabel('tank volumes zoomed [m^3]')
plt.xlabel("Time [s]")
plt.legend(loc='upper right',fontsize='small')
plt.axis([38,50,47,53])
plt.grid(True)

plane_ani = animation.FuncAnimation(fig,update_plot,frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()