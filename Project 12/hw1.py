import matplotlib.pyplot as plt

x = [0.5, 1.5, 1.3, 2.5, 3.1, 3.6, 4.7, 5.1, 5.5, 6.8, 7.5, 8.5, 9.2, 9.8]
y = [2, 2.5, 3, 7, 8.5, 9.2, 4.5, 5.2, 5.9, 3, 2, 8, 9, 7]

plt.scatter(x, y)
plt.xlim(0, 10)

cc = ['blue', 'orange', 'grey', 'green', 'red']
for i in range(len(cc)):
    plt.axvspan(i*2, i*2+2, facecolor=cc[i], alpha=0.2)

plt.show()

# https://matplotlib.org/stable/gallery/color/named_colors.html