from cffi import FFI
ffi = FFI()

from wrapper import solve


def trente_trois(n, F, sols, max_solutions, verbose):
    N = 1 + n + (n * (n - 1)) // 2
    F[0] = F[0] ^ F[1+32+(32*(32-1))//2] # coeff constant
    



def mult_var(n, F, sols, max_solutions, verbose):
    N = 1 + n + (n * (n - 1)) // 2

    print('lala')
