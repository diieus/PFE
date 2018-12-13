### Clean everything ###

cd ../wrapper/
py3clean .
rm -f _*
cd -

cd ../timetests/
py3clean .
rm -f _*
cd -

cd ../pytest/
py3clean .
cd -
