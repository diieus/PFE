from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source("_naive",  # name of the output C extension
"""
    #include "naive_eval.c"
""",
    include_dirs=["../libfes-lite/src"],  # specify the dir for the sources
    libraries=['feslite'],    # link with the feslite library
    extra_compile_args=["-w"]) #avoids the warnings


ffibuilder.cdef("""
uint32_t feslite_naive_evaluation(size_t, const uint32_t * const, uint32_t);
""")


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
