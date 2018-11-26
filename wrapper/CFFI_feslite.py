from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source("_wrapper",  # name of the output C extension
"""
    #include "feslite.c"
""",
    include_dirs=["../libfes-lite/src"],  # specify the dir for the sources
    libraries=['feslite'])    # link with the feslite library


ffibuilder.cdef("""
size_t feslite_solve(size_t, const uint32_t * const, uint32_t *, size_t, bool);
""")


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
