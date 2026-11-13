```yaml
data:
  waveform_dataset_path: training_data/waveform_dataset.hdf5
  train_fraction: 0.95
  domain_update:
    f_min: 20.0
    f_max: 1024.0
  svd_size_update: 200
  detectors: [H1, L1]
  extrinsic_prior:  # Sampled at train time
    dec: default
    ra: default
    geocent_time: bilby.core.prior.Uniform(minimum=-0.10, m…
    psi: default
    luminosity_distance: bilby.core.prior.Uniform(minimum=1…
  ref_time: 1126259462.391
  inference_parameters: [chirp_mass, mass_ratio, chi_1, chi…
                         theta_jn, dec, ra, geocent_time,
                         luminosity_distance, psi]
```
