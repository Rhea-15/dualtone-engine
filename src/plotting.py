# src/plotting.py (Dev 3 Section: FFT Spectrum Chart)
import plotly.graph_objects as go
import numpy as np

def create_fft_plot(freqs: np.ndarray, magnitudes: np.ndarray, f_low: int = None, f_high: int = None) -> go.Figure:
    """
    Generates an interactive Plotly figure showing Magnitude vs. Frequency
    with vertical indicator lines for detected low and high frequencies.
    """
    # Filter frequencies between 400 Hz and 2000 Hz for focused view
    view_mask = (freqs >= 400) & (freqs <= 2000)
    
    fig = go.Figure()

    # Add Spectrum Trace
    fig.add_trace(go.Scatter(
        x=freqs[view_mask],
        y=magnitudes[view_mask],
        mode='lines',
        name='FFT Magnitude',
        line=dict(color='#10B981', width=2)
    ))

    # Add Vertical Indicator Lines for Detected Low Frequency
    if f_low:
        fig.add_vline(
            x=f_low, line_dash="dash", line_color="#F59E0B",
            annotation_text=f"Low: {f_low} Hz", annotation_position="top left"
        )

    # Add Vertical Indicator Lines for Detected High Frequency
    if f_high:
        fig.add_vline(
            x=f_high, line_dash="dash", line_color="#EF4444",
            annotation_text=f"High: {f_high} Hz", annotation_position="top right"
        )

    # Layout styling
    fig.update_layout(
        title="FFT Frequency Spectrum",
        xaxis_title="Frequency (Hz)",
        yaxis_title="Magnitude",
        template="plotly_dark",
        height=320,
        margin=dict(l=40, r=40, t=40, b=40)
    )

    return fig