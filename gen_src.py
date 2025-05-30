'''
Generate mock observations of sources

Each source has a certain intrinsic polarisation properties, and each source is further simulated multiple times to take measurement uncertainty into account
'''

import polsim
import numpy as np
import os



## Define a list of sources to simulate
## One randomisation seed will produce one simulation realisation
src_list = [
{"model_sel": 1, 
"pDict": {"fracPol": 0.3, "psi0_deg": 55., "RM_radm2": -250.,}, 
"freq_array": np.arange(800.e6, 1089.e6, 1.e6),
"iDict": {"reffreq": 944.e6, "flux": 2.e-3, "alpha": 0.},
"noise": 20.e-6, 
"seed_list": np.arange(1000, 1003, 1)
},
{"model_sel": 11,
"pDict": {"fracPol1": 0.2, "fracPol2": 0.1, "psi01_deg": 155., "psi02_deg": 30., "RM1_radm2": 400., "RM2_radm2": -250.,},
"freq_array": np.arange(800.e6, 1089.e6, 1.e6),
"iDict": {"reffreq": 944.e6, "flux": 2.e-3, "alpha": 0.},
"noise": 20.e-6,
"seed_list": np.arange(10000, 10003, 1)
},
]



## A dummy variable to give each source a unique "name"
nsrc = 0

for src in src_list:
   ## A dummy variable to give each realisation a unique "name"
   nreal = 0
   for seed in src['seed_list']:
      ## Generate the simulated IQU values
      i_list, q_list, u_list = polsim.iqu_sim(src["model_sel"], src["pDict"], src["freq_array"], src["iDict"], src["noise"], seed)
      ## Create the output files, each source / realisation in one dir.
      os.system('mkdir src'+str(nsrc)+'_real'+str(nreal))
      f = open('src'+str(nsrc)+'_real'+str(nreal)+'/IQU.tsv', 'w')
      for _ in range(len(src["freq_array"])):
         f.write('%.0f' % src["freq_array"][_]+'\t%.8f' % i_list[_]+'\t%.8f' % q_list[_]+'\t%.8f' % u_list[_]+'\t%.8f' % src["noise"]+'\t%.8f' % src["noise"]+'\t%.8f' % src["noise"]+'\n')
      f.close()
      nreal += 1
   nsrc += 1





