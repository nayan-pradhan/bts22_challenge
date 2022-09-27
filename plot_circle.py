import matplotlib.pyplot as plt
import get_intersections as intersec
import math


xA, yA, rA = 10, 10, math.sqrt(500)
xB, yB, rB = 30, 5, math.sqrt(725)
xC, yC, rC = 40, 40, math.sqrt(500)

fig, ax = plt.subplots()

A = plt.Circle( (xA, yA), rA, fill = False)
B = plt.Circle( (xB, yB), rB, fill = False)
C = plt.Circle( (xC, yC), rC, fill = False)

ax.set_xlim((-40, 100))
ax.set_ylim((-40, 10))
ax.add_artist(A)
ax.add_artist(B)
ax.add_artist(C)

intersections = intersec.get_intersections(xA, yA, rA, xB, yB, rB)
if intersections is not None:
    x1, y1, x2, y2 = intersections
    plt.plot([x1, x2], [y1, y2], '.', color='r')

intersections = intersec.get_intersections(xA, yA, rA, xC, yC, rC)
if intersections is not None:
    x1, y1, x2, y2 = intersections
    plt.plot([x1, x2], [y1, y2], '.', color='r')

intersections = intersec.get_intersections(xB, yB, rB, xC, yC, rC)
if intersections is not None:
    x1, y1, x2, y2 = intersections
    plt.plot([x1, x2], [y1, y2], '.', color='r')


plt.gca().set_aspect('equal', adjustable='box')
plt.show()