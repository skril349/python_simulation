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
print(y)

################ANIMATION##################

#frame quantity
frame_amount = len(t)
#function update_plot
def update_plot(num):

    plane_trajectory.set_data(x[0:num],y[0:num])
    plane_1.set_data([x[num]-40,x[num]+20],[y[num],y[num]])
    plane_2.set_data([x[num]-20,x[num]],[y[num]+0.3,y[num]])
    plane_3.set_data([x[num]-20,x[num]],[y[num]-0.3,y[num]])
    plane_4.set_data([x[num]-40,x[num]-30],[y[num]+0.15,y[num]])
    plane_5.set_data([x[num]-40,x[num]-30],[y[num]-0.15,y[num]])

    return plane_trajectory,plane_1,plane_2,plane_3,plane_4,plane_5,

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
plane_trajectory, = ax0.plot([],[],'g',linewidth=2)

#plane design
plane_1,=ax0.plot([],[],'k',linewidth=10)
plane_2,=ax0.plot([],[],'k',linewidth=5)
plane_3,=ax0.plot([],[],'k',linewidth=5)
plane_4,=ax0.plot([],[],'k',linewidth=3)
plane_5,=ax0.plot([],[],'k',linewidth=3)


#draw houses
house_1, = ax0.plot([100,100],[0,1.0],'k',linewidth=4)
house_2, = ax0.plot([300,300],[0,1.0],'k',linewidth=4)
house_3, = ax0.plot([900,900],[0,1.5],'k',linewidth=4)
house_4, = ax0.plot([1300,1300],[0,0.9],'k',linewidth=4)


#adding axis limits
plt.xlim(x[0], x[-1])
plt.ylim(0, y[-1]+1)

# Animation Function
plane_ani = animation.FuncAnimation(fig,update_plot,frames=frame_amount, interval=20,repeat=True,blit=True)

plt.show()