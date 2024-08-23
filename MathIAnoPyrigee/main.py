import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.patches import Circle
from matplotlib.animation import PillowWriter

fig = plt.figure()
loworbit, = plt.plot([], [], 'k-')
transferorbit, = plt.plot([], [], 'k-')
highorbit, = plt.plot([], [], 'k-')
plt.ylim(-5, 5)
plt.xlim(-5, 5)

metadata = dict(title='Hohmann transfer orbit', artist = 'woo')
writer = PillowWriter(fps=15, metadata=metadata)

xlist = []
ylist = []
x1list = []
y1list = []
x2list = []
y2list = []

with writer.saving(fig, "transferorbit.gif", 60):
    for t in np.linspace(0, 6*np.pi, 60):
        a, b = 2, 2  # Semi-major and semi-minor axes lengths for loworbit

        c, d = 3, 1  # Semi-major and semi-minor axes lengths for transferorbit
        transfercenter_x, transfercenter_y = -1, 0 #center coodinates for transferorbit ellipse

        e, f = 4, 4, # Semi-major and semi-minor axes lengths for highorbit

        xlist.append(a*np.cos(t))
        ylist.append(b*np.sin(t))
        x1list.append(transfercenter_x + c*np.cos(t))
        y1list.append(transfercenter_y + d*np.sin(t))
        x2list.append(e*np.cos(t))
        y2list.append(f*np.sin(t))

        loworbit.set_data(xlist, ylist)
        transferorbit.set_data(x1list, y1list)
        highorbit.set_data(x2list, y2list)

        writer.grab_frame()