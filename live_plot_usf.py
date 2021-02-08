import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('dark_background')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    df = pd.read_csv('usf.csv')
    ys = df.iloc[1:, 2].values
    xs = list(range(1, len(ys) + 1))
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()