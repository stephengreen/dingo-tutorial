```yaml
local:
  device: cuda
  num_workers: 32
  runtime_limits:
    max_time_per_run: 3600000
    max_epochs_per_run: 500
  checkpoint_epochs: 50
  leave_waveforms_on_disk: True
  condor:
    num_cpus: 32
    memory_cpus: 128000
    memory_gpus: 8000
    request_disk: 50GB
```
