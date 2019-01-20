import rand
import sys
sys.path.append(sys.path[0] + "/..")
import wrapper.naive
import unittest


class MultipleTest(unittest.TestCase):

    """Test case used to test the naive solver."""

    def test_naive_simple(self):
        """Test the naive version on a 32 variables 32 equations system."""

        n = 32
        n_eqs = 32
        random_seed = 1338
        rand.mysrand(random_seed)
        N = 1 + n + n * (n - 1) // 2
        F = [0]
        for i in range (1,N):
            F.append(rand.myrand() & ((1 << n_eqs) - 1))
        X = rand.myrand() & ((1 << n) - 1)

        F[0] = wrapper.naive.naive_evaluation(n, F[:], X)
        self.assertEqual(wrapper.naive.naive_evaluation(n, F, X), 0),"not ok - designated solution was not found"


    def test_naive_variables(self):
        """Test the naive version on a 32 + k variables 32 equations system."""

        n = 37
        n_eqs = 32
        random_seed = 1338
        rand.mysrand(random_seed)
        N = 1 + n + n * (n - 1) // 2
        F = [0]
        for i in range (1,N):
            F.append(rand.myrand() & ((1 << n_eqs) - 1))
        X = rand.myrand() & ((1 << n) - 1)

        F[0] = wrapper.naive.naive_evaluation(n, F[:], X)
        self.assertEqual(wrapper.naive.naive_evaluation(n, F, X), 0),"not ok - designated solution was not found"


    def test_naive_equations(self):
        """Test the naive version on a 32 variables 32 + k equations system."""

        n = 32
        n_eqs = 37
        random_seed = 1338
        rand.mysrand(random_seed)
        N = 1 + n + n * (n - 1) // 2
        F = [0]
        for i in range (1,N):
            F.append(rand.myrand() & ((1 << n_eqs) - 1))
        X = rand.myrand() & ((1 << n) - 1)

        F[0] = wrapper.naive.naive_evaluation(n, F[:], X)
        self.assertEqual(wrapper.naive.naive_evaluation(n, F, X), 0),"not ok - designated solution was not found"

    def test_naive_both(self):
        """Test the naive version on a 32 + k variables 32 + k equations system."""

        n = 36
        n_eqs = 36
        random_seed = 1338
        rand.mysrand(random_seed)
        N = 1 + n + n * (n - 1) // 2
        F = [0]
        for i in range (1,N):
            F.append(rand.myrand() & ((1 << n_eqs) - 1))
        X = rand.myrand() & ((1 << n) - 1)

        F[0] = wrapper.naive.naive_evaluation(n, F[:], X)
        self.assertEqual(wrapper.naive.naive_evaluation(n, F, X), 0),"not ok - designated solution was not found"



    def test_naive_comp(self):
        """Test the naive version on a 32 + k variables 32 + k equations system and check is the sol is the same with the limited naive solver."""

        n = 38
        n_eqs = 38
        random_seed = 1338
        rand.mysrand(random_seed)
        N = 1 + n + n * (n - 1) // 2
        F = [0]
        for i in range (1,N):
            F.append(rand.myrand() & ((1 << n_eqs) - 1))
        X = rand.myrand() & ((1 << n) - 1)

        F[0] = wrapper.naive.naive_evaluation(n, F[:], X)
        self.assertEqual(wrapper.naive.naive_limited(n, F, X), 0),"not ok - designated solution was not found"
