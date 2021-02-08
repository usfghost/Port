import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
#axis 1
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open('sampletext.txt', 'r').read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for line in dataArray:
        if len(line)>1:
            x,y = line.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar, yar)

ani = animation.FuncAnimation(fig, animate, interval = 100)
plt.show()