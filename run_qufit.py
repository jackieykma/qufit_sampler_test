'''
Actual running of QU-fitting
Only use the correct model for fitting
'''



import subprocess
import os
import numpy as np
import glob



def run_qufit(srcname, model, nruns, sampler, qufit_path):
   for n in range(nruns):
      while os.path.exists(srcname+'/IQU_m'+str(model)+'_'+str(n)+'_'+sampler+'.json') == False:
         print('Running for source '+srcname+', nrun='+str(n)+'...')
         try:
            subprocess.run(['python3', qufit_path, srcname+'/IQU.tsv', '-m', str(model), '--sampler', sampler, '--ncores', '16', '--nlive', '128'], timeout=1200)
         except subprocess.TimeoutExpired:
            print('Timed out... Retrying...')
      ## Change name to reflect the nruns
      os.system('mv '+srcname+'/IQU_m'+str(model)+'_'+sampler+'.dat '+srcname+'/IQU_m'+str(model)+'_'+str(n)+'_'+sampler+'.dat')
      os.system('mv '+srcname+'/IQU_m'+str(model)+'_'+sampler+'.json '+srcname+'/IQU_m'+str(model)+'_'+str(n)+'_'+sampler+'.json')
      ## Remove some files --- too costly to save!
      os.system('rm -rf '+srcname+'/IQUfig_*_corner.pdf')
      os.system('rm -rf '+srcname+'/IQUfig_*_specfit.pdf')
      os.system('rm -rf '+srcname+'/IQU_m'+str(model)+'_'+sampler)




if __name__ == "__main__":
   import argparse
   parser = argparse.ArgumentParser()
   parser.add_argument(
      "-n",
      dest="srcname",
      help="Source directory name.",
      type=str,
   )
   parser.add_argument(
      "-m",
      dest="model",
      help="QU-fitting model to attempt (e.g. 1, 2, 11...).",
      type=int,
   )
   parser.add_argument(
      "-k",
      dest="nruns",
      help="Number of QU-fitting attempts.",
      type=int,
   )
   parser.add_argument(
      "-s",
      dest="sampler",
      help="Nestled sampling sampler to use.",
      type=str,
   )
   parser.add_argument(
      "-p",
      dest="qufit_path",
      help="QU-fitting full path (.../.../RM-Tools/RMtools_1D/do_QUfit_1D_mnest.py).",
      type=str,
   )
   
   args = parser.parse_args()
   
   run_qufit(args.srcname, args.model, args.nruns, args.sampler, args.qufit_path)

