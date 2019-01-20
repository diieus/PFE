def idx1(i):
  return int(i * (i + 1) / 2 + 1)

def idx2(i, j):
  return idx1(j) + 1 + i

def naive_evaluation(n, F, x):
    """
    Naive evaluation of a 32 + k variables 32 + k' equations system.
    """
    v = []
    n_eqs = max([(a).bit_length() for a in F])
    for k in range(n):
        v.append(int(hex(-1 + 2 ** n_eqs),16) if (x & 0x0001) else 0x00000000)
        x >>= 1
    y = F[0]
    for idx_0 in range(n):
        v_0 = v[idx_0]
        y ^= F[idx1(idx_0)] & v_0
        for idx_1 in range(idx_0):
            v_1 = v_0 & v[idx_1]
            y ^= F[idx2(idx_1, idx_0)] & v_1
    return y


def naive_limited(n, F, x):
    """
    Naive evaluation of a 32 variables 32 equations system.
    """
    F = [(x & 0xffffffff) for x in F]
    v = []
    for k in range(n):
        v.append(0xffffffff if (x & 0x0001) else 0x00000000)
        x >>= 1

    y = F[0]

    for idx_0 in range(n):
        v_0 = v[idx_0]
        y ^= F[idx1(idx_0)] & v_0

        for idx_1 in range(idx_0):
            v_1 = v_0 & v[idx_1]
            y ^= F[idx2(idx_1, idx_0)] & v_1
    return y
