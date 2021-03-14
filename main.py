"""
Рисуем графики
"""
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
x = np.arange(-10, 10.01, 0.01)

# plt.plot(x, x**2)

# -----------------------------------------------------------------------------
# plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
# plt.xlabel(r'$x$')
# plt.ylabel(r'$f(x)$')
# plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
# plt.grid(True)

# def testing():
#     """
#     test function
#     :return: None
#     """
#     pass


# _____________________________________________________________________________
# Рисуем график и сохраняем как legend.png
# -----------------------------------------------------------------------------
# plt.figure(figsize=(10, 6))
# plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')
# plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
# plt.plot(x, -x, label=r'$f_3(x)=-x$')
# plt.xlabel(r'$x$', fontsize=14)
# plt.ylabel(r'$f\ (x)$', fontsize=14)
# plt.legend(loc='best', fontsize=10)
# plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\  f_3(x)=-x$', fontsize=14)
# plt.grid(True)
# plt.savefig('legend.png')

# -----------------------------------------------------------------------------
# subplot несколько графиков в одном графическом окне (Subplot.png)
# -----------------------------------------------------------------------------
t = np.arange(-10, 11, 1)
# subplot 1
plt.subplot(221)
plt.plot(x, np.sin(x), 'g')
plt.title(r'$\sin(x)$')
plt.grid(True)

# subplot 2
plt.subplot(222)
plt.plot(x, np.cos(x), 'r')
# plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.axis('equal')
plt.title(r'$\cos(x)$')
plt.grid(True)

# subplot 3
plt.subplot(223)
plt.plot(x, x ** 2, t, t ** 2, 'ro')
plt.title(r'$x^2$')
plt.grid(True)

# subplot 4
sp = plt.subplot(224)
plt.plot(x, x)
sp.spines['left'].set_position('center')
sp.spines['bottom'].set_position('center')
plt.title(r'$x$')

# testing()

plt.savefig('Subplot.png')
plt.show()
