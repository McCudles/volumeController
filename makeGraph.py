import utils
import matplotlib.pyplot as plt
import controlPoints as ctrlPnts

data = utils.init(ctrlPnts.points)

plt.plot(data[0], data[1])
plt.savefig("figure.png")
