"""
Link Budget and Channel Fundamentals
Includes:
- Shannon capacity calculation
- Free Space Path Loss at 28 GHz mmWave
Author: Pujan Thapa Magar
"""
import math

# ─────────────────────────────────────────
# 1. Shannon Capacity
# ─────────────────────────────────────────
# Shannon gives the max bitrate a channel can handle.
# More bandwidth or better SNR = higher capacity.

B = 20e6       # bandwidth in Hz
SNR_db = 15    # SNR in dB

def db_to_linear(SNR_db):
    return 10 ** (SNR_db / 10)    # dB to linear

C = B * math.log2(1 + db_to_linear(SNR_db))

print(f"Bandwidth: {B/1e6} MHz")
print(f"SNR: {SNR_db} dB = {db_to_linear(SNR_db):.2f} linear")
print(f"Shannon Capacity: {C/1e6:.2f} Mbps")

# ─────────────────────────────────────────
# 2. Free Space Path Loss at 28 GHz
# ─────────────────────────────────────────
# Signal drops fast at high frequencies.
# That's why mmWave 5G needs many small cells close together.

freq = 28e9    # 28 GHz mmWave
c = 3e8        # speed of light
distances = [10, 50, 100, 500]

def fspl(d):
    return 20*math.log10(freq) + 20*math.log10(d) + 20*math.log10(4*math.pi/c)

for d in distances:
    print(f"FSPL at {d}m: {fspl(d):.2f} dB")