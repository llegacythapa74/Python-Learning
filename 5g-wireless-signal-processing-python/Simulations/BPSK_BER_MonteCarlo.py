"""
Monte Carlo BER Simulation — BPSK
Author: Pujan Thapa Magar

Simulating 1000 BPSK transmissions to estimate the
Bit Error Rate at a given SNR using random noise.
"""

import math
import random   
from math import sqrt     
SNR_dB=2
SNR_linear=10**(SNR_dB/10)
symbols=[]
transmitted_bits=[]
sigma=1/sqrt(2*SNR_linear)
received_bits=[]
for i in range(1000):
    transmitted_bits.append(random.randint(0,1))
    if transmitted_bits[i]==0:
        symbols.append(+1)
    else:
        symbols.append(-1)
    noise=random.gauss(0,sigma)
    received_bits.append(symbols[i]+noise)

detected_bits=[]
for r in received_bits:
    if r > 0:
        detected_bits.append(0)
    else:
        detected_bits.append(1)
    
errors=0
for j in range(1000):
    if transmitted_bits[j] != detected_bits[j]:
        errors +=1

print(f"Errors: {errors}")
print(f"BER: {errors/1000:3f}")