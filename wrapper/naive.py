def idx1(i):
  return int(i * (i + 1) / 2 + 1)

def idx2(i, j):
  #assert(i < j)
  return idx1(j) + 1 + i

def naive_evaluation(n, F, x):
	v = []
	for k in range(n):
		v.append(0xffffffff if (x & 0x0001) else 0x00000000)
		x >>= 1

	y = F[0]

	for idx_0 in range(n):
		v_0 = v[idx_0]
		y ^= F[idx1(idx_0)] & v_0

		for idx_1 in range(idx_0):
			v_1 = v_0 & v[idx_1]
			y ^= F[idx2(idx_1, idx_0)] & v_1
	return y
