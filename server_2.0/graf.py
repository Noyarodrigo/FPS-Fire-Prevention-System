import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import multiprocessing


style.use('fivethirtyeight')

xmin = 0
xmax = 60
critico_tmp = 70
critico_h = 60 
ax1_data = []
ax2_data = []
ax3_data = []
i = 0
y = []

fig = plt.figure()
ax1 = fig.add_subplot(1,3,1,xlim= (xmin,xmax))
ax1.title.set_text('Tmp36')
ax1.set_xlabel('Valor')
ax1.set_ylabel('Muestra')
ax1.axhline(y=critico_tmp, xmin=0, xmax=1)

ax2 = fig.add_subplot(1,3,2,xlim= (xmin,xmax))
ax2.title.set_text('Humedad')
ax2.set_xlabel('Valor')
ax2.set_ylabel('Muestra')
ax2.axhline(y=critico_h, xmin=0, xmax=1)

ax3 = fig.add_subplot(1,3,3,xlim= (xmin,xmax))
ax3.title.set_text('TmpDHT')
ax3.set_xlabel('Valor')
ax3.set_ylabel('Muestra')
ax3.axhline(y=critico_h, xmin=0, xmax=1)

def animate(q):
    while True:
        if not q.empty():
            read = q.get()
            print(read)
            i =+ 1
            at, h, t = read.split(',')
            ax1_data.append(float(at))
            ax2_data.append(float(h))
            ax3_data.append(float(t))
            y.append(i)
            ax1.clear()
            ax2.clear()
            ax3.clear()
            ax1.plot(ax1_data, y)   
            ax1.plot(ax2_data, y)   
            ax1.plot(ax3_data, y)   
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
