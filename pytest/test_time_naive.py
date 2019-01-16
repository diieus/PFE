import rand
import sys
sys.path.append(sys.path[0] + "/..")
import wrapper.multiple
import unittest
import wrapper.naive
import time

class NaiveTimeTest(unittest.TestCase):

    """Test case used to test the multiple wrapper."""

    def test_designated_exists(self):
        """Test if designated solutions exist with 32 + 1 variables."""

        n = 38
        n_eqs = 38
        random_seed = 1338
        rand.mysrand(random_seed)
        N = 1 + n + n * (n - 1) // 2
        F = [0]
        for i in range (1,N):
            F.append(rand.myrand() & ((1 << n_eqs) - 1))
        X = rand.myrand() & ((1 << n) - 1)

        deb = time.time()
        check_sol = wrapper.naive.naive_evaluation(n, F, X)
        self.assertEqual(wrapper.naive.naive_evaluation(n, F, X),check_sol, "not ok 1 - designated solutions does NOT exist")
        print(f"Time PY : {time.time() - deb}")


        deb = time.time()
        X = X & 0xffffffff
        T = wrapper.multiple.multiple_parser(n, F)

        check_sol = T[0][0]
        T[0][0] = wrapper.wrapper.naive(32, T[0], X)
        self.assertEqual(wrapper.wrapper.naive(32, T[0], X),check_sol, "not ok 2 - designated solutions does NOT exist")
        print(f"Time C : {time.time() - deb}")

#        check_sol = T[1][0]
#        T[1][0] = wrapper.wrapper.naive(32, T[1], X)
#        self.assertEqual(wrapper.wrapper.naive(32, T[1], X),check_sol, "not ok 2 - designated solutions does NOT exist")
