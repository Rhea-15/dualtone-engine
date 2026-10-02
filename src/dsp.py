# src/dsp.py (Dev 3 Section: FFT & Peak Finding)
import numpy as np
from scipy.fft import rfft, rfftfreq

ROW_FREQS = np.array([697, 770, 852, 941])
COL_FREQS = np.array([1209, 1336, 1477, 1633])

def compute_fft(signal: np.ndarray, sample_rate: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Calculates the Real Fast Fourier Transform (rFFT) of a 1D time-domain signal.
    
    Parameters:
        signal (np.ndarray): Time-domain signal array
        sample_rate (int): Sampling frequency Fs in Hz
        
    Returns:
        tuple[np.ndarray, np.ndarray]: (frequencies array in Hz, magnitude spectrum array)
    """
    n_samples = len(signal)
    
    # Calculate real-valued FFT magnitude and corresponding frequency bins
    fft_values = np.abs(rfft(signal)) / n_samples
    freqs = rfftfreq(n_samples, 1 / sample_rate)
    
    return freqs, fft_values

def find_peaks(freqs: np.ndarray, magnitudes: np.ndarray) -> tuple[int, int]:
    """
    Isolates peak magnitudes in DTMF low band (600-1000 Hz) and high band (1100-1700 Hz),
    and quantizes them to the closest standard nominal DTMF frequencies.
    
    Parameters:
        freqs (np.ndarray): Frequency axis array
        magnitudes (np.ndarray): FFT magnitude array
        
    Returns:
        tuple[int, int]: (quantized_low_freq, quantized_high_freq)
    """
    # 1. Low Band Search (600 Hz to 1000 Hz)
    low_mask = (freqs >= 600) & (freqs <= 1000)
    if np.any(low_mask):
        peak_low_raw = freqs[low_mask][np.argmax(magnitudes[low_mask])]
    else:
        peak_low_raw = 0.0

    # 2. High Band Search (1100 Hz to 1700 Hz)
    high_mask = (freqs >= 1100) & (freqs <= 1700)
    if np.any(high_mask):
        peak_high_raw = freqs[high_mask][np.argmax(magnitudes[high_mask])]
    else:
        peak_high_raw = 0.0

    # 3. Quantize peaks to nearest nominal DTMF frequencies
    f_low = int(ROW_FREQS[np.argmin(np.abs(ROW_FREQS - peak_low_raw))])
    f_high = int(COL_FREQS[np.argmin(np.abs(COL_FREQS - peak_high_raw))])

    return f_low, f_high