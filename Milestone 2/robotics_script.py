import sympy as sp

def sysCall_init()
    sim = require('sim')
    self.objectHandle = sim.getObject(..5)
    self.target_position = 0(3.14180)
    self.required_duration = 5
    #sim.setJointPosition(objectHandle, target_position)

def sysCall_actuation()
    curr_time = sim.getSimulationTime()
    if curr_time  self.required_duration
        newPosition = (curr_timeself.required_duration)  self.target_position
        sim.setJointTargetPosition(self.objectHandle, newPosition)
    else
        sim.setJointTargetPosition(self.objectHandle, self.target_position)
        
    pass

def sysCall_cleanup()
    EEPosition = sim.getObjectPosition(sim.getObject(Empty_Link7_respondable),sim.getObject(..Empty_Link1_visual))
    print(EEPosition)
    
    theta = sp.symbols('q1 q2 q3 q4')  
    
    T1 = transformation_func(30(3.14180), 0.2193  sp.sin(45(3.14180)), 0.2193  sp.cos(45(3.14180)), sp.pi2)
    
    T2 = transformation_func(25(3.14180), 0, 0.35, 0)
    
    T3 = transformation_func(45(3.14180), 0, 0.3638, 0)
    
    T4 = transformation_func(0, 0, 0.12633, 0)
    matrix = []
    
    matrix.append(T1)
    matrix.append(T2)
    matrix.append(T3)
    matrix.append(T4)
    final_matrix = matrix[0]  matrix[1]  matrix[2]  matrix[3]
    print(Final Matrix)
    for i in range(final_matrix.rows)
        print(fRow {i+1} {final_matrix.row(i)})
    
    for i, m in enumerate(matrix)
        print(fT{i+1}n{m}n)
    pass

def transformation_func(theta, d, a, alpha)

    
    T = sp.Matrix([[sp.cos(theta), -sp.sin(theta)sp.cos(alpha), sp.sin(theta)sp.sin(alpha), asp.cos(theta)],
                   [sp.sin(theta),  sp.cos(theta)sp.cos(alpha), -sp.cos(theta)sp.sin(alpha), asp.sin(theta)],
                   [0,              sp.sin(alpha),               sp.cos(alpha),               d],
                   [0,              0,                           0,                           1]])

    return T


# See the user manual or the available code snippets for additional callback functions and details
