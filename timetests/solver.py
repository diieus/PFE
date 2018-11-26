from cffi import FFI
ffi = FFI()

try:
    from _timeCU import lib
except ImportError:
    import sys
    sys.exit("You forgot to execute 'python3 CFFI.py' or 'source sources' before running. Do it and try again.")


def test():
    lib.main()
#    print(f'found {n_solutions} solutions') #, here they come :')
    #for c in range(n_solutions):
    #    print(f'  {solutions[c]}')


if __name__ == '__main__':
    test()
