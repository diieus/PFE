from cffi import FFI
ffi = FFI()

try:
    from _aleafes import lib
except ImportError:
    import sys
    sys.exit("You forgot to execute 'python3 CFFI.py' or 'source sources' before running. Do it and try again.")


def test():
    random_seed = 2
    n = 32
    # F is alea_F
    solutions = ffi.new("uint32_t []", [233] * 256)
    max_solutions = 256
    verbose = True
    n_solutions = lib.feslite_solve(n,lib.alea_F(random_seed,n),solutions,max_solutions,verbose)
    print(f'found {n_solutions} solutions') #, here they come :')
    #for c in range(n_solutions):
    #    print(f'  {solutions[c]}')


if __name__ == '__main__':
    test()
