
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
draw_circle = plt.Circle( (35.4, 23.8), 0.3, fill = False)
ax.set_xlim((34.8, 36))
ax.set_ylim((23.2, 24.4))
ax.add_patch(draw_circle)

plt.title('Circle Drawing')
plt.show()