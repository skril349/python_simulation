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
altitude = 2
#np.ones create an array with t array length
y = np.ones(len(t))*altitude

################ANIMATION##################

#frame quantity
frame_amount = len(t)
dot = np.zeros(frame_amount)
n=20;

for i in range(0,frame_amount):
    if(i == n):
        dot[i] = x[i]
        n=n+20
    else: 
        dot[i] = x[n-20]

print(dot)        
#function update_plot
def update_plot(num):

    #plot1
    plane_trajectory.set_data(dot[0:num],y[0:num])
    vertical_plane.set_data([x[num],x[num]],[0,altitude])

    #plane design movement
    plane_1.set_data([x[num]-40,x[num]+20],[y[num],y[num]])
    plane_2.set_data([x[num]-20,x[num]],[y[num]+0.3,y[num]])
    plane_3.set_data([x[num]-20,x[num]],[y[num]-0.3,y[num]])
    plane_4.set_data([x[num]-40,x[num]-30],[y[num]+0.15,y[num]])
    plane_5.set_data([x[num]-40,x[num]-30],[y[num]-0.15,y[num]])

    stopwatch0.set_text(str(round(t[num],1))+'hrs')
    stopwatch1.set_text(str(round(x[num],1))+'km')

    #plot2
    #line.set_data([xi,xf],[yi,yf])
    x_dist.set_data(t[0:num],x[0:num])
    horizontal.set_data([t[0],t[num]],[x[num],x[num]])
    vertical.set_data([t[num],t[num]],[x[0],x[num]])

    return plane_trajectory,plane_1,plane_2,plane_3,plane_4,plane_5,\
    stopwatch0,stopwatch1,x_dist,horizontal,vertical,vertical_plane,

#figsize is screen 16*9
#dpi = resolution
#facecolor = color of the figure in RGB
fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
#how we will divide the screen
# 2,2 = __|__
#         |
gs = gridspec.GridSpec(2,2)

# Subplot 1
ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))
#la coma es per donar la info dins dels []
#r:o vol dir que faci la línea vermella amb punts
plane_trajectory, = ax0.plot([],[],'r:o',linewidth=2)
vertical_plane, = ax0.plot([],[],'k:o',linewidth=2)

#plane design
plane_1,=ax0.plot([],[],'k',linewidth=10)
plane_2,=ax0.plot([],[],'k',linewidth=5)
plane_3,=ax0.plot([],[],'k',linewidth=5)
plane_4,=ax0.plot([],[],'k',linewidth=3)
plane_5,=ax0.plot([],[],'k',linewidth=3)


#draw houses
house_1, = ax0.plot([100,100],[0,1.0],'k',linewidth=8)
house_2, = ax0.plot([300,300],[0,1.0],'k',linewidth=10)
house_3, = ax0.plot([900,900],[0,1.5],'k',linewidth=6)
house_4, = ax0.plot([1300,1300],[0,0.9],'k',linewidth=4)


#adding axis limits
plt.xlim(x[0], x[-1])
plt.ylim(0, y[-1]+1)
#adding ticks
plt.xticks(np.arange(x[0],x[-1]+1,x[-1]/4),size=15)
plt.yticks(np.arange(0,y[-1]+2,y[-1]/y[-1]),size=15)
#adding labels
plt.xlabel('x-distance (km)',fontsize=15)
plt.ylabel('y-distance (km)',fontsize=15)
plt.title('Airplane', fontsize=20)
plt.grid(True)


#subplot 2

ax1 = fig.add_subplot(gs[1,0], facecolor=(0.9,0.9,0.9))
horizontal, = ax1.plot([],[],'r:o',linewidth=2, label="horizontal Line")
vertical, = ax1.plot([],[],'g:o',linewidth=2, label="vertical Line")
x_dist, = ax1.plot([],[],'b',linewidth=3, label="X=800t")
plt.xlim(t[0], t[-1])
plt.ylim(x[0], x[-1])
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.yticks(np.arange(x[0],x[-1]+1,x[-1]))
plt.ylabel('x-distance (km)',fontsize=15)
plt.xlabel('time (hrs)',fontsize=15)
plt.title('x-t', fontsize=20)
plt.legend(loc="upper left",fontsize="x-large")
plt.grid(True)
#adding text
box_object = dict(boxstyle="square", fc=(0.9,0.9,0.9),ec='r',lw=1)
box_object2 = dict(boxstyle="square", fc=(0.9,0.9,0.9),ec='g',lw=1)

stopwatch0 = ax0.text(1400,0.70,'', size=20,color='r',bbox=box_object);
stopwatch1 = ax0.text(1400,0.15,'', size=20,color='g',bbox=box_object2);
# Animation Function
plane_ani = animation.FuncAnimation(fig,update_plot,frames=frame_amount, interval=20,repeat=True,blit=True)

plt.show()