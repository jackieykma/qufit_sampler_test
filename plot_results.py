'''
Plot the results to compare between runs
'''

import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import json



## "Source list": One per source-reallisation combination
## Include the input parameters!
src_list = {
   'src0_real0': {
      'fracPol': 0.3,
      'psi0_deg': 55.,
      'RM_radm2': -250.,
      },
   #'src1_real2': {
   #   'fracPol1': 0.2,
   #   'fracPol2': 0.1,
   #   'psi01_deg': 155.,
   #   'psi02_deg': 30.,
   #   'RM1_radm2': 400.,
   #   'RM2_radm2': -250.,
   #   },
   }

## Write down while samplers to look through
sampler_list = ['pymultinest', 'nestle', 'dynesty', 'ultranest']


for sampler in sampler_list:
   for src in src_list:
      print('Working on '+src+' for sampler '+sampler+'...')
      f_list = glob.glob(src+'/IQU_m*_*_'+sampler+'.json')
      json_info_list = [] ## Store all json files
      for f in f_list:
         with open(f, mode='r') as read_file:
            json_info_list.append(json.load(read_file))
      for _ in range(len(json_info_list[0]['parNames'])):
         ## Loop through each parameter
         param = json_info_list[0]['parNames'][_]
         print('Working on parameter '+param+'...')
         values_list = []
         errPlus_list = []
         errMinus_list = []
         for i in range(len(json_info_list)):
            ## Look through each QU-fitting run
            values_list.append(json_info_list[i]['values'][_])
            errPlus_list.append(json_info_list[i]['errPlus'][_])
            errMinus_list.append(json_info_list[i]['errMinus'][_])
         ## Plot the results!
         fig, axs = plt.subplot_mosaic([['scatter', 'hist']], figsize=(4, 2.5), sharey=True, width_ratios = (4, 1))
         axs['scatter'].errorbar(range(len(json_info_list)), values_list, yerr=[errMinus_list, errPlus_list], fmt='ko')
         axs['scatter'].set_xlabel('Run Number')
         axs['scatter'].set_ylabel(param)
         axs['hist'].hist(values_list, bins=20, orientation='horizontal', histtype='step', lw=2, color='k')
         axs['hist'].set_xlabel('Count')
         ## Shade both plots
         axs['scatter'].axhspan(src_list[src][param]-np.median(np.array(errMinus_list)), src_list[src][param]+np.median(np.array(errPlus_list)), color='grey')
         axs['scatter'].axhline(src_list[src][param], lw=2, ls=':', color='r')
         axs['hist'].axhspan(src_list[src][param]-np.median(np.array(errMinus_list)), src_list[src][param]+np.median(np.array(errPlus_list)), color='grey')
         axs['hist'].axhline(src_list[src][param], lw=2, ls=':', color='r')
         plt.tight_layout()
         if True:
            ## True --> Show plot in X-window; False --> save figure
            plt.show()
         else:
            if os.path.exists('plots') == False:
               os.system('mkdir plots')
            plt.savefig('plots/'+src+'_'+param+'_'+sampler+'.png')



