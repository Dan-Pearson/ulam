import dionysus as d
import numpy as np


def rwh_primes(n):
    correction = (n % 6 > 1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n//3)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[((k*k)//3)::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
    return np.array([2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]])


n_max = 10**3
n_list = rwh_primes(n_max)
print(n_max)
m_list = np.sqrt(n_list).astype(int)
k_list = n_list - m_list**2
zero_list = 0*n_list
a_list = np.maximum(zero_list, k_list-m_list)
b_list = np.minimum(k_list, m_list)

odd_m_indices = np.where(m_list % 2 == 1)
even_m_indices = np.where(m_list % 2 == 0)

Ux_odd_m = (m_list[odd_m_indices] + 1) // 2 - a_list[odd_m_indices]
Uy_odd_m = (-m_list[odd_m_indices] + 1) // 2 + b_list[odd_m_indices]
U_odd_m = np.array((Ux_odd_m, Uy_odd_m)).T#, n_list[odd_m_indices])).T

Ux_even_m = -m_list[even_m_indices] // 2 + a_list[even_m_indices]
Uy_even_m = m_list[even_m_indices] // 2 - b_list[even_m_indices]
U_even_m = np.array((Ux_even_m, Uy_even_m)).T#, n_list[even_m_indices])).T

U_all = np.vstack((U_odd_m, U_even_m)).astype(float)

f = d.fill_rips(U_all, 2, 20.)
p = d.homology_persistence(f)
dgms = d.init_diagrams(p, f)

d.plot.plot_diagram_density(dgms[1], show = True)

