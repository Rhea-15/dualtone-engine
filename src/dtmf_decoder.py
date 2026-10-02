# src/dtmf_decoder.py
import numpy as np

# Standard DTMF Frequency Definitions (Hz)
ROW_FREQS = np.array([697, 770, 852, 941])
COL_FREQS = np.array([1209, 1336, 1477, 1633])

# 4x4 Keypad Mapping Table
DTMF_MATRIX = {
    (697, 1209): '1', (697, 1336): '2', (697, 1477): '3', (697, 1633): 'A',
    (770, 1209): '4', (770, 1336): '5', (770, 1477): '6', (770, 1633): 'B',
    (852, 1209): '7', (852, 1336): '8', (852, 1477): '9', (852, 1633): 'C',
    (941, 1209): '*', (941, 1336): '0', (941, 1477): '#', (941, 1633): 'D'
}

def decode_key(f_low: int, f_high: int) -> str:
    """
    Maps detected low and high frequencies to the corresponding DTMF key character.
    
    Parameters:
        f_low (int): Peak frequency in the low group (Hz)
        f_high (int): Peak frequency in the high group (Hz)
        
    Returns:
        str: Detected key symbol ('0'-'9', '*', '#', 'A'-'D', or 'Unknown')
    """
    return DTMF_MATRIX.get((f_low, f_high), "Unknown")