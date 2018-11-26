for e in `seq 1 3`; do
	(/usr/bin/time -f'%E' python3 solver.py) >/dev/null 2>> time_results
done

sed -e s/0://g -i time_results
awk '{ total += $1; count++ } END { print total/count }' time_results >> RESULT
rm time_results
