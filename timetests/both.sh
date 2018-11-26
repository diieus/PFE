for randseed in `seq 2 15`; do
  python3 CFFI.py
  ./average.sh
  echo "RES W:"
  cat RESULT
  cd originalCU
  ./average.sh
  echo "RES O:"
  cat RESULT
  cd ..
  cd ../libfes-lite/benchmark/
  sed -e s/"unsigned long random_seed = $(( $randseed - 1 ));"/"unsigned long random_seed = $randseed;"/g -i correct_use.c
  sudo make
  cd -
done
