```yaml
training:
  stage_0:
    epochs: 300
    asd_dataset_path: training_data/asd_dataset_fiducial/as…
    freeze_rb_layer: True
    optimizer:
      type: adam
      lr: 5.0e-5
    scheduler:
      type: cosine
      T_max: 300
    batch_size: 4096
  stage_1:
    epochs: 150
    asd_dataset_path: training_data/asd_dataset/asds_O1.hdf5
    freeze_rb_layer: False
    optimizer:
      type: adam
      lr: 1.0e-5
    scheduler:
      type: cosine
      T_max: 150
    batch_size: 4096
```
