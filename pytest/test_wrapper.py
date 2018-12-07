import rand
import sys
sys.path.append(sys.path[0] + "/..")
import wrapper.wrapper
import unittest


class WrapperTest(unittest.TestCase):

    """Test case used to test the wrapper."""

    def test_designated(self):
        """Test the wrapper on a designated solution."""

        n = 24
        n_eqs = 24
        random_seed = 1338
        rand.mysrand(random_seed)
        N = 1 + n + n * (n - 1) // 2
        F = [0]
        for i in range (1,N):
            F.append(rand.myrand() & ((1 << n_eqs) - 1))
        X = rand.myrand() & ((1 << n) - 1)

        F[0] = wrapper.wrapper.naive(n, F, X);
        self.assertEqual(wrapper.wrapper.naive(n, F, X),0, "not ok (0) - designated solutions does NOT exist")

        max_solutions = 256
        solutions = []
        status = False

        n_solutions =  wrapper.wrapper.solve(n, F, solutions, max_solutions, 0)
        for i in range(n_solutions):
            if (solutions[i] == X):
                status = True
                break

        self.assertTrue(status, "not ok (1) : expected solution NOT found")
