import matplotlib.pyplot as plt
import numpy as np

y,x = np.ogrid[-5:5:100j,-5:5:100j]

plt.contour(x.ravel(), y.ravel(),x**3-x-y**2,[1])

plt.show()
