# Libfes wrapper README file
## Install
Go to the scripts directory  (```cd scripts/```) and run ```./install.sh``` then config the library path with the next commands :

```
sudo ln -s /usr/local/lib/libfeslite.so.0 /usr/lib/libfeslite.so.0
sudo ldconfig
```


## Run
Go to the scripts directory  (```cd scripts/```) and run ```./init.sh``` to init the wrapper

You can now use the main script *wrapper.py* in other Python scripts.


## Tests
Go to the scripts directory  (```cd scripts/```) and run ```./unit_tests.sh```


## Clean
Go to the scripts directory  (```cd scripts/```) and run ```./clean_all.sh```
