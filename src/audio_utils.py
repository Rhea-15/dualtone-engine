import io
import numpy as np
from scipy.io import wavfile


def load_audio(file_bytes) -> tuple[int, np.ndarray, float, int]:
    """
    Loads WAV audio data from file bytes or a Streamlit UploadedFile object.
    
    Parameters:
        file_bytes: bytes, BytesIO, or Streamlit UploadedFile
        
    Returns:
        tuple containing:
            - sample_rate (int): Sampling frequency in Hz
            - signal (np.ndarray): 1D float32 numpy array normalized to [-1.0, 1.0]
            - duration_sec (float): Duration of audio in seconds
            - total_samples (int): Total number of audio samples
    """
    # Convert input to BytesIO if raw bytes are passed
    if isinstance(file_bytes, (bytes, bytearray)):
        file_bytes = io.BytesIO(file_bytes)
    elif hasattr(file_bytes, "getvalue"):
        # Handles Streamlit UploadedFile object
        file_bytes = io.BytesIO(file_bytes.getvalue())

    # Read WAV data
    sample_rate, data = wavfile.read(file_bytes)

    # Convert stereo to mono by averaging channels
    if data.ndim > 1:
        data = data.mean(axis=1)

    # Normalize integer PCM types to float32 range [-1.0, 1.0]
    if data.dtype == np.int16:
        signal = data.astype(np.float32) / 32768.0
    elif data.dtype == np.int32:
        signal = data.astype(np.float32) / 2147483648.0
    elif data.dtype == np.uint8:
        signal = (data.astype(np.float32) - 128.0) / 128.0
    else:
        signal = data.astype(np.float32)

    total_samples = len(signal)
    duration_sec = float(total_samples / sample_rate) if sample_rate > 0 else 0.0

    return sample_rate, signal, duration_sec, total_samples