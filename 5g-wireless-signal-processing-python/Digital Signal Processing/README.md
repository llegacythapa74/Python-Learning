# Digital Signal Processing

Signal generation and analysis tools used in wireless communications.

## What this covers
- Complex AWGN generation with proper variance scaling  
- Power validation — checking that our noise actually hits the target energy
- BPSK bit error rate analysis and SNR threshold detection
- MIMO channel matrix generation with Frobenius norm verification
- AND, OR, XOR operations on binary sequences
- Hamming distance — measuring bit errors between two sequences

## Why it matters
We spent time getting the sqrt(0.5) scaling right because accurate noise power is the baseline for every SNR calculation we run. If the variance is off, our whole link budget drifts.

The BPSK BER curve tells us exactly where reliable communication starts—finding that 1e-5 threshold is how we size our link budgets in practice.

For MIMO systems, the Frobenius norm gives us the total channel energy. We verify our manual calculation against built-in functions because in real simulations, you can't afford to be off by even 0.1 dB.

Hamming distance is how we measure channel errors in practice. The more bits that flip, the worse the channel quality.

## Files
- `Gaussian_Noise.py` — complex Gaussian noise with power validation (Pujan Thapa Magar)
- `bpsk_ber_analysis.py` — theoretical BPSK BER calculation and SNR threshold detection (Pujan Thapa Magar)
- `channel_matrix_analysis.py` — MIMO channel matrix generation with Frobenius norm verification (Pujan Thapa Magar)
- `Bitwise_and_Hamming.py` — bitwise ops and Hamming distance