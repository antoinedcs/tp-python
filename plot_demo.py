import matplotlib.pyplot as plt

xs = [5,6,7,8,9,10,11,12,13,14]
y1 = [3] * len(xs)
y2 = [5] * len(xs)

plt.plot(xs, y1, 'r*')
plt.plot(xs, y2, 'r*')
plt.title('Deux rangées de points rouges')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
