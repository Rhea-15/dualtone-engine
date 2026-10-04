import numpy as np
from scipy.signal import butter, filtfilt


def apply_bandpass(signal: np.ndarray, sample_rate: int, lowcut: float = 600.0, highcut: float = 1700.0, order: int = 4) -> np.ndarray:
    """
    Applies a Butterworth Digital Bandpass Filter to isolate the DTMF frequency band.
    
    Parameters:
        signal (np.ndarray): Input audio signal
        sample_rate (int): Audio sampling rate in Hz
        lowcut (float): Lower cutoff frequency in Hz (default 600 Hz)
        highcut (float): Upper cutoff frequency in Hz (default 1700 Hz)
        order (int): Filter order (default 4)
        
    Returns:
        np.ndarray: Filtered audio signal array
    """
    nyquist = 0.5 * sample_rate
    low = lowcut / nyquist
    high = highcut / nyquist

    # Guard against invalid Nyquist bounds
    if high >= 1.0:
        high = 0.99

    b, a = butter(order, [low, high], btype='bandpass')
    filtered_signal = filtfilt(b, a, signal)
    
    return filtered_signal


# =====================================================================
# DEV 3 STUBS (Maintains agreement without breaking team imports)
# =====================================================================

def compute_fft(signal: np.ndarray, sample_rate: int) -> tuple[np.ndarray, np.ndarray]:
    """Stub for Dev 3 FFT implementation."""
    freqs = np.fft.rfftfreq(len(signal), d=1.0 / sample_rate)
    magnitudes = np.abs(np.fft.rfft(signal))
    return freqs, magnitudes


def find_peaks(freqs: np.ndarray, magnitudes: np.ndarray) -> tuple[int, int]:
    """Stub for Dev 3 Peak Detection implementation."""
    return 770, 1336