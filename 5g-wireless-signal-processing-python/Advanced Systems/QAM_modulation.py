"""
Modulator and Demodulator — BPSK, QPSK and 16QAM
I built this to understand how modulation actually works in practice.
BPSK is the simplest — 1 bit per symbol. QPSK does 2 bits per symbol.
16QAM does 4 bits per symbol but needs a much cleaner signal to work.
the higher the modulation order, more data you can send but the receiver
has a harder time decoding it — classic tradeoff in wireless comms.
Author: Pujan Thapa Magar
"""

import math
import random
import cmath
from math import sqrt, erfc

class Antenna:
    def __init__(self, gain_dbi:float,frequency_hz:float):
        self.gain_dbi=gain_dbi
        self.frequency_hz=frequency_hz
        self.wavelength=3e8/frequency_hz  # lambda = c/f
    
    def effective_area(self) -> float:
        # Aeff = (lambda^2 * G) / 4pi — how much signal the antenna actually captures
        return (self.wavelength**2*self.gain_dbi/(4*math.pi))
    
    def __str__(self) -> str:
        return f"Antenna (Gain= {self.gain_dbi} dbi, freq= {self.frequency_hz} Ghz)"
    
    def __repr__(self) -> str:
        return self.__str__()

ant1=Antenna(15,3.5e9)   # sub-6GHz antenna
ant2=Antenna(25,28e9)    # mmWave antenna

print(f"Antenna 1: {ant1}")
print(f"Wavelength: {ant1.wavelength*100:.2f} cm")
print(f"Effective Area: {ant1.effective_area()*1e4:.2f} cm²")
print(f"Antenna 2: {ant2}")
print(f"Wavelength: {ant2.wavelength*1000:.2f} mm")
print(f"Effective area: {ant2.effective_area()*1e4:.4f} cm²")


class Signal:
    """Represents a communication signal"""
    def __init__(self,power_dbm:float, frequency_Hz:float, Bandwidth_Hz:float):
     self._power_dbm=power_dbm
     self._frequency_Hz=frequency_Hz
     self._Bandwidth_Hz=Bandwidth_Hz

    @property
    def power_dbm(self) -> float:
       return self._power_dbm

    @power_dbm.setter
    def power_dbm(self,value:float):
       if value > 50:
          raise ValueError("Power cannot exceed more than 50 dBm (Safety Limit)")
       self._power_dbm=value

    @property
    def power_Watts(self) -> float:
       # converting dBm to watts — P(W) = 10^(dBm/10) * 0.001
       return 10**(self._power_dbm/10)*0.001
    
    @property
    def info(self) -> str:
       return (f"Signal: {self._power_dbm} dBm, "f"{self._frequency_Hz/1e9:.1f} GHz, "
              f"{self._Bandwidth_Hz/1e6:.0f} MHz BW")

sig = Signal(23, 3.5e9, 100e6)
print(sig.info)
print(f"Power in watts: {sig.power_Watts*1000:.1f} mW")
sig.power_dbm = 30
print(f"Updated power: {sig.power_dbm} dBm = {sig.power_Watts:.3f} W")


class Channel:
    """Base class — all channel types inherit from this"""
    def __init__(self,name):
        self.name=name
    
    def apply(self,signal:complex) ->complex:
        raise NotImplementedError("Subclasses must implement apply()")

    def __str__(self):
        return f"Channel_name: {self.name}"

class AWGN_Channel(Channel):
    # simplest channel — just adds white gaussian noise
    def __init__(self, snr_db:float):
        super().__init__("AWGN")
        self.snr_db=snr_db
        self.snr_linear=10**(self.snr_db/10)
    
    def apply(self,signal:complex) -> complex:
        sigma=1/math.sqrt(2*self.snr_linear)  # noise std dev based on SNR
        noise=complex(random.gauss(0,sigma),random.gauss(0,sigma))
        return signal + noise
    
    def __str__(self):
        return f"AWGN_Channel (SNR= {self.snr_db} dB)"

class Fading_Channel(Channel):
    """Rayleigh Fading Channel + AWGN Noise"""
    # more realistic than AWGN — signal also gets multiplied by a random fading tap
    def __init__(self, snr_db:float,num_taps:int=1):
        super().__init__("Rayleigh Fading")
        self.snr_db=snr_db
        self.snr_linear=10**(self.snr_db/10)
        self.num_taps=num_taps
        # generating random complex fading taps
        self.taps=[complex(random.gauss(0,1/math.sqrt(2)),random.gauss(0,1/math.sqrt(2))) for _ in range(num_taps)]

    def apply(self,signal:complex) -> complex:
        faded=signal*self.taps[0]   # apply fading
        sigma=1/math.sqrt(2*self.snr_linear)
        noise=complex(random.gauss(0,sigma),random.gauss(0,sigma))
        return faded + noise
    
    def __str__(self):
        return f"FadingChannel(SNR={self.snr_db}dB, taps={self.num_taps})"


