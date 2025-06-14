# qufit_test
Test different samplers of RM-Tools QU-fitting


## Preparations before running
(1) Install `qufit_test`
```
cd /path/to/install/
git clone https://github.com/jackieykma/qufit_sampler_test.git
```
(2) Get `polsim.py`
```
cd /path/to/install/qufit_sampler_test/
git clone https://github.com/jackieykma/polsim.git
mv polsim/polsim.py ./
rm -rf polsim
```
(3) Generate mock observations\
\
Edit `gen_src.py`: Put source parameters to within `src_list`. Polarisation parameters follow RM-Tools QU-fitting convention, as follows:
- `model_sel`: QU-fitting model selected
- `pDict`: Dictionary containing the polarisation parameters

Total intensity properties should also be specified within `iDict`:
- `reffreq`: Reference frequency at which `flux` is specified (Hz)
- `flux`: Total intensity at `reffreq` (Jy)
- `alpha`: Spectral index (S = S0 (nu/nu0)^alpha)

Observation parameters are specified by:
- `freq_array`: Array of observing frequency (Hz); note that bandwidth depolarisation is not taken into account
- `noise`: Per-channel noise level for all Stokes parameter (Jy)

Finally, the same simulated source can be mock-observed for multiple times, with everything kept equal except for the noise realisation. This is done by adjusting the `seed_list` list --- one seed should be provided for each realisation



## Running QU-fitting
Multiple runs of QU-fitting are to be performed on the same source to test the stability of the outputs between runs. After installation of `qufit_test` and generationg of the mock observations (as above), one can execute the QU-fitting test via\
`python3 run_qufit.py -n [src_dir_name] -m [qufit_model] -k [nruns] -s [sampler] -p [qufit_path]`\
For this test, probably want to have high nruns (>~ 100), and try different samplers (`dynesty`, `pymultinest`, `nestle`)

As an example, the following command is used as part of the tests shown in the RM-Tools paper (Van Eck et al. in prep.)\
`python3 run_qufit.py -n src0_real0 -m 1 -k 1000 -s pymultinest -p /path/to/RM-Tools/RMtools_1D/do_QUfit_1D_mnest.py`


## Plotting the outputs
The best-fit parameters across different runs are to be plotted. More details will be added here...






