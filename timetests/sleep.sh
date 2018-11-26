cp -f ../libfes-lite/benchmark/correct_use.c orig_correct_use.c
cp -f sleep_correct_use.c ../libfes-lite/benchmark/correct_use.c
for randseed in `seq 1 15`; do
  python3 CFFI.py
  echo "Step $randseed/15"
  ./average.sh
  cd originalCU
  echo "Step $randseed/15"
  ./average.sh
  cd ..
  cd ../libfes-lite/benchmark/
  sed -e s/"sleep($(( $randseed - 1 )));"/"sleep($randseed);"/g -i correct_use.c
  sudo make
  cd -
done
cp -f orig_correct_use.c ../libfes-lite/benchmark/correct_use.c
