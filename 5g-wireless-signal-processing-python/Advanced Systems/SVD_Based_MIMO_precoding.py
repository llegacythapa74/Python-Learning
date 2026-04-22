"""
SVD Based MIMO Precoding — With and Without Precoding Comparison
I wanted to see the actual difference SVD precoding makes in practice.
The idea is simple — without precoding the streams interfere with each other
and the receiver struggles to separate them. With SVD precoding, the channel
is decomposed into independent parallel streams and each one is detected cleanly.
The BER comparison at the end shows exactly how much precoding helps.
Author: Pujan Thapa Magar
"""
import numpy as np

# Defining the channel matrix as 4x2:
H = np.array([[0.5+0.3j, 0.6-0.8j],
              [0.1-0.2j, 0.9+0.8j],
              [0.7-0.6j, 0.5+0.4j],
              [0.2-0.6j, 0.3+0.4j]])

# SVD: H = U * S * V^H
U, sigma, Vh = np.linalg.svd(H, full_matrices=False)
V = Vh.conj().T

# transmit signal (keep your style)
x_signal = np.random.randn(2) + 1j * np.random.randn(2)
tx_bits = np.sign(x_signal.real)

# WITHOUT precoding
noise = 0.01 * (np.random.randn(4) + 1j*np.random.randn(4))
y_no_precoding = H @ x_signal + noise

x_hat_no_precoding = np.linalg.pinv(H) @ y_no_precoding
bits_no_precoding = np.sign(x_hat_no_precoding.real)

# WITH precoding
x_precoded = V @ x_signal

noise2 = 0.01 * (np.random.randn(4) + 1j*np.random.randn(4))
y_precoding = H @ x_precoded + noise2

y_rotated = U.conj().T @ y_precoding
x_hat_precoding = y_rotated / (sigma + 1e-12)
bits_precoding = np.sign(x_hat_precoding.real)

# BER Analysis
def ber(tx_bits, rx_bits):
    return np.sum(tx_bits != rx_bits) / len(tx_bits)

# true transmitted bits
tx_bits = np.sign(x_signal.real)

ber_no_precoding = ber(tx_bits, bits_no_precoding)
ber_precoding = ber(tx_bits, bits_precoding)

# Results
print("Transmitted bits:", tx_bits)
print("Detected (no precoding):", bits_no_precoding)
print("Detected (SVD precoding):", bits_precoding)

print("\nBER without precoding:", ber_no_precoding)
print("BER with SVD precoding:", ber_precoding)