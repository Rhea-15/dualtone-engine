# test_dev3.py
import sys
import os

# Add root project folder to Python search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np
from src.dsp import compute_fft, find_peaks
from src.dtmf_decoder import decode_key, DTMF_MATRIX

def generate_dtmf_tone(f_low: int, f_high: int, duration: float = 0.3, sample_rate: int = 8000) -> np.ndarray:
    """Synthesizes a clean DTMF tone signal array."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Dual-tone sinusoid: s(t) = sin(2*pi*f_low*t) + sin(2*pi*f_high*t)
    return np.sin(2 * np.pi * f_low * t) + np.sin(2 * np.pi * f_high * t)

def run_dev3_tests():
    print("=== RUNNING DEV 3 UNIT TESTS ===")
    sample_rate = 8000
    passed = 0
    total = len(DTMF_MATRIX)

    for (target_low, target_high), expected_key in DTMF_MATRIX.items():
        # 1. Synthesize signal
        signal = generate_dtmf_tone(target_low, target_high, sample_rate=sample_rate)
        
        # 2. Compute FFT
        freqs, mags = compute_fft(signal, sample_rate)
        
        # 3. Find Peaks
        f_low, f_high = find_peaks(freqs, mags)
        
        # 4. Decode Key
        detected_key = decode_key(f_low, f_high)
        
        # Assertions
        assert f_low == target_low, f"Low freq mismatch! Expected {target_low}, got {f_low}"
        assert f_high == target_high, f"High freq mismatch! Expected {target_high}, got {f_high}"
        assert detected_key == expected_key, f"Key mismatch! Expected {expected_key}, got {detected_key}"
        
        print(f"[PASS] Tone ({target_low}Hz + {target_high}Hz) => Detected: '{detected_key}'")
        passed += 1

    print(f"\n✅ All {passed}/{total} DTMF Keys Successfully Decoded!")

if __name__ == "__main__":
    run_dev3_tests()