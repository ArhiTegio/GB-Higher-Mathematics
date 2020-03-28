import matplotlib.pyplot as plt
import numpy as np


fig, ax_f = plt.subplots()
#ax_c = ax_f.twinx()

x = np.linspace(10, 30, 100)
k = 1
ax_f.plot(x, np.cos(k * x))
k2 = 0.5
ax_f.plot(x, np.cos(k2 * x))
ax_f.set_xlim(10, 30)

ax_f.set_title('Задание 4.')
#ax_f.set_ylabel('Fahrenheit')
#ax_c.set_ylabel('Celsius')

plt.show()