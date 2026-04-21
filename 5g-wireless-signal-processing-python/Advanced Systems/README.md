# Advanced Systems

This folder is where things get more interesting. I built four simulations
that connect the theoretical concepts from lectures to actual working code.
Each one covers a core part of how modern 5G systems work under the hood.

---

## What is inside

### 1. `modulator_demodulator.py` — BPSK, QPSK and 16QAM Communication System

This was my attempt to build a complete communication chain from scratch —
transmitter, channel and receiver all in one place. I wanted to understand
not just what modulation is but how the bits actually become complex symbols,
travel through a noisy channel and get decoded back on the other side.

Supports three modulation schemes:

| Scheme   | Bits per Symbol | Minimum SNR needed |
|----------|-----------------|--------------------|
| BPSK     | 1               | Low (~6 dB)        |
| QPSK     | 2               | Medium (~10 dB)    |
| 16-QAM   | 4               | High (~15 dB)      |

Also includes AWGN and Rayleigh fading channel models.
The simulation sweeps SNR from 0 to 20 dB and compares simulated BER
against the theoretical formula — good way to verify the implementation is correct.

---

### 2. `antenna_array.py` — Phased Array Beamforming Simulator

I built this to understand how a 5G base station points its beam toward a user
without physically moving the antenna. The trick is giving each antenna element
a slightly different phase shift — this is called a steering vector.

The beam pattern method then sweeps all angles from -90 to +90 degrees and
shows where the beam is strong and where it cancels out. With 10 antennas
the peak magnitude at 0 degrees comes out exactly 10 — all elements perfectly
in phase. This is the mathematical core of mmWave beamforming in 5G NR.

---

### 3. `link_budget.py` — Free Space Link Budget Calculator

This one simulates how much signal survives after travelling through open space.
I wanted to understand the tradeoff between distance, frequency and SNR that
every RF engineer has to deal with when designing a wireless link.

Given a distance it calculates the received SNR. Given a target SNR it works
backwards and finds the maximum distance where communication is still possible.
Tested at 75 GHz mmWave — the numbers show exactly why mmWave has such
short range compared to sub-6 GHz.

| Method              | Input        | Output          |
|---------------------|--------------|-----------------|
| `calculate_snr()`   | Distance (m) | SNR (dB)        |
| `find_max_distance()` | Target SNR (dB) | Distance (km) |

---

### 4. `water_filling.py` — Water-Filling Power Allocation for MIMO Eigenchannels

After learning about SVD in MIMO systems I wanted to see how a base station
actually decides how much power to put on each spatial stream. The answer is
water-filling — pour more power into strong eigenchannels and turn off the
weak ones entirely rather than wasting energy on them.

The idea comes from the fact that after SVD the channel becomes parallel
independent pipes with different qualities. If you split power equally across
all of them you end up wasting a lot of it on pipes that are nearly blocked.
Water-filling finds the optimal split by treating each 1/λ as the depth of a
bucket and pouring water until the level is the same everywhere.

Given eigenvalues [4.0, 1.0, 0.25, 0.01] and total power = 4, the algorithm
progressively adds channels until the water level is low enough that the next
channel would receive negative power. In this case only the top 2 channels
are worth using:

| Channel | λ (gain) | 1/λ (depth) | Power allocated | Status |
|---------|----------|-------------|-----------------|--------|
| 1       | 4.0      | 0.25        | 2.375           | ON     |
| 2       | 1.0      | 1.00        | 1.625           | ON     |
| 3       | 0.25     | 4.00        | 0.000           | OFF    |
| 4       | 0.01     | 100.0       | 0.000           | OFF    |

Compared to equal power allocation this gives about 30% more capacity with
the same total transmit power — a good reminder that smarter signal processing
often beats just throwing more power at the problem.

---

## Concepts covered

- Modulation and demodulation (BPSK, QPSK, 16QAM)
- AWGN and Rayleigh fading channel models
- Bit Error Rate (BER) simulation vs theoretical
- Phased array steering vectors and beam patterns
- Free Space Path Loss (FSPL)
- SNR calculation and link budget analysis
- SVD-based eigenchannel decomposition
- Water-filling power allocation and channel capacity

---

## How to run

Each file is standalone, just run directly:

```bash
python modulator_demodulator.py
python antenna_array.py
python link_budget.py
python water_filling.py