import utils
import matplotlib.pyplot as plt
import controlPoints as ctrlPnts

# This file will use some linux-dependent imports,
# you cannot run this using windows' python.exe
data = utils.init(ctrlPnts.points)

plt.plot(data[0], data[1])
plt.savefig("./images/figure.png")
