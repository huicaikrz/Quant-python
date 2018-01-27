# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:02:46 2018

@author: lenovo
"""

import random
import matplotlib.pyplot as plt
from scipy.stats import norm
#Parameters
n = 100 #names in credit index
rho = 0.5
num_sims = 1000
prob_default = 0.1

#For equity tranche 0-20%, mezzanine 20%-80%
tranche_cutoffs = [0,0.2,1]
tranche_to_watch = 1 #1 is quity, 2 mezz, etc

#derived parameters
z_score_of_default = norm.ppf(prob_default)  #the return when the default happens
beta = rho**0.5
alpha = (1 -rho)**0.5
max_defaults_protected = n*tranche_cutoffs[tranche_to_watch-1]
wiped_out_defaults = n*tranche_cutoffs[tranche_to_watch]
names_in_tranche = wiped_out_defaults-max_defaults_protected
# run simulation
#histogram = [0] * (n+1)
trial_results = []
names_remaining_in_tranche = []
for _ in range(num_sims):
    M = random.gauss(0, 1)
    K = 0 # number of variables that are > 0
    for _ in range(n):
        R_i = beta * M + alpha * random.gauss(0, 1)
        if R_i < z_score_of_default:
            K += 1
    #histogram[K] += 1
    trial_results.append(K)
    remaining_in_tranche = max(0,names_in_tranche - max(0,max_defaults_protected))
    names_remaining_in_tranche.append(remaining_in_tranche)
#print(histogram)
plt.hist(trial_results, bins=n+1, normed=0, align='mid')
plt.title('Distribution of Defaults in ' + str(num_sims) + ' trials')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()