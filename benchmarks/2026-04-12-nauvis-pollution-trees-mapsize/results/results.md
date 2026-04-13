# Factorio Benchmark Results

**Platform:** linux-x86_64
**Factorio Version:** 2.0.76
**Date:** 2026-04-12

## Scenario
* Each save was tested for 108000 tick(s) and 20 run(s)

## Results
| Metric            | Description                           |
| ----------------- | ------------------------------------- |
| **Mean UPS**      | Updates per second – higher is better |
| **Mean Avg (ms)** | Average frame time – lower is better  |
| **Mean Min (ms)** | Minimum frame time – lower is better  |
| **Mean Max (ms)** | Maximum frame time – lower is better  |

| Save | Avg (ms) | Min (ms) | Max (ms) | UPS | Execution Time (ms) | % Difference from base |
|------|----------|----------|----------|-----|---------------------|------------------------|
| default | 14.107 | 12.421 | 153.825 | 70 | 3047016 | 0.00% |
| del-trees-nauvis-all-surface | 13.386 | 11.838 | 145.974 | 74 | 2891189 | 5.39% |
| del-trees-nauvis-all-surface-pollution-off | 12.194 | 10.523 | 142.676 | **82** | 2633964 | 15.68% |
| del-trees-nauvis-all-surface-pollution-off-del-useless-map | 12.167 | 10.910 | 136.194 | **82** | 2628024 | 15.94% |
| del-trees-nauvis-city-frame-only | 13.825 | 12.177 | 155.130 | 72 | 2986087 | 2.04% |
| del-trees-nauvis-city-frame-only-pollution-off | 12.208 | 10.576 | 151.523 | 81 | 2636986 | 15.55% |
| del-trees-nauvis-pollution-cloud-only | 13.407 | 11.811 | 146.968 | 74 | 2895929 | 5.22% |
| del-trees-nauvis-pollution-cloud-only-pollution-off | 12.213 | 10.651 | 144.052 | 81 | 2638142 | 15.50% |
| pollution-off | 12.197 | 10.649 | 147.779 | 81 | 2634585 | 15.65% |
| pollution-off-del-useless-map | 12.173 | 10.869 | 141.339 | **82** | 2629317 | 15.89% |

## Conclusion