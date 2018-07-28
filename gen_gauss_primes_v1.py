import dionysus as d
import numpy as np
import timeit


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

start = timeit.default_timer()

n_max = 10**3
prime_list = rwh_primes(n_max)
max_prime = np.max(prime_list)
sq_list = np.arange(1,int(np.sqrt(max_prime)))**2
xx,yy = np.meshgrid(sq_list,sq_list)
candidates = xx+yy
indices = np.where(np.isin(candidates,prime_list))
gauss_primes = np.vstack([np.sqrt(xx[indices]).astype(int), np.sqrt(yy[indices]).astype(int)]).T
print(gauss_primes)



stop = timeit.default_timer()
print(stop-start)
