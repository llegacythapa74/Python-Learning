"""
Power Combination in dBm
Author: Pujan Thapa Magar

Practicing the concept that you cannot add dBm values directly.
Convert to Watts first, sum them up, then convert back to dBm.
Classic RF mistake if you skip this step.
"""

import math

def combine_power_dbm(dbm_values):
    results = []
    for i in dbm_values:
        linear = 10 ** (i / 10) * 0.001
        results.append(linear)
    total_watts = sum(results)
    total_dbm = 10 * math.log10(total_watts / 0.001)
    return total_dbm

# test: two 20 dBm signals combined should give ~23 dBm
print(f"Combined power: {combine_power_dbm([20, 20]):.2f} dBm")