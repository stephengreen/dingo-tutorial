```yaml
data:
  ...
  tokenization:
    token_size: 16
    normalize_position: true
    mask_detectors:
      p_num_masked: [0.6, 0.3, 0.1]
      p_detector:
        H1: 0.3
        L1: 0.3
        V1: 0.4
    mask_frequency_range:
      p_mask: 0.2
      f_min_upper: 100.0
      f_max_lower: 800.0
      p_lower_upper_both: [0.4, 0.4, 0.2]
      p_same_all_detectors: 0.7
    mask_frequency_notches:
      p_per_detector: 0.3
      max_width: 10.0
```
