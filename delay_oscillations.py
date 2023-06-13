import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np


# Set up the duration for your animation
t0=0 # [hrs]
t_end=16 # [s]
dt=0.02 # [s]

# Create array for time
t=np.arange(t0,t_end+dt,dt) 

########### create arrays for the motions
### blue train ###
f1 = 0.125 # [Hz]
A1 = 7 #Amplitude [m]
train_blue = A1*np.sin(2*np.pi*f1*t)

### red train ###
f2 = 0.125 # [Hz]
A2 = -7 #Amplitude [m]
train_red = A1*np.cos(2*np.pi*f2*t)

############ CARS #################
y_i = 13
car_green = y_i-2*(t-2)**2 #t - delay 
car_purple=y_i-2*(t-6)


######################## ANIMATION ##############################
frame_amount=len(t)

def update_plot(num):

    X_blue.set_data(t[0:num],train_blue[0:num])
    X_red.set_data(t[0:num],train_red[0:num])

    block_blue.set_data([train_blue[num]-0.45,train_blue[num]+0.45],[3.5,3.5])
    block_red.set_data([train_red[num]-0.45,train_red[num]+0.45],[1.5,1.5])

    if t[num]>=2:    
        block_green.set_data([3.5, 3.5],[car_green[num]-0.5,car_green[num]+0.5])
        Y_green.set_data(t[int(2/dt):num],car_green[int(2/dt):num])
    else:
        block_green.set_data([3.5, 3.5],[y_i-0.5,y_i+0.5])
        Y_green2.set_data(t[0:num],y_i)

    # block_purple.set_data([1.5, 1.5],[car_purple[num]-0.5,car_purple[num]+0.5])


    return X_red, X_blue, block_red, block_blue, block_green,Y_green, Y_green2,


fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

############ subplot 0 ##########################

ax0 = fig.add_subplot(gs[0,0],facecolor=(0.9,0.9,0.9))
X_blue, = ax0.plot([],[],'-b',linewidth=3,label="X_blue ="+str(A1)+'*sin(2*pi*'+str(f1)+'*t)')
X_red, = ax0.plot([],[],'-r',linewidth=3,label="X_red ="+str(A2)+'*cos(2*pi*'+str(f2)+'*t)')
plt.xlim(t0,t_end)
plt.ylim(-8,8)
plt.xlabel("time [s]")
plt.ylabel("X [m]")
plt.grid(True)
#put the x_axis in the middle position
ax0.spines['bottom'].set_position('center')
ax0.xaxis.set_label_coords(0.5,0)
plt.legend(bbox_to_anchor=(1,1.2),fontsize="medium")

############ subplot 1 ##########################

ax1 = fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
Y_green, = ax1.plot([],[],'-g',linewidth=3)
#alpha ->transparency
Y_green2, = ax1.plot([],[],'-g',linewidth=3, alpha=0.3)
Y_purple, = ax1.plot([],[],'-m',linewidth=3)
Y_purple2, = ax1.plot([],[],'-m',linewidth=3, alpha=0.3)
plt.xlim(t0,t_end)
plt.ylim(-2,y_i+1)
plt.xlabel("time [s]")
plt.ylabel("X [m]")
plt.grid(True)
#put the x_axis in the middle position
ax1.spines['bottom'].set_position(('data',0))

ax1.xaxis.set_label_coords(0.5,0)

############ subplot 2 ##########################

ax2 = fig.add_subplot(gs[:,1],facecolor=(0.9,0.9,0.9))
block_blue, = ax2.plot([],[],'-b',linewidth=28)
block_red, = ax2.plot([],[],'-r',linewidth=28)
block_green, = ax2.plot([],[],'-g',linewidth=24)
block_purple, = ax2.plot([],[],'purple',linewidth=24)

#create danger zone
danger_zone_1, = ax2.plot([3,4],[1,1],'-k',linewidth=3)
danger_zone_2, = ax2.plot([3,4],[2,2],'-k',linewidth=3)
danger_zone_3, = ax2.plot([3,3],[1,2],'-k',linewidth=3)
danger_zone_4, = ax2.plot([4,4],[1,2],'-k',linewidth=3)

danger_zone2_1, = ax2.plot([3,4],[3,3],'-k',linewidth=3)
danger_zone2_2, = ax2.plot([3,4],[4,4],'-k',linewidth=3)
danger_zone2_3, = ax2.plot([3,3],[3,4],'-k',linewidth=3)
danger_zone2_4, = ax2.plot([4,4],[3,4],'-k',linewidth=3)

danger_zon3_1, = ax2.plot([-3,-4],[3,3],'-k',linewidth=3)
danger_zon3_2, = ax2.plot([-3,-4],[4,4],'-k',linewidth=3)
danger_zon3_3, = ax2.plot([-3,-3],[3,4],'-k',linewidth=3)
danger_zon3_4, = ax2.plot([-4,-4],[3,4],'-k',linewidth=3)

danger_zone4_1, = ax2.plot([-3,-4],[1,1],'-k',linewidth=3)
danger_zone4_2, = ax2.plot([-3,-4],[2,2],'-k',linewidth=3)
danger_zone4_3, = ax2.plot([-3,-3],[1,2],'-k',linewidth=3)
danger_zone4_4, = ax2.plot([-4,-4],[1,2],'-k',linewidth=3)

bbox_green = dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='g',lw='1')
bbox_purple = dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='purple',lw='1')
ax2.text(0.3,y_i+1.5,"car green",size=10,color='g',bbox=bbox_green)
ax2.text(-7.8,y_i+1.5,"car purple",size=10,color='g',bbox=bbox_purple)

plt.xlim(-max(A1,A2)-1,max(A1,A2)+1)
plt.ylim(-2,y_i+1)
plt.xlabel("time [s]")
plt.ylabel("X [m]")
plt.grid(True)
#put the x_axis in the middle position
ax2.spines['bottom'].set_position(('data',0))
ax2.spines['left'].set_position("center")

ax2.xaxis.set_label_coords(0.5,0)
ax2.yaxis.set_label_coords(0,0.5)
#delete 0 in the axis
plt.xticks(np.concatenate([np.arange(-7-1,0,1),np.arange(1,7+2,1)]),size=10)
plt.yticks(np.concatenate([np.arange(-2-1,0,1),np.arange(1,y_i+2,1)]),size=10)



plane_ani = animation.FuncAnimation(fig,update_plot,frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()