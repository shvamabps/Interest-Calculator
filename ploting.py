import numpy as np
import random
import matplotlib.pyplot as plt
import time

random.seed(9)
x_data = np.array([-3, -1, 1, 3]).reshape(-1, 1)
y_data = np.array([3, 4.5, 4.5, 5.5]).reshape(-1, 1)


def model(x):
    global m, c
    y = m * x + c
    return y


m = random.uniform(-1, 1)
c = 0
y_init = model(x_data)
fig = plt.figure()
plt.axis([-4, 4, -1, 7])
plt.scatter(x_data, y_data)
plt.plot(x_data, y_init)
plt.draw()
learn_rate = 0.01
iterations = 100
for i in range(iterations):
    plt.clf()
    for i, j in zip(x_data, y_data):
        y = model(i)
        error = j - y
        m += learn_rate * error * i
        c += learn_rate * error

    y_next = model(x_data)
    plt.plot(x_data, y_next)
    plt.scatter(x_data, y_data)

    plt.plot(x_data, y_init)

    plt.pause(0.001)


plt.show()


"""
import time

import numpy as np
import matplotlib.pyplot as plt


def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()


plt.clf()
plt.setp(plt.gca(), autoscale_on=False)

tellme("You will define a triangle, click to begin")

plt.waitforbuttonpress()

while True:
    pts = []
    while len(pts) < 3:
        tellme("Select 3 corners with mouse")
        pts = np.asarray(plt.ginput(3, timeout=-1))
        if len(pts) < 3:
            tellme("Too few points, starting over")
            time.sleep(1)  # Wait a second

    ph = plt.fill(pts[:, 0], pts[:, 1], "r", lw=2)

    tellme("Happy? Key click for yes, mouse click for no")

    if plt.waitforbuttonpress():
        break

    # Get rid of fill
    for p in ph:
        p.remove()


# Define a nice function of distance from individual pts
def f(x, y, pts):
    z = np.zeros_like(x)
    for p in pts:
        z = z + 1 / (np.sqrt((x - p[0]) ** 2 + (y - p[1]) ** 2))
    return 1 / z


X, Y = np.meshgrid(np.linspace(-1, 1, 51), np.linspace(-1, 1, 51))
Z = f(X, Y, pts)

CS = plt.contour(X, Y, Z, 20)

tellme("Use mouse to select contour label locations, middle button to finish")
CL = plt.clabel(CS, manual=True)
tellme("Now do a nested zoom, click to begin")
plt.waitforbuttonpress()

while True:
    tellme("Select two corners of zoom, middle mouse button to finish")
    pts = plt.ginput(2, timeout=-1)
    if len(pts) < 2:
        break
    (x0, y0), (x1, y1) = pts
    xmin, xmax = sorted([x0, x1])
    ymin, ymax = sorted([y0, y1])
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

tellme("All Done!")
plt.show()
"""
