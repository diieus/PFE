from cffi import FFI
ffi = FFI()

from ._wrapper import lib as wlib

def solve(n, F, sols, max_solutions, verbose):
    solutions = ffi.new("uint32_t []", [42] * max_solutions)
    n_solutions = wlib.feslite_solve(n, F, solutions, max_solutions, verbose)
    for i in range(n_solutions):
        sols.append(solutions[i])
    return n_solutions

from ._naive import lib as nlib


def naive(n, F, X):
    return nlib.feslite_naive_evaluation(n, F, X)
