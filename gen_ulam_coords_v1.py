# run using: python3 n_min n_max

import numpy as np
import timeit
import sys


n_min = int(sys.argv[1])
n_max = int(sys.argv[2]) + 1
n_list = np.arange(n_min,n_max)
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

np.save('test1',U_odd_m)
np.save('test2',U_even_m)