class Modulator:
    """Mapping bits to symbols"""

    # all three schemes in one lookup table
    CONSTELLATIONS = {
        "BPSK": {0: 1+0j, 1: -1+0j},
        "QPSK": {0: (1+1j)/math.sqrt(2), 1: (-1+1j)/math.sqrt(2),
                 2: (-1-1j)/math.sqrt(2), 3: (1-1j)/math.sqrt(2)},
        # 16QAM — 4x4 grid of points, dividing by sqrt(10) keeps average power = 1
        "16-QAM":{0:complex(-3,-3)/math.sqrt(10),1:complex(-3,-1)/math.sqrt(10),2:complex(-3,1)/math.sqrt(10),3:complex(-3,3)/math.sqrt(10),
               4:complex(-1,-3)/math.sqrt(10),5:complex(-1,-1)/math.sqrt(10),6:complex(-1,1)/math.sqrt(10),7:complex(-1,3)/math.sqrt(10),
               8:complex(1,-3)/math.sqrt(10),9:complex(1,-1)/math.sqrt(10),10:complex(1,1)/math.sqrt(10),11:complex(1,3)/math.sqrt(10),
               12:complex(3,-3)/math.sqrt(10),13:complex(3,-1)/math.sqrt(10),14:complex(3,1)/math.sqrt(10),15:complex(3,3)/math.sqrt(10)}}

    def __init__(self,scheme:str="BPSK"):
        self.scheme=scheme
        self.constellation=self.CONSTELLATIONS[scheme]

    def modulate(self,bits:list) -> list:
        if self.scheme=="BPSK":
            # 1 bit per symbol, dead simple
            return [self.constellation[b] for b in bits]
        elif self.scheme == "QPSK":
            symbols = []
            for i in range(0,len(bits),2):
                # grab 2 bits, convert to index 0-3
                idx=bits[i]*2 + bits[i+1]
                symbols.append(self.constellation[idx])
            return symbols
        else:
            symbols=[]
            for i in range(0, len(bits),4):
                # grab 4 bits, convert to index 0-15
                idx= bits[i]*2**3 + bits[i+1]*2**2 + bits[i+2]*2 + bits[i+3]
                symbols.append(self.constellation[idx])
            return symbols


class Demodulator:
    """Mapping received symbols back to bits"""

    def __init__(self,scheme:str="BPSK"):
        self.scheme=scheme

    def demodulate(self,symbols:list) -> list:
        if self.scheme == "BPSK":
            # just check the sign of real part
            return [0 if s.real > 0 else 1 for s in symbols]
        elif self.scheme == "QPSK":
            bits = []
            for s in symbols:
                bits.append(0 if s.real > 0 else 1)
                bits.append(0 if s.imag > 0 else 1)
            return bits
        else:
            bits = []
            for s in symbols:
                # undo the sqrt(10) normalization first
                r = s.real*math.sqrt(10)
                i = s.imag*math.sqrt(10)
                # real part (I) → first 2 bits
                if r > 2:
                    bits.extend([1, 1])      # +3
                elif r > 0:
                    bits.extend([1, 0])      # +1
                elif r > -2:
                    bits.extend([0, 1])      # -1
                else:
                    bits.extend([0, 0])      # -3
                # imaginary part (Q) → last 2 bits
                if i > 2:
                    bits.extend([1, 1])      # +3
                elif i > 0:
                    bits.extend([1, 0])      # +1
                elif i > -2:
                    bits.extend([0, 1])      # -1
                else:
                    bits.extend([0, 0])      # -3
            return bits


class commSystem:
    """Complete Communication System (Tx -> Channel -> Rx)"""

    def __init__(self, modulation:str,snr_db:float,Channel_type:str="AWGN"):
        self.modulator=Modulator(modulation)
        self.demodulator=Demodulator(modulation)
        self.modulation=modulation
        self.snr_db=snr_db

        if Channel_type == "AWGN":
            self.channel=AWGN_Channel(snr_db)
        else:
            self.channel=Fading_Channel(snr_db)

    def simulate(self,num_bits:int) -> dict:
        """Run end-end simulation"""
        tx_bits = [random.randint(0,1) for _ in range(num_bits)]
        tx_symbols=self.modulator.modulate(tx_bits)
        rx_symbols = [self.channel.apply(s) for s in tx_symbols]
        rx_bits = self.demodulator.demodulate(rx_symbols)

        # count how many bits came out wrong
        errors = 0
        for a, b in zip(tx_bits,rx_bits):
            if a!= b:
                errors +=1
        ber = errors/num_bits

        return {
            "num_bits": num_bits,
            "errors": errors,
            "ber": ber,
            "snr_db": self.snr_db,
            "modulation": self.modulation,
        }

    def __str__(self):
        return f"CommSystem({self.modulation}, SNR={self.snr_db}dB)"


# seed 42 so results are reproducible every run
random.seed(42)
system=commSystem("BPSK",snr_db=10)
result=system.simulate(num_bits=10000)
print(f"System: {system}")
print(f"Result: {result['errors']} errors in {result['num_bits']} bits")
print(f"BER: {result['ber']:.4e}")

# sweeping SNR from 0 to 20 dB and comparing simulated vs theoretical BER
print("\nBPSK BER vs SNR:")
for snr in range(0, 21, 2):
    sys = commSystem("BPSK", snr_db=snr)
    res = sys.simulate(100000)
    theoretical = 0.5 * math.erfc(math.sqrt(10**(snr/10)))
    print(f"  SNR={snr:2d}dB: Simulated BER={res['ber']:.4e}, Theory={theoretical:.4e}")

# 16QAM needs higher SNR — testing at 15dB
print("\n16QAM at SNR=15dB:")
sys_16qam = commSystem("16-QAM", snr_db=15)
res_16qam = sys_16qam.simulate(10000)
print(f"System: {sys_16qam}")
print(f"BER: {res_16qam['ber']:.4e}")