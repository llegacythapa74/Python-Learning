# Link and Channel Fundamentals

Basic calculations for understanding how wireless channels behave.

## What this covers
- Shannon capacity — maximum data rate for a given bandwidth and SNR
- Free Space Path Loss at 28 GHz — how signal weakens over distance at mmWave
- 3GPP TDL channel models — standard channel models used in 5G NR simulations

## Why it matters
Before designing any 5G system you need to know how much data the channel
can theoretically carry and how much signal you lose over distance.
At 28 GHz the path loss is severe — that's the core challenge of mmWave 5G.
TDL models are what 3GPP uses to standardize channel conditions for testing
and simulation — I used them here to practice Python dictionaries.

## Files
- `Shannon_Capacity_and_FSPL.py` — Shannon capacity and FSPL calculations
- `TDL_Channel_Models.py` — 3GPP TDL-A to TDL-E models with delay spread and LOS conditions