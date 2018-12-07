# Libfes wrapper README file
## Install
Just run ```./script.sh```

## Run
Go in the wrapper directory (```cd wrapper/```) and run the Python scripts CFFI_feslite.py and CFFI_naive.py with ```python3 CFFI_feslite.py``` and ```python3 CFFI_naive.py``` in order to create the libraries *file.so*

You can now use the main script *wrapper.py* in other Python scripts. For the designated solution, go to the directory *testu* and run it with ```python3 designated.py```

## Clean
To remove libraries and object files, juste run ```./clean.sh```
