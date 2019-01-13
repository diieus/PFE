from cffi import FFI
ffi = FFI()

from ._wrapper import lib as wlib

def suite(n):
    return (1 + n + (n * (n - 1)) // 2)

def shift(F):
    TF = []
    for i in range(len(F)):
        TF.append(F[i] & 0xffffffff)
    return TF

def trente_trois(n, F):
    T = []
    T.append(shift(F[:suite(32)]))

    c = suite(32)
    F[0] = F[0] ^ F[c] # coeff constant
    for i in [suite(x) for x in range(32)]:
        c += 1
        F[i] = F[i] ^ F[c]
    T.append(shift(F[:suite(32)]))

    return T

def multiple_parser(n, F):
    if n < 33:
        return [F]
    stack = []
    n_temp = n - 1

    c = suite(n_temp)
    stack.append(F[:c])
    F[0] = F[0] ^ F[c] # coeff constant
    for i in [suite(x) for x in range(n_temp)]:
        c += 1
        F[i] = F[i] ^ F[c]
    stack.append(F[:c])

    temp = []
    while(n_temp > 32):
        n_temp -= 1
        temp = stack
        stack = []
        for e in temp:
            c = suite(n_temp)
            stack.append(e[:c])
            e[0] = e[0] ^ e[c]
            for i in [suite(x) for x in range(n_temp)]:
                c += 1
                e[i] = e[i] ^ e[c]
            stack.append(e[:c])

    return [shift(x) for x in stack]


def multiple_solve(T, sols, max_solutions, verbose):
    solutions = ffi.new("uint32_t []", [42] * max_solutions)
    n_solutions = 0
    N_sols = 0
    for e in T:
        n_solutions = wlib.feslite_solve(32, e, solutions, max_solutions, verbose)
        for i in range(n_solutions):
            sols.append(solutions[i])
        N_sols += n_solutions

    return N_sols
