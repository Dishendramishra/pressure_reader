import time
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
x, y = [], []

while True:
    x.append(i)
    y.append(5)
    
    ax.plot(x, y, color='b')
    fig.canvas.draw()
    ax.set_xlim(left=max(0, i-50), right=i+50)
    print("done")
    time.sleep(0.5)
    i += 1