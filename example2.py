import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 500)
y = numpy.random.normal(150, 40, 500) / x

plt.scatter(x, y)
plt.show()