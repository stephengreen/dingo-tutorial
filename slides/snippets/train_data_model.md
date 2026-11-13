```yaml
data:
  waveform_dataset_path: training_data/waveform_dataset.hdf5
  train_fraction: 0.95
  domain_update:
    f_min: 20.0
    f_max: 1024.0
  svd_size_update: 200
  detectors:
    - H1
    - L1
  extrinsic_prior:  # Sampled at train time
    dec: default
    ra: default
    geocent_time: bilby.core.prior.Uniform(minimum=-0.10, m…
    psi: default
    luminosity_distance: bilby.core.prior.Uniform(minimum=1…
  ref_time: 1126259462.391
  inference_parameters:
  - chirp_mass
  - mass_ratio
  - chi_1
  - chi_2
  - theta_jn
  - dec
  - ra
  - geocent_time
  - luminosity_distance
  - psi
model:
  posterior_model_type: normalizing_flow
  posterior_kwargs:
    num_flow_steps: 30
    base_transform_kwargs:
      hidden_dim: 1024
      num_transform_blocks: 5
      activation: elu
      dropout_probability: 0.0
      norm: BatchNorm
      num_bins: 8
      base_transform_type: rq-coupling
  embedding_type: resnet
  embedding_kwargs:
    output_dim: 128
    hidden_dims: [1024, 1024, 1024, 1024, 1024, 1024,
                  512, 512, 512, 512, 512, 512,
                  256, 256, 256, 256, 256, 256,
                  128, 128, 128, 128, 128, 128]
    activation: elu
    dropout: 0.0
    norm: BatchNorm
    svd:
      num_training_samples: 50000
      num_validation_samples: 10000
      size: 200
```
