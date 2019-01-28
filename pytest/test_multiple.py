import rand
import sys
sys.path.append(sys.path[0] + "/..")
import wrapper.multiple
import wrapper.naive
import unittest

import time

class MultipleTest(unittest.TestCase):

    """Test case used to test the multiple wrapper."""

    def test_mult_temp(self):
        """Test"""

#        n = 35
#        n_eqs = 35
#        random_seed = 13385474
        n = 35
        n_eqs = 35
        random_seed = 123385474
        rand.mysrand(random_seed)
        N = 1 + n + n * (n - 1) // 2
        F = [0]
        for i in range (1,N):
            F.append(rand.myrand() & ((1 << n_eqs) - 1))
        #X = rand.myrand() & ((1 << n) - 1)

        max_solutions = 256
        solutions = []
        #status = False
        #F[0] = wrapper.naive.naive_evaluation(n, F, X)
        T = wrapper.multiple.multiple_parser(n, F[:])
        n_solutions = wrapper.multiple.multiple_solve(n, T, solutions, max_solutions, 0)
        print(solutions)
        for i in range(n_solutions):
            print(f"sol is {wrapper.naive.naive_evaluation(n, F[:], solutions[i])}")
            #self.assertEqual(wrapper.naive.naive_evaluation(n, F, solutions[i]), 0, "not ok - all the solutions aren't good")
#            if (solutions[i] == X):
#                status = True
#                break


        #self.assertTrue(status, "not ok - expected solution NOT found")



    def test_mult_truc(self):
        """Test"""

#        n = 34
#        n_eqs = 34
#        random_seed = 133854
        n = 36
        n_eqs = 36
        random_seed = 213358544
        rand.mysrand(random_seed)
        N = 1 + n + n * (n - 1) // 2
        F = [0]
        for i in range (1,N):
            F.append(rand.myrand() & ((1 << n_eqs) - 1))
        X = rand.myrand() & ((1 << n) - 1)
        max_solutions = 256
        solutions = []
        status = False
        F[0] = wrapper.naive.naive_evaluation(n, F, X)
        T = wrapper.multiple.multiple_parser(n, F[:])
        deb = time.time()
        n_solutions = wrapper.multiple.multiple_solve(n, T, solutions, max_solutions, 0)
        print(f"Time for solver is {time.time() - deb}")
        print(solutions)
        print(X)
        for i in range(n_solutions):
            #print(f"sol is {wrapper.naive.naive_evaluation(n, F, solutions[i])}")
            #self.assertEqual(wrapper.naive.naive_evaluation(n, F, solutions[i]), 0, "not ok - all the solutions aren't good")
            if (solutions[i] == (X)):
                status = True
                break


        self.assertTrue(status, "not ok - expected solution NOT found")
