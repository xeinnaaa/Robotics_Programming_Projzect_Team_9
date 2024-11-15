import sympy as sp
def sysCall_init():
    sim = require('sim')
    target_angles = [0.7853981634623128, 0.4694267109022231, 0.7177715600613838, -2.1777474986063883]
    # Define handles and target positions for each joint
    self.objects = [
        {"handle": sim.getObject("../2"), "target_position": target_angles[0]},
        {"handle": sim.getObject("../3"), "target_position": target_angles[1]},
        {"handle": sim.getObject("../4"), "target_position": target_angles[2]},
        {"handle": sim.getObject("../5"), "target_position": target_angles[3]}
    ]
    
    self.required_duration = 1  # Duration for each rotation

def sysCall_actuation():
    curr_time = sim.getSimulationTime()

    # Update each object's position based on the current time
    for obj in self.objects:
        handle = obj["handle"]
        target_position = obj["target_position"]

        if curr_time < self.required_duration:
            # Interpolate position based on time
            new_position = (curr_time / self.required_duration) * target_position
            sim.setJointTargetPosition(handle, new_position)
        else:
            # Set to target position once duration is complete
            sim.setJointTargetPosition(handle, target_position)

def sysCall_cleanup():
    EEPosition = sim.getObjectPosition(sim.getObject("/EndEffector"),sim.getObject("../BaseFrame"))
    print(EEPosition)
    print(sim.getJointPosition(sim.getObject("../5")))
    '''
    theta = sp.symbols('q1 q2 q3 q4')  
    
    T1 = transformation_func(theta[0],0, sp.symbols('L1'), sp.pi/2)
    
    T2 = transformation_func(theta[1], 0, sp.symbols('L2'), 0)
    
    T3 = transformation_func(theta[2], 0, sp.symbols('L3'), 0)
    
    T4 = transformation_func(theta[3], 0, sp.symbols('L4'), 0)
    matrix = []
    
    matrix.append(T1)
    matrix.append(T2)
    matrix.append(T3)
    matrix.append(T4)
    final_matrix = matrix[0] * matrix[1] * matrix[2] * matrix[3]
    
    print("Final Matrix:")
    for i in range(final_matrix.rows):
        print(f"Row {i+1}: {final_matrix.row(i)}")
    
    for i, m in enumerate(matrix):
        print(f"T{i+1}:\n{m}\n")
    
    
    '''

    L1, L2, L3, L4 = [0.219,0.35, 0.364, 0.126]
    T1 = transformation_func(0.7854, 0, L1, sp.pi/2)
    
    T2 = transformation_func(0.4694267109022231, 0, L2, 0)
    
    T3 = transformation_func(0.7177715600613838, 0, L3, 0)
    
    T4 = transformation_func(-2.1777474986063883, 0, L4, 0)
    matrix = []
    
    matrix.append(T1)
    matrix.append(T2)
    matrix.append(T3)
    matrix.append(T4)
    final_matrix = matrix[0] * matrix[1] * matrix[2] * matrix[3]
    
    print("Final Matrix:")
    for i in range(final_matrix.rows):
        print(f"Row {i+1}: {final_matrix.row(i)}")
    
    for i, m in enumerate(matrix):
        print(f"T{i+1}:\n{m}\n")
    
    '''
    batee5 = sp.symbols('X Y Z')
    q1, q3 = inverse_position_kinematics(-0.0770658314629956, -0.0646194449152991, 0.284051314247094, 0.35, 0.364, 0.126305)
    print(q1)
    print(q3)
    '''
    
    
    pass

def transformation_func(theta, d, a, alpha):

    
    T = sp.Matrix([[sp.cos(theta), -sp.sin(theta)*sp.cos(alpha), sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
                   [sp.sin(theta),  sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
                   [0,              sp.sin(alpha),               sp.cos(alpha),               d],
                   [0,              0,                           0,                           1]])

    return T

def inverse_position_kinematics(X,Y,Z, L2, L3, L4):
    R = sp.sqrt(Z**2 + Y**2) - L4 
    q1 = sp.atan2(Y,X)
    #q2 = sp.atan2(Y2, X2) + (sp.acos((L3**2 - X2**2-Y2**2 - L2**2) / 2*((sp.sqrt(X2**2 + Y2**2))*L2)))
    q3 = sp.acos((-(R**2) + L2**2 + L3**2) / (2*L2*L3))
    return q1, q3
    
# See the user manual or the available code snippets for additional callback functions and details
