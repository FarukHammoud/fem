import numpy as np

def local_solver(Coord, t, Em, v, p, P, b, tn):
    #**Complete Linear Analysis - Finite Element Method Example, by Clayton Pettit**
    
    # Constitutive Relantionship 
    CStress = (Em/(1 + v))*np.array([[1/(1 - v), v/(1 - v), 0], [v/(1 - v), 1/(1 - v), 0], [0, 0, 1/2]])
    CStrain = (Em/((1 + v)*(1 - 2*v)))*np.array([[1 - v, v, 0], [v, 1 - v, 0], [0, 0, (1 - 2*v)/2]])
    Cc = CStress

    ## Step 1 - Stiffness Matrix

    # Shape function - Quad 
    N1 = lambda xi,eta :(1 - xi)*(1 - eta)/4
    N2 = lambda xi,eta :(1 + xi)*(1 - eta)/4
    N3 = lambda xi,eta :(1 + xi)*(1 + eta)/4
    N4 = lambda xi,eta :(1 - xi)*(1 + eta)/4
    Ni = [N1, N2, N3, N4]

    x = lambda xi, eta: sum(Ni[i](xi,eta)*Coord[i][0] for i in range(4))
    y = lambda xi, eta: sum(Ni[i](xi,eta)*Coord[i][1] for i in range(4))

    # N Matrix 
    Nn_ = np.zeros((2,8)).tolist()

    for i in range(4):
        Nn_[0][2*i] = Ni[i]
        Nn_[1][2*i+1] = Ni[i]
        Nn_[0][2*i+1] = Nn_[1][2*i] = lambda xi, eta: 0

    Nn = lambda xi, eta: [[Nn_[i][j](xi,eta) for j in range(8)] for i in range(2)]

    # Jacobian Matrix - from Mathematica
    J = lambda xi, eta: [[(3*(1 - eta))/4 + 0.75*(1 + eta), 0.125*(1 - xi) + 0.125*(1 + xi)], [(1 - eta)/4 + 0.05*(1 + eta), (1/4)*(-1 - xi) + (3*(1 - xi))/4 + 0.8*(1 + xi)]]
    Jinv = lambda xi, eta: [[((1/4)*(-1 - xi) + (3*(1 - xi))/4 + 0.8*(1 + xi))/(1.875 + 0.05*eta - 0.3*xi), ((1/4)*(-1 + eta) - 0.05*(1 + eta))/(1.875 + 0.05*eta - 0.3*xi)], [(-0.125*(1 - xi) - 0.125*(1 + xi))/(1.875 + 0.05*eta - 0.3*xi), ((3*(1 - eta))/4 + 0.75*(1 + eta))/(1.875 + 0.05*eta - 0.3*xi)]]

    # B Matrix 
    B1 = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 1, 0]]);
    B2 = lambda xi, eta: [[Jinv(xi,eta)[0][0],Jinv(xi,eta)[0][1], 0, 0], [Jinv(xi,eta)[1][0], Jinv(xi,eta)[1][1],0, 0], [0, 0, Jinv(xi,eta)[0][0], Jinv(xi,eta)[0][1]], [0, 0, Jinv(xi,eta)[1][0], Jinv(xi,eta)[1][1]]]
    B3_ = np.zeros((4,8)).tolist();

    D_Ni_xi = lambda eta: [(1/4)*(-1 + eta), (1 - eta)/4, (1 + eta)/4, (1/4)*(-1 - eta)]
    D_Ni_eta = lambda xi: [(1/4)*(-1 + xi), (1/4)*(-1 - xi), (1 + xi)/4, (1 - xi)/4]

    def B3(xi,eta):
        B3_ = np.zeros((4,8)).tolist();
        for k in range(4):
            B3_[0][2*k]  = D_Ni_xi(eta)[k]
            B3_[2][2*k+1] = D_Ni_xi(eta)[k]
            B3_[1][2*k] = D_Ni_eta(xi)[k]
            B3_[3][2*k+1] = D_Ni_eta(xi)[k]
            B3_[0][2*k+1] = B3_[1][2*k+1] = B3_[2][2*k] = B3_[3][2*k] = 0

        return B3_

    B = lambda xi, eta : np.dot(np.dot(B1,B2(xi,eta)),B3(xi, eta));

    # Integration Function 
    IntFunc = lambda xi, eta: (np.dot(np.dot(B(xi, eta).transpose(),Cc),B(xi, eta)))*np.linalg.det(J(xi, eta));

    # Stiffness Matrix 
    xiset = [1/np.sqrt(3), -1/np.sqrt(3)]
    etaset = [1/np.sqrt(3), -1/np.sqrt(3)]
    Kfull = 0
    for i in range(2):
        for j in range(2):
            Kfull += t*IntFunc(xiset[i], etaset[j])

    ## Step 2 - Nodal Forces Vector 

    # Nodal Loads due to Concentrated Loads 
    Fa = P

    # Nodal Loads due to Body Forces 
    pb = p*b
    pbFunc = lambda xi, eta: (np.dot(np.array(Nn(xi, eta)).transpose(),pb))*np.linalg.det(J(xi, eta))
    Fpb = 0
    for i in range(2):
        for j in range(2):
            Fpb += t*pbFunc(xiset[i],etaset[j])

    D_x_eta = lambda xi: 0.125*(1 - xi) + 0.125*(1 + xi)
    D_y_eta = lambda xi: (1/4)*(-1 - xi) + (3*(1 - xi))/4 + 0.8*(1 + xi)

    # Nodal Loads due to Traction Vectors 
    dl = np.sqrt(D_x_eta(1)**2 + D_y_eta(1)**2)
    tnFunc = lambda xi, eta: np.dot(np.array(Nn(xi, eta)).transpose(),tn)*dl
    Ftn = 2*tnFunc(1,0);

    # Nodal Force Vector 
    Fn = Fa + Fpb + Ftn

    ## Step 3 - Solve the Sytem for Nodal Displacements 

    # Account for Boundary Conditions 

    Kglobal = np.delete(np.delete(Kfull,slice(0,4),0),slice(0,4),1)
    Fglobal = np.delete(Fn,slice(0,4))

    # Solve the Linear System 
    NDisp = np.linalg.solve(Kglobal,Fglobal)

    # Nodal Displacement Vector 
    NodalDisp = np.insert(NDisp, 0,[0,0,0,0],axis=0)

    # Reaction Forces 
    NodalForces = np.dot(Kfull,NodalDisp)
    ReactionForces = NodalForces - Fn
    ReactionForces[np.abs(ReactionForces) < 10**(-10)] = 0

    ## Step 4 - Displacement/Strain/Stress Inside of the Element 

    # Displacement Inside of the element 
    ElementDisp = lambda xi,eta: np.dot(Nn(xi,eta),NodalDisp);

    # Strain Inside of the element 
    Strain = lambda xi,eta: np.dot(B(xi,eta),NodalDisp)

    # Stresses Inside of the Element 
    Stress = lambda xi,eta: np.dot(Cc,Strain(xi, eta))

    # Strain at Integration Points 
    Strain1 = Strain(-1/np.sqrt(3), 1/np.sqrt(3))
    Strain2 = Strain(-1/np.sqrt(3), -1/np.sqrt(3))
    Strain3 = Strain(1/np.sqrt(3), 1/np.sqrt(3))
    Strain4 = Strain(1/np.sqrt(3), -1/np.sqrt(3))
    StrainE11 = np.array([Strain1[0], Strain2[0], Strain3[0], Strain4[0]])
    StrainE22 = np.array([Strain1[1], Strain2[1], Strain3[1], Strain4[1]])
    StrainE12 = np.array([Strain1[2], Strain2[2], Strain3[2], Strain4[2]])

    # Stress Field 
    Stress1 = Stress(-1/np.sqrt(3), 1/np.sqrt(3))
    Stress2 = Stress(-1/np.sqrt(3), -1/np.sqrt(3))
    Stress3 = Stress(1/np.sqrt(3), 1/np.sqrt(3))
    Stress4 = Stress(1/np.sqrt(3), -1/np.sqrt(3))
    StressS11 = np.array([Stress1[0], Stress2[0], Stress3[0], Stress4[0]])
    StressS22 = np.array([Stress1[1], Stress2[1], Stress3[1], Stress4[1]])
    StressS12 = np.array([Stress1[2], Stress2[2], Stress3[2], Stress4[2]])

    ## Step 5 - Display Results

    with np.printoptions(precision=3, suppress=True):
        print("Results:")
        print("Element Stiffness Matrix:")
        print(Kfull)
        print("")
        print("Nodal Force Vector:")
        print(Fn)
        print("")
        print("Nodal Displacements:")
        print(NodalDisp)
        print("")
        print("Reaction Forces:")
        print(ReactionForces)
        print("")
        print("Strain at Integration Points:")
        print("Strain E11 at Integration Points =:", StrainE11)
        print("Strain E22 at Integration Points =:", StrainE22)
        print("Strain E12 at Integration Points =:", StrainE12)
        print("")
        print("Stresses at Integration Points:")
        print("Stress S11 at Integration Points =:", StressS11)
        print("Stress S22 at Integration Points =:", StressS22)
        print("Stress S12 at Integration Points =:", StressS12)
        print("")
    
    return Kfull