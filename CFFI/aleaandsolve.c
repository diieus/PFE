#include "../libfes-lite/src/feslite.c"


uint32_t * alea_F(unsigned long random_seed,size_t n)
{
  srand48(random_seed);
  size_t n_eqs = 28;
  const size_t N = (n/2) * (n + 1) + 1;
  uint32_t *F = calloc(N, sizeof(*F));
  for (size_t i = 0; i < N; i++)
  {
    F[i] = lrand48() & ((1ll << n_eqs) - 1);
  }
  return F;
}
