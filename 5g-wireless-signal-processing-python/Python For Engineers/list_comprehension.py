"""
List Comprehension in Wireless Engineering
Author: Pujan Thapa Magar

Practicing list comprehension using real wireless engineering
calculations — powers of 2, wavelengths and free space path loss.
"""

import math

# a) First 20 powers of 2
powers = [2**i for i in range(20)]
print(powers)


# b) Wavelengths for common 5G/LTE frequencies
frequencies = [900e6, 1.8e9, 2.4e9, 3.5e9, 28e9]
speed_of_light = 3e8
wavelengths = [speed_of_light/i for i in frequencies]
print([f"{w:.2f}" for w in wavelengths])


# c) FSPL at 3.5GHz for different distances
frq = 3.5e9
c = 3e8
distances = [10, 50, 100, 200, 500, 1000]
FSPL = []
for index, d in enumerate(distances):
    FSPLs = 20*math.log10(d) + 20*math.log10(frq) + 20*math.log10(4*math.pi/c)
    FSPL.append(FSPLs)
for j in range(len(FSPL)):
    print(f"FSPL at distance [{distances[j]}] m = {FSPL[j]:.2f} dB")