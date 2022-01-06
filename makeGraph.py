import volumeController
import utils
import matplotlib.pyplot as plt

data = volumeController.dataPlot()

plt.plot(data[0], data[1])
plt.savefig("figure.png")
