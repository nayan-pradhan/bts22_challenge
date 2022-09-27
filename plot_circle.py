import matplotlib.pyplot as plt

xA, yA, rA = 35.4, 23.8, 5
xB, yB, rB = 30.5, 20.4, 5
xC, yC, rC = 32.4, 27.2, 5
fig, ax = plt.subplots()
A = plt.Circle( (xA, yA), rA, fill = False)
B = plt.Circle( (xB, yB), rB, fill = False)
C = plt.Circle( (xC, yC), rC, fill = False)

ax.set_xlim((15, 45))
ax.set_ylim((12, 35))
ax.add_patch(A)
ax.add_patch(B)
ax.add_patch(C)

plt.title('Circle Drawing')
plt.show()