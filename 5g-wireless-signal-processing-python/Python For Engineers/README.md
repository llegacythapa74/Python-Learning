# Python for Engineers

This folder is about practicing core Python concepts using real
wireless engineering problems instead of generic textbook examples.

## Files

### power_functions.py
Practicing the concept that dBm values cannot be added directly.
Convert to Watts first, sum them up, then convert back to dBm.
Classic RF mistake if you skip this step.

### list_comprehension.py
Practicing list comprehension using RF calculations — powers of 2
for digital modulation, wavelengths for common 5G frequencies and
free space path loss at different distances.

### subcarrier_conflict_detection.py
Practicing Python sets using an OFDMA resource allocation problem.
Two users share subcarriers and I used set operations to find conflicts,
total occupied subcarriers and what can be freed up.

### measurement_dataset.py
Simulating 100 SNR/BER measurement samples using dictionaries and lists.
Used min() with a lambda to find the best sample — good practice for
working with real measurement data in wireless testing.

## Why this approach
Wireless engineering involves a lot of data processing and list manipulation.
Learning Python this way makes it easier to connect the language to
real problems I will face on the job.

## Author
Pujan Thapa Magar