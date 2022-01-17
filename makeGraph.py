import utils
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import controlPoints as ctrlPnts
import numpy as np

data = utils.init(ctrlPnts.points)
xmax = ctrlPnts.points[len(ctrlPnts.points) - 1][0]
ymax = 100

fig, ax = plt.subplots()
ax.set_xticks([0, 150, 180, 210], labels=["Start", "2:30", "3:00", "End"])
ax.set_xlabel("Time", fontsize=20, color="red")
ax.set_yticks([0, 25, 50, 75, 100], labels=["0%", "25%", "50%", "75%", "100%"])
ax.set_ylabel("Volume in Percent")
# setting the color for each zone
plt.axvspan(0, 150, color="green", alpha=0.5)
plt.axvspan(150, 180, color="yellow", alpha=0.5)
plt.axvspan(180, 210, color="red", alpha=0.5)
# setting a grid for the background
plt.grid(
    visible=True,
    which="major",
    axis="x",
    color="black",
    linestyle="-",
    linewidth=1,
)
# setting title
plt.title("9Round Round Volume Progression")
plt.title
# making the domain and range
plt.xlim([0, xmax])
plt.ylim([0, ymax])
# plotting points and saving to figure.png
plt.plot(data[0], data[1])
plt.savefig("./images/figure.png")
