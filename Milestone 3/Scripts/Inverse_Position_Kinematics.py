import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

q1, q2, q3, q4, L1, L2, L3, L4 = sp.symbols('q1 q2 q3 q4 L1 L2 L3 L4', real=True)

X = L1 * sp.cos(q1) + L2 * sp.cos(q1) * sp.cos(q2) - L3 * sp.sin(q2) * sp.sin(q3) * sp.cos(q1) \
    + L3 * sp.cos(q1) * sp.cos(q2) * sp.cos(q3) + L4 * (-sp.sin(q2) * sp.sin(q3) * sp.cos(q1) + sp.cos(q1) * sp.cos(q2) * sp.cos(q3)) * sp.cos(q4) \
    + L4 * (-sp.sin(q2) * sp.cos(q1) * sp.cos(q3) - sp.sin(q3) * sp.cos(q1) * sp.cos(q2)) * sp.sin(q4)

Y = L1 * sp.sin(q1) + L2 * sp.sin(q1) * sp.cos(q2) - L3 * sp.sin(q1) * sp.sin(q2) * sp.sin(q3) \
    + L3 * sp.sin(q1) * sp.cos(q2) * sp.cos(q3) + L4 * (-sp.sin(q1) * sp.sin(q2) * sp.sin(q3) + sp.sin(q1) * sp.cos(q2) * sp.cos(q3)) * sp.cos(q4) \
    + L4 * (-sp.sin(q1) * sp.sin(q2) * sp.cos(q3) - sp.sin(q1) * sp.sin(q3) * sp.cos(q2)) * sp.sin(q4)

Z = L2 * sp.sin(q2) + L3 * sp.sin(q2) * sp.cos(q3) + L3 * sp.sin(q3) * sp.cos(q2) \
    + L4 * (-sp.sin(q2) * sp.sin(q3) + sp.cos(q2) * sp.cos(q3)) * sp.sin(q4) + L4 * (sp.sin(q2) * sp.cos(q3) + sp.sin(q3) * sp.cos(q2)) * sp.cos(q4)

mu_e = sp.Matrix([X, Y, Z])
J = mu_e.jacobian([q1, q2, q3, q4])

L1_val, L2_val, L3_val, L4_val = 0.219, 0.35, 0.364, 0.126

mu_a = np.array([0.5, 0.5, 0.5])

q = np.array([0, 0, 0, 0], dtype=float)

delta = np.array([10**10, 10**10, 10**10])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

while np.linalg.norm(delta) > 0.01:
    q_vals = {q1: q[0], q2: q[1], q3: q[2], q4: q[3], L1: L1_val, L2: L2_val, L3: L3_val, L4: L4_val}

    mu_e_val = np.array(mu_e.subs(q_vals).evalf(), dtype=float).flatten()
    J_val = np.array(J.subs(q_vals).evalf(), dtype=float)

    delta = mu_a - mu_e_val

    q += np.dot(np.linalg.pinv(J_val), delta)

    x1 = L1_val * np.cos(q[0])
    y1 = L1_val * np.sin(q[0])
    z1 = 0
    x2 = x1 + L2_val * np.cos(q[0]) * np.cos(q[1])
    y2 = y1 + L2_val * np.sin(q[0]) * np.cos(q[1])
    z2 = L2_val * np.sin(q[1])
    x3 = x2 + L3_val * np.cos(q[0]) * np.cos(q[1]) * np.cos(q[2]) - L3_val * np.cos(q[0]) * np.sin(q[1]) * np.sin(q[2])
    y3 = y2 + L3_val * np.sin(q[0]) * np.cos(q[1]) * np.cos(q[2]) - L3_val * np.sin(q[0]) * np.sin(q[1]) * np.sin(q[2])
    z3 = z2 + L3_val * np.sin(q[1]) * np.cos(q[2]) + L3_val * np.cos(q[1]) * np.sin(q[2])
    x4 = x3 + (L4_val * (np.cos(q[0]) * np.cos(q[1]) * np.cos(q[2]) - np.cos(q[0]) * np.sin(q[1]) * np.sin(q[2])) * np.cos(q[3]) \
        + L4_val * (np.cos(q[0]) * np.sin(q[1]) * np.cos(q[2]) + np.cos(q[0]) * np.sin(q[2]) * np.cos(q[1])) * np.sin(q[3]))
    y4 = y3 + (L4_val * (np.sin(q[0]) * np.cos(q[1]) * np.cos(q[2]) - np.sin(q[0]) * np.sin(q[1]) * np.sin(q[2])) * np.cos(q[3]) \
        + L4_val * (np.sin(q[0]) * np.sin(q[1]) * np.cos(q[2]) + np.sin(q[0]) * np.sin(q[2]) * np.cos(q[1])) * np.sin(q[3]))
    z4 = z3 + (L4_val * (np.sin(q[1]) * np.cos(q[2]) + np.cos(q[1]) * np.sin(q[2])) * np.cos(q[3]) + L4_val * (np.cos(q[1]) * np.cos(q[2]) - np.sin(q[1]) * np.sin(q[2])) * np.sin(q[3]))

    ax.clear()
    ax.plot([0, x1, x2, x3, x4], [0, y1, y2, y3, y4], [0, z1, z2, z3, z4], 'b-o')
    ax.plot([mu_a[0]], [mu_a[1]], [mu_a[2]], 'r*', markersize=10)
    ax.plot([0], [0], [0], 'ks', markersize=10)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.pause(0.05)

print(f'Final solution: q1 = {q[0]}, q2 = {q[1]}, q3 = {q[2]}, q4 = {q[3]}')
plt.show()
