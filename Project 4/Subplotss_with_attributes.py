import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

fig, ax = plt.subplots(2, 3, gridspec_kw={'wspace': 0.5, 'hspace': 0.5})

ax[0, 0].plot(x, y)
ax[0, 1].scatter(x, y)
ax[0, 2].bar(x, y)
ax[1, 0].stem(x, y)
ax[1, 1].step(x, y)
ax[1, 2].pie(y)
plt.show()
