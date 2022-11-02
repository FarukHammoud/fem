def _submatrices(K, c):
    # Separates a matrix in submatrices
    n = K.shape[0]

    Kss = K[0:c,0:c]
    Ksl = K[0:c,c:n]
    Kls = K[c:n,0:c]
    Kll = K[c:n,c:n]

    return Kss, Ksl, Kls, Kll
