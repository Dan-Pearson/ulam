#!/usr/bin/python

import numpy as np

def next_term(j,ulam):
	out = -999
	sums_list = np.array([], dtype=np.uint64) # we initialize the list of the sums
	for m in xrange(j):
		A = ulam[m]
		for n in xrange(m):
			if m == n: # this line is unnecessary if the bounds on for loop are right
				continue
			B = ulam[n]
			C = A+B
			if C > ulam[j-1]: # ignore sums less than the j-th term in ulam sequence
				sums_list = np.append(sums_list,C)
	k=j+1 # k is our test value for the next integer in the Ulam sequence
	while 1==1:
		counter = np.count_nonzero(sums_list == k)
		if counter == 1: # k is Ulam number if sum=k appears in sums_list exactly once
			out = k
			break
		else:
			k += 1			
	return out # if returned out=-999, there was an error

	
###########################################################################
#                                                                         #
#                      Ulam Sequence Generator v.1                        #
#                                                                         #
###########################################################################
	
nmax = 500
ulam = np.zeros(nmax, dtype=np.uint64)
ulam[0] = 1
ulam[1] = 2
for j in xrange(2, nmax):
	ulam[j] = next_term(j,ulam)

outfileName = 'ulam_seq_'+str(nmax)+'.txt'
np.savetxt(outfileName, ulam, fmt='%i')