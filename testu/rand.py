next = 1

def myrand_15():
    """
    pseudo-random number in the range 0--32767
    """
    global next
    next = next * 1103515245 + 12345
    return((next//65536) % 32768)

def myrand():
    """
    pseudo-random number in the range 0--2^32 - 1
    """
    return  (myrand_15() << 24) ^ (myrand_15() << 10) ^ myrand_15()


def mysrand(seed):
    global next
    next = seed
