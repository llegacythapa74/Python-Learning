"""
Water-Filling Power Allocation
==============================

Optimal power distribution across eigenchannels for a MIMO system.

Given channel eigenvalues [4.0, 1.0, 0.25, 0.01] and total power budget P = 4,
this script implements the water-filling algorithm to maximise channel
capacity by pouring more power into stronger channels and turning off
weak ones entirely.

Author: Pujan Thapa Magar

Theory
------
After SVD the MIMO channel decomposes into parallel eigenchannels with
gains λ₁ ≥ λ₂ ≥ … ≥ λₙ. The optimal power allocation is:

    Pᵢ = max(0, μ − 1/λᵢ)

where the water level μ is chosen so that ΣPᵢ = P_total. Channels with
1/λᵢ > μ are too weak to justify any power and are shut off.

Algorithm
---------
1. Sort eigenvalues descending (strongest first).
2. Compute inverse gains 1/λ (bucket depths).
3. Increase the number of active channels k until the water level μ
   is low enough that the next channel would receive no power.
4. Allocate Pᵢ = max(0, μ − 1/λᵢ) and verify the total.
"""

import numpy as np

np.random.seed(42)

# channel eigenvalues (representing channel strengths)
eigen_values = np.array([4.0, 1.0, 0.25, 0.01])

# total available transmit power
total_power = 4

# sorting helps visualize which channels are strongest
sorted_eigen_values = np.sort(eigen_values)[::-1]
inv_eigen_values = 1.0 / sorted_eigen_values

print(f"Sorted eigenvalues: {sorted_eigen_values}")
print(f"Inverse channel gains: {inv_eigen_values}")

# finding the water level μ
# we progressively include channels until the level becomes valid
n = len(sorted_eigen_values)

for k in range(1, n + 1):
    mu = (total_power + np.sum(inv_eigen_values[:k])) / k

    # once μ is below the next inverse gain, we've found the right level
    if k == n or mu <= inv_eigen_values[k]:
        active_channels = k
        break

# allocating power based on the final water level
# channels below the "water line" get zero power
allocated_power = np.maximum(mu - inv_eigen_values, 0)

print(f"\nWater level (μ): {mu:.4f}")
print(f"Active channels: {active_channels}")
print(f"Power allocation: {allocated_power}")
print(f"Total power used: {np.sum(allocated_power):.4f}")