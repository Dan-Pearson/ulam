import numpy as np
import matplotlib.pyplot as plt
import timeit

start = timeit.default_timer()

m_max = 11 # should be odd
n_max = m_max**2 # really this is n_max+1
n_list = np.arange(n_max)
m_list = np.sqrt(n_list).astype(int)
k_list = n_list - m_list**2
zero_list = 0*n_list
a_list = np.maximum(zero_list, k_list-m_list)
b_list = np.minimum(k_list, m_list)

odd_m_indices = np.where(m_list % 2 == 1)
even_m_indices = np.where(m_list % 2 == 0)

Ux_odd_m = (m_list[odd_m_indices] + 1) // 2 - a_list[odd_m_indices]
Uy_odd_m = (-m_list[odd_m_indices] + 1) // 2 + b_list[odd_m_indices]
U_odd_m = np.array((Ux_odd_m, Uy_odd_m, n_list[odd_m_indices])).T

Ux_even_m = -m_list[even_m_indices] // 2 + a_list[even_m_indices]
Uy_even_m = m_list[even_m_indices] // 2 - b_list[even_m_indices]
U_even_m = np.array((Ux_even_m, Uy_even_m, n_list[even_m_indices])).T

print(U_odd_m)
print(U_even_m)

stop = timeit.default_timer()
print(stop - start) 

fig, ax = plt.subplots()
print(np.shape(U_odd_m[:,0]))
for i in range(np.size(U_odd_m[:,0])):
    ax.text(U_odd_m[i,0], U_odd_m[i,1], U_odd_m[i,2], va='center', ha='center')
for i in range(np.size(even_m_indices)):
    ax.text(U_even_m[i,0], U_even_m[i,1], U_even_m[i,2], va='center', ha='center')
    
mymax = np.max(Ux_odd_m)+2
ax.set_xlim(-mymax, mymax)
ax.set_ylim(-mymax, mymax)

plt.show()
    
