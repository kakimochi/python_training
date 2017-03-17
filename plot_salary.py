import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 40, 40)
y = (1.57*np.log(x) + 4.38) * 1e6

plt.plot(x,y, "o")
plt.grid(True)
# plt.savefig('data.png', dpi=300, orientation='portrait', transparent=False, pad_inches=0.0)

plt.show()
