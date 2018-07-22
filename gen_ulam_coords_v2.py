# run using: python3 iteration step_size

import numpy as np
import timeit
import sys

iteration = int(sys.argv[1])
step_size = int(sys.argv[2])
n_min = (iteration-1)*step_size
n_max = iteration*step_size
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

U_all = np.vstack((U_odd_m, U_even_m))
U_all = U_all[U_all[:,2].argsort()]

output_name = 'output' + str(iteration) + '.npy'
np.save(output_name,U_all)
