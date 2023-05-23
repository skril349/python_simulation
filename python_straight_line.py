'''
LICENSE AGREEMENT
In relation to this Python file:
1. Copyright of this Python file is owned by the author: Mark Misin
2. This Python code can be freely used and distributed
3. The copyright label in this Python file such as
copyright=ax_main.text(x,y,'© Mark Misin Engineering',size=z)
that indicate that the Copyright is owned by Mark Misin MUST NOT be removed.

WARRANTY DISCLAIMER!
This Python file comes with absolutely NO WARRANTY! 
In no event can the author of this Python file be held responsible
for whatever happens in relation to this Python file.
For example, if there is a bug in the code and because of that a project,
invention, or whatever it is used for fails - the author is NOT RESPONSIBLE!
'''



import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up the duration for your animation
t0=0 # [hrs]
t_end=2 # [hrs]
dt=0.005 # [hrs]

# Create array for time
t=np.arange(t0,t_end+dt,dt)

# Create an x array
x=800*t # [km]

# Create a y array
altitude=2 # [km]
y=np.ones(len(t))*altitude

# Speed in the x direction
speed_x=np.ones(len(t))*800

################## ANIMATION ####################
frame_amount=len(t)
dot=np.zeros(frame_amount)
n=20
for i in range(0,frame_amount):
    if i==n:
        dot[i]=x[n]
        n=n+20
    else:
        dot[i]=x[n-20]

def update_plot(num):

    # 1st subplot
    plane_trajectory.set_data(dot[0:num],y[0:num])

    plane_1.set_data([x[num]-40,x[num]+20],[y[num],y[num]])
    plane_2.set_data([x[num]-20,x[num]],[y[num]+0.3,y[num]])
    plane_3.set_data([x[num]-20,x[num]],[y[num]-0.3,y[num]])
    plane_4.set_data([x[num]-40,x[num]-30],[y[num]+0.15,y[num]])
    plane_5.set_data([x[num]-40,x[num]-30],[y[num]-0.15,y[num]])

    ax0_vertical.set_data([x[num],x[num]],[0,y[num]])

    stopwatch0.set_text(str(round(t[num],1))+' hrs')
    dist_counter0.set_text(str(int(x[num]))+' km')

    # 2nd subplot
    x_dist.set_data(t[0:num],x[0:num])
    horizontal_line.set_data([t[0],t[num]],[x[num],x[num]])
    vertical_line.set_data([t[num],t[num]],[x[0],x[num]])

    # 3rd subplot
    speed.set_data(t[0:num],speed_x[0:num])
    vertical_line_ax4.set_data([t[num],t[num]],[0,speed_x[num]])
    if num!=0:
        division_x_dist.set_text(str(int(x[num])))
        division_time.set_text(str(round(t[num],3)))
        division_speed.set_text('= '+str(int(round(x[num]/t[num],1)))+' km/hr')

    return plane_trajectory,plane_1,plane_2,plane_3,plane_4,plane_5,\
    stopwatch0,dist_counter0,x_dist,horizontal_line,vertical_line,ax0_vertical,\
    speed,vertical_line_ax4,division_x_dist,division_time,division_speed


fig=plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

# Subplot 1
ax0=fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9))

# Line following the airplane
plane_trajectory,=ax0.plot([],[],'r:o',linewidth=2)

# Airplane lines
plane_1,=ax0.plot([],[],'k',linewidth=10)
plane_2,=ax0.plot([],[],'k',linewidth=5)
plane_3,=ax0.plot([],[],'k',linewidth=5)
plane_4,=ax0.plot([],[],'k',linewidth=3)
plane_5,=ax0.plot([],[],'k',linewidth=3)

ax0_vertical,=ax0.plot([],[],'k:o',linewidth=2)

# Draw houses
house_1,=ax0.plot([100,100],[0,1.0],'k',linewidth=7)
house_2,=ax0.plot([300,300],[0,1.0],'k',linewidth=7)
house_3,=ax0.plot([700,700],[0,0.7],'k',linewidth=15)
house_4,=ax0.plot([900,900],[0,0.9],'k',linewidth=10)
house_5,=ax0.plot([1300,1300],[0,1.0],'k',linewidth=20)

box_object=dict(boxstyle='circle',fc=(0.1,0.9,0.9),ec='r',lw=10)
stopwatch0=ax0.text(1400,0.65,'',size=20,color='g',bbox=box_object)

box_object2=dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='g',lw=1)
dist_counter0=ax0.text(1000,0.5,'',size=20,color='r',bbox=box_object2)

# Copyright
copyright=ax0.text(0,(altitude+1)*3.2/3,'© Mark Misin Engineering',size=15)


# Subplot properties
plt.xlim(x[0],x[-1])
plt.ylim(0,y[0]+1)
plt.xticks(np.arange(x[0],x[-1]+1,x[-1]/4),size=15)
plt.yticks(np.arange(0,y[-1]+2,y[-1]/y[-1]),size=15)
plt.xlabel('x-distance',fontsize=15)
plt.ylabel('y-distance',fontsize=15)
plt.title('Airplane',fontsize=20)
plt.grid(True)


# Subplot 2
ax2=fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
x_dist,=ax2.plot([],[],'-b',linewidth=3,label='X=800*t')
horizontal_line,=ax2.plot([],[],'r:o',linewidth=2,label='horizontal line')
vertical_line,=ax2.plot([],[],'g:o',linewidth=2,label='vertical line')
plt.xlim(t[0],t[-1])
plt.ylim(x[0],x[-1])
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.yticks(np.arange(x[0],x[-1]+1,x[-1]/4))
plt.xlabel('time [hrs]',fontsize=15)
plt.ylabel('x-distance [km]',fontsize=15)
plt.title('X-distance VS time',fontsize=15)
plt.grid(True)
plt.legend(loc='upper left',fontsize='x-large')

# Subplot3
ax4=fig.add_subplot(gs[1,1], facecolor=(0.9,0.9,0.9))
speed,=ax4.plot([],[],'-b',linewidth=3,label='ΔX/Δt = 800')
vertical_line_ax4,=ax4.plot([],[],'b:o',linewidth=2)
division_line,=ax4.plot([0.08,0.37],[995,995],'k',linewidth=1)
division_x_dist=ax4.text(0.1,1015,'',fontsize=20,color='r')
division_time=ax4.text(0.1,865,'',fontsize=20,color='g')
division_speed=ax4.text(0.4,950,'',fontsize=20,color='b')
plt.xlim(t[0],t[-1])
plt.ylim(0,speed_x[-1]*2)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4),size=15)
plt.yticks(np.arange(0,speed_x[-1]*2+1,speed_x[-1]*2/4),size=15)
plt.xlabel('time [hrs]',fontsize=15)
plt.ylabel('speed [km/hr]',fontsize=15)
plt.title('Speed as a function of time',fontsize=15)
plt.grid(True)
plt.legend(loc='upper right',fontsize='x-large')




plane_ani=animation.FuncAnimation(fig,update_plot,
    frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()



###################################################################
