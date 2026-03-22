# Adaptive Modulation and Coding (AMC) Selector

This was one of my exercises to understand how 5G NR dynamically selects
the modulation and coding scheme based on the channel SNR.

The idea is simple — better SNR means the channel can handle more complex
modulation, which means more bits per symbol and higher throughput.

## What it does

Takes a list of SNR values and prints the selected modulation scheme and
code rate for each one based on standard 5G NR MCS thresholds.

## SNR Thresholds used

| SNR Range | Modulation | Code Rate |
|-----------|------------|-----------|
| < 5 dB    | No transmission | N/A  |
| 5 - 10 dB | QPSK       | 1/3       |
| 10 - 15 dB| QPSK       | 1/2       |
| 15 - 20 dB| 16-QAM     | 1/2       |
| 20 - 25 dB| 64-QAM     | 2/3       |
| ≥ 25 dB   | 256-QAM    | 3/4       |

## Author
Pujan Thapa Magar