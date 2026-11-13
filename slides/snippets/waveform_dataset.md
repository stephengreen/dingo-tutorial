```yaml
domain:
  type: UniformFrequencyDomain
  f_min: 20.0
  f_max: 1024.0
  delta_f: 0.125
waveform_generator:
  approximant: IMRPhenomXPHM  # SEOBNRv4PHM
  f_ref: 20.0
  spin_conversion_phase: 0.0
intrinsic_prior:
  mass_1: bilby.core.prior.Constraint(minimum=10.0, maximum…
  mass_2: bilby.core.prior.Constraint(minimum=10.0, maximum…
  chirp_mass: bilby.gw.prior.UniformInComponentsChirpMass(m…
  mass_ratio: bilby.gw.prior.UniformInComponentsMassRatio(m…
  phase: default
  chi_1: bilby.gw.prior.AlignedSpin(name='chi_1', a_prior=U…
  chi_2: bilby.gw.prior.AlignedSpin(name='chi_2', a_prior=U…
  theta_jn: default
  luminosity_distance: 100.0  # Mpc
  geocent_time: 0.0  # s
num_samples: 5000000
compression:
  svd:
    size: 200
    num_training_samples: 50000
    num_validation_samples: 10000
  whitening: aLIGO_ZERO_DET_high_P_asd.txt
```
