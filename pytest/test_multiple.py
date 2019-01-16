import rand
import sys
sys.path.append(sys.path[0] + "/..")
import wrapper.multiple
import unittest


class MultipleTest(unittest.TestCase):

    """Test case used to test the multiple wrapper."""

    def test_designated_exists(self):
        """Test if designated solutions exist with 32 + 1 variables."""

        n = 35
        n_eqs = 35
        random_seed = 1338
        rand.mysrand(random_seed)
        N = 1 + n + n * (n - 1) // 2
        F = [0]
        for i in range (1,N):
            F.append(rand.myrand() & ((1 << n_eqs) - 1))
        X = rand.myrand() & ((1 << n) - 1)
        X = X & 0xffffffff

        T = wrapper.multiple.multiple_parser(n, F)

        check_sol = T[0][0]
        T[0][0] = wrapper.wrapper.naive(32, T[0], X)
        self.assertEqual(wrapper.wrapper.naive(32, T[0], X),check_sol, "not ok 1 - designated solutions does NOT exist")

        check_sol = T[1][0]
        T[1][0] = wrapper.wrapper.naive(32, T[1], X)
        self.assertEqual(wrapper.wrapper.naive(32, T[1], X),check_sol, "not ok 2 - designated solutions does NOT exist")


    def test_designated_found(self):
        """Test the wrapper on a designated solution."""

        n = 37
        n_eqs = 37
        random_seed = 1338
        rand.mysrand(random_seed)
        N = 1 + n + n * (n - 1) // 2
        F = [0]
        for i in range (1,N):
            F.append(rand.myrand() & ((1 << n_eqs) - 1))
        X = rand.myrand() & ((1 << n) - 1)
        X = X & 0xffffffff

        T = wrapper.multiple.multiple_parser(n, F)

        for i in range(len(T)):
            T[i][0] = wrapper.wrapper.naive(32, T[i], X)

        max_solutions = 256
        solutions = []
        status = False

        n_solutions =  wrapper.multiple.multiple_solve(T, solutions, max_solutions, 0)

        for i in range(n_solutions):
            if (solutions[i] == X):
                status = True
                break

        self.assertTrue(status, "not ok - designated solution not found")


    # def test_number_found(self):
    #     """Test the number of solutions found."""
    #
    #     n = 36
    #     n_eqs = 36
    #     random_seed = 1338
    #     rand.mysrand(random_seed)
    #     N = 1 + n + n * (n - 1) // 2
    #     F = [0]
    #     for i in range (1,N):
    #         F.append(rand.myrand() & ((1 << n_eqs) - 1))
    #     X = rand.myrand() & ((1 << n) - 1)
    #     X = X & 0xffffffff
    #
    #     T = wrapper.multiple.multiple_parser(n, F)
    #
    #     for i in range(len(T)):
    #         T[i][0] = wrapper.wrapper.naive(32, T[i], X)
    #
    #     max_solutions = 256
    #     solutions = []
    #     status = False
    #
    #     n_solutions =  wrapper.multiple.multiple_solve(T, solutions, max_solutions, 0)
    #
    #     self.assertEqual(n_solutions, 2 ** (n - 32), "not ok - the number of solutions is not good")
