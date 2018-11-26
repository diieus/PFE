from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source("_aleafes",
    open("aleaandsolve.c",'r').read(),
    include_dirs=["../libfes-lite/src"],  # specify the dir for the sources
    libraries=['feslite'])    # link with the feslite library


ffibuilder.cdef("""
size_t feslite_solve(size_t, const uint32_t * const, uint32_t *, size_t, bool);
uint32_t * alea_F(unsigned long, size_t);
""")


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
