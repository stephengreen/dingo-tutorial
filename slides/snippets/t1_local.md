```yaml
local:
  device: cuda
  num_gpus: 8
  num_workers: 64
  runtime_limits:
    max_time_per_run: 1_000_000
    max_epochs_per_run: 500
  checkpoint_epochs: 25
  local_cache_path: /tmp
```
