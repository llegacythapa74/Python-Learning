# import numpy as np

# arr = np.array([[1,2,3],[5,6,7]])
# print(arr)
# print(arr.shape)
# print(arr.ndim)
# print(arr.dtype)
# print(arr[1,0])

# a = np.array([1,2,3,4,56])
# print(a*2)
# print(np.ones((2,4)))
# print(np.linspace(0,1,5))
import numpy as np
import random 
import math
from math import sqrt, erfc


snr_values = np.array([0,5,10,15,20,25,30])
print(f"SNR Values: {snr_values}")
print(f"Type: {type(snr_values)}, dType: {snr_values.dtype}, Shape: {snr_values.shape}")

# complex array coeffecients
h = np.array([complex(0.5,0.3),complex(-0.2,0.8),complex(0.1,-0.4)])
print(f"Channel Taps: {h}")
print(f"dtype: {h.dtype}")

#Common Array Creation Functions
zeros = np.zeros((3,3))
ones = np.ones((3,3))
arrange = np.arange(0,31,7)
linspace = np.linspace(0, 30, 7) 

print(f" Zeros: {zeros}")
print(f"Ones: {ones}")
print(f"Arrange: {arrange}")
print(f"Linespace: {linspace}")

# 2D Arrays Matrices for the MIMO
h_MIMO = np.array([[complex(0.5,-0.3),complex(1,-2)],[complex(-1,-1),complex(0.8,-0.5)]])
print(f"2X2 MIMO Channel Matrix: {h_MIMO}")
print(f" Shape of the channel matrix: {h_MIMO.shape}")

# Complex Gaussian Noise for the AWGN Channel
complex_noise = (np.random.randn(10) + 1j*np.random.randn(10))/sqrt(2)
print(f"Complex Noise: {complex_noise[:3]}")

# Vectorized Operations
snr_db = np.arange(0,31,5)
snr_linear = 10**(snr_db/10)
capacity = np.log2(1 + snr_linear)

for s_db,snr_lin,cap in zip(snr_db,snr_linear,capacity):
    print(f"  {s_db:2d} dB = {snr_lin:8.1f} linear -> {cap:.2f} bps/Hz")

# Comparison: Python loop vs NumPy
import time

N = 1000000
# Python loop (SLOW)
start = time.time()
result_python = [x**2 for x in range(N)]
time_python = time.time() - start

# NumPy vectorized (FAST)
start = time.time()
arr = np.arange(N)
result_numpy = arr ** 2
time_numpy = time.time() - start

print(f"\nSquaring {N} numbers:")
print(f"  Python loop: {time_python*1000:.1f} ms")
print(f"  NumPy:       {time_numpy*1000:.1f} ms")
print(f"  Speedup:     {time_python/time_numpy:.0f}x")


# 3. Array Indexing and Slicing

N_fft = 16
freq_grid = np.arange(-N_fft//2,N_fft//2)
print(f"Freq Grid: {freq_grid}")
print(f"First 4 elements: {freq_grid[:4]}")
print(f"Last 4 elements: {freq_grid[-4:]}")
print(f"Every other elements in the gap of 2: {freq_grid[::2]}")

# Complex number operations
h = np.array([0.5+0.3j, -0.2+0.8j, 0.1-0.4j, 0.7+0.1j])
print(f"\nChannel taps: {h}")
print(f"Magnitude: {np.abs(h)}")