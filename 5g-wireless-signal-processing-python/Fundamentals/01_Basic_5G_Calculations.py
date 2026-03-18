"""
Basic 5G Wireless Calculations

Includes:
- Wavelength computation for mmWave systems
- Complex signal magnitude and phase extraction
- RF unit conversions (dB, dBm, Watts)

Author: Pujan Thapa Magar
"""
# ─────────────────────────────────────────
# 1. mmWave Wavelength Calculation
# ─────────────────────────────────────────
# At 28 GHz, short wavelength enables compact massive MIMO arrays.
# Antenna spacing is typically λ/2 ≈ 5.4 mm for 64-element arrays.

import math 
subcarriers = 256
carrier_frequency = 28e9  # Hz
bandwidth = 400e6         # Hz
antenna_elements = 64
speed_of_light = 3e8      # m/s

wavelength = (speed_of_light / carrier_frequency) * 1000  # converting to mm
print(f"Wavelength: {wavelength:.2f} mm")

# ─────────────────────────────────────────
# 2. Complex Baseband Signal Analysis
# ─────────────────────────────────────────
# In 5G NR, signals are represented as complex baseband samples (I + jQ).
# Magnitude relates to received signal power, phase carries modulation info.

r = 1.5 + 2.3j  # complex baseband sample (I=1.5, Q=2.3)

magnitude = abs(r)                          # |r| = sqrt(I² + Q²)
power = abs(r)**2                           # received power proportional to |r|²
phase = math.degrees(math.atan2(r.imag, r.real))  # phase angle in degrees

print(f"Magnitude: {magnitude:.4f}")
print(f"Power |r|²: {power:.4f}")
print(f"Phase: {phase:.2f}°")

# ─────────────────────────────────────────
# 3. RF Unit Conversions
# ─────────────────────────────────────────
# dB, dBm and Watts are the core language of RF engineering.

db_value = -3
power_w = 0.001      # 1 mW reference
dbm_value = 30

linear_value = 10 ** (db_value / 10)                    # -3 dB = half power
dbm_from_watt = 10 * math.log10(power_w / 0.001)
watt_from_dbm = (10 ** (dbm_value / 10)) * 0.001        # 30 dBm = 1W

print(f"Linear value: {linear_value:.4f}")
print(f"dBm from Watts: {dbm_from_watt:.2f} dBm")
print(f"Watts from dBm: {watt_from_dbm:.4f} W")