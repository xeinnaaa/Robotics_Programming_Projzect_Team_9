import sympy as sp
import numpy as np

q1, q2, q3, q4 = sp.symbols('q1 q2 q3 q4')
L1, L2, L3, L4 = sp.symbols('L1 L2 L3 L4')

X = (L1 * sp.cos(q1) +
     L2 * sp.cos(q1) * sp.cos(q2) -
     L3 * sp.sin(q2) * sp.sin(q3) * sp.cos(q1) +
     L3 * sp.cos(q1) * sp.cos(q2) * sp.cos(q3) +
     L4 * (-sp.sin(q2) * sp.sin(q3) * sp.cos(q1) + sp.cos(q1) * sp.cos(q2) * sp.cos(q3)) * sp.cos(q4) +
     L4 * (-sp.sin(q2) * sp.cos(q1) * sp.cos(q3) - sp.sin(q3) * sp.cos(q1) * sp.cos(q2)) * sp.sin(q4))

Y = (L1 * sp.sin(q1) +
     L2 * sp.sin(q1) * sp.cos(q2) -
     L3 * sp.sin(q1) * sp.sin(q2) * sp.sin(q3) +
     L3 * sp.sin(q1) * sp.cos(q2) * sp.cos(q3) +
     L4 * (-sp.sin(q1) * sp.sin(q2) * sp.sin(q3) + sp.sin(q1) * sp.cos(q2) * sp.cos(q3)) * sp.cos(q4) +
     L4 * (-sp.sin(q1) * sp.sin(q2) * sp.cos(q3) - sp.sin(q1) * sp.sin(q3) * sp.cos(q2)) * sp.sin(q4))

Z = (L2 * sp.sin(q2) +
     L3 * sp.sin(q2) * sp.cos(q3) +
     L3 * sp.sin(q3) * sp.cos(q2) +
     L4 * (-sp.sin(q2) * sp.sin(q3) + sp.cos(q2) * sp.cos(q3)) * sp.sin(q4) +
     L4 * (sp.sin(q2) * sp.cos(q3) + sp.sin(q3) * sp.cos(q2)) * sp.cos(q4))

joint_angles = [q1, q2, q3, q4]

J = sp.Matrix([
    [sp.diff(X, q1), sp.diff(X, q2), sp.diff(X, q3), sp.diff(X, q4)],
    [sp.diff(Y, q1), sp.diff(Y, q2), sp.diff(Y, q3), sp.diff(Y, q4)],
    [sp.diff(Z, q1), sp.diff(Z, q2), sp.diff(Z, q3), sp.diff(Z, q4)]
])

print("Jacobian matrix, J:")
sp.pprint(J)

values = {
    q1: np.deg2rad(30), 
    q2: np.deg2rad(45),
    q3: np.deg2rad(60),
    q4: np.deg2rad(90),
    L1: 1,              
    L2: 1,
    L3: 1,
    L4: 1
}
dq1, dq2, dq3, dq4 = sp.symbols('dq1 dq2 dq3 dq4')

joint_velocities_symbolic = sp.Matrix([dq1, dq2, dq3, dq4])

random_joint_velocities = {
    dq1: 1,
    dq2: 1,
    dq3: 1,
    dq4: 1
}

J_numeric = J.subs(values)

end_effector_velocity_numeric = J_numeric * joint_velocities_symbolic

end_effector_velocity_result = end_effector_velocity_numeric.subs(random_joint_velocities)

print("\nEnd-effector velocity [dX, dY, dZ] with randomized joint velocities:")
sp.pprint(end_effector_velocity_result)



if J_numeric.shape[0] == J_numeric.shape[1]:  
    J_inv = J_numeric.inv()
    joint_velocities = J_inv * end_effector_velocity_result
    
else:
    J_pseudo_inv = J_numeric.pinv()
  
    joint_velocities = J_pseudo_inv * end_effector_velocity_result

end_effector_velocity_symbolic = J_numeric * joint_velocities_symbolic
end_effector_velocity_result_direct = end_effector_velocity_symbolic.subs(random_joint_velocities)

print("\nRecomputed joint velocities after inverse kinematics calculation (may differ due to numerical rounding):")
sp.pprint(joint_velocities)