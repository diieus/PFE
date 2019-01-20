from cffi import FFI
ffi = FFI()
import wrapper.naive
from ._wrapper import lib as wlib

def suite(n):
    """
    Gives the position of the x_n variable.
    """
    return (1 + n + (n * (n - 1)) // 2)

def shift(F, N):
    """
    Makes a right N shift on the elements of F.
    """
    TF = []
    for i in range(len(F)):
        TF.append((F[i] >> N) & 0xffffffff)
    return TF

def half_split(n, F, a, b):
    """
    Splits a system in two subsystems.
    """
    stack = []
    c = suite(n)
    stack.append((F[:c], a))
    F[0] = F[0] ^ F[c]
    for i in [suite(x) for x in range(n)]:
        c += 1
        F[i] = F[i] ^ F[c]
    stack.append((F[:c], b))
    return stack


def multiple_parser(n, F):
    """
    Parses a 32 + k variables system into a list of 2 ** k "32 variables" subsystems.
    """
    #If n <= 32, simply return F
    if n < 33:
        return [(F,0)]

    stack = []
    temp = []

    #First split
    n_temp = n - 1
    stack += half_split(n_temp, F[:], 0, 1)

    #All the other splits
    while(n_temp > 32):
        n_temp -= 1
        temp = stack
        stack = []
        for e in temp:
            stack += half_split(n_temp, e[0], e[1], e[1] + (1 << n - 1 - n_temp))
    return stack


def multiple_solve(n, T, sols, max_solutions, verbose):
    """
    Solves 32 + k variables 32 + k' equations system.
    """
    solutions = ffi.new("uint32_t []", [42] * max_solutions)
    n_eqs = max([max([a.bit_length() for a in B[0]]) for B in T])
    for e in T:
        SOLS = []
        for i in range(0, 1 + n_eqs - 32):
            n_solutions = wlib.feslite_solve(32, shift(e[0],i), solutions, max_solutions, verbose)
            SOLS.append(solutions[0:n_solutions])
        if SOLS != []:
            inter = SOLS[0]
            for s in SOLS:
                inter = set(s).intersection(inter)
            #print(f"wo shift : {[x for x in list(inter)]}")
            sols += [x + (e[1] << 32) for x in list(inter)] # ??? shift not good...
            #print(f"sols add when e[1] is {e[1]}")

    return len(sols)
