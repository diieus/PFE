import rand
import sys
sys.path.append(sys.path[0] + "/..")
import wrapper.wrapper

def main():
    n = 24
    n_eqs = 24
    random_seed = 1338

    #/*************** setup *****************/
    print(f"# initalizing random system with seed={random_seed}")

    rand.mysrand(random_seed)
    N = 1 + n + n * (n - 1) // 2
    F = [0]
    for i in range (1,N):
        F.append(rand.myrand() & ((1 << n_eqs) - 1))
    X = rand.myrand() & ((1 << n) - 1)


    F[0] = wrapper.wrapper.naive(n, F, X);

    if wrapper.wrapper.naive(n, F, X) == 0:
        print("ok 1 - designated solutions exists");
    else:
        print("not ok 1 - designated solutions does NOT exist");

    print(f"# F[{X}] = 0")

    max_solutions = 256
    solutions = []

    #/******************** go *******************/
    status = False

    n_solutions =  wrapper.wrapper.solve(n, F, solutions, max_solutions, 0)
    for i in range(n_solutions):
        print(f"# reporting solution {solutions[i]}")
        if (solutions[i] == X):
            status = True
            break


    if status:
        print("ok : expected solution found")
    else:
        print("not ok : expected solution NOT found")

    return 0


if __name__ == "__main__":
    main()
