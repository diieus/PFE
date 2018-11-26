op = open("RESULT",'r')
RE = op.read()
L1 = [float(x) for x in RE.split('\n')[14:29]]
op.close()

op = open("originalCU/RESULT",'r')
RE = op.read()
L2 = [float(x) for x in RE.split('\n')[14:29]]
op.close()

import matplotlib.pyplot as plt

plt.title("Différence temps C / CFFI")
plt.plot(range(0,15),L1,label="CFFI")
plt.plot(range(0,15),L2,label="C original")
plt.legend()
plt.xlabel('Seconde(s) ajoutée(s) (s)')
plt.ylabel('Temps (s)')
plt.show()
