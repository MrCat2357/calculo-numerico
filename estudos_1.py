import matplotlib.pyplot as plt
import numpy as np
import math as mt
t = np.linspace (0,4,1001)
y = np.cos(t)
b = t

plt.plot (t,y,'b--')
plt.plot (b,t,'ro')
plt.xlabel('zulques x')
plt.ylabel('zulques y')
plt.grid()
plt.show()

