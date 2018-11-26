from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source("_timeCU",
    open("../libfes-lite/benchmark/correct_use.c",'r').read(),
    include_dirs=["../libfes-lite/src"],  # specify the dir for the sources
    libraries=['feslite'])    # link with the feslite library


ffibuilder.cdef("""
int main();
""")


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
