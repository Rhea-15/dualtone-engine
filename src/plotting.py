import numpy as np
import plotly.graph_objects as go


def plot_waveform(
    signal: np.ndarray, 
    sample_rate: int, 
    title: str = "TIME DOMAIN WAVEFORM", 
    filtered_signal: np.ndarray | None = None
) -> go.Figure:
    """
    Generates an interactive Plotly figure for time-domain signal waveform.
    
    Parameters:
        signal (np.ndarray): Primary audio signal
        sample_rate (int): Audio sampling rate in Hz
        title (str): Title of the plot
        filtered_signal (np.ndarray, optional): Filtered signal to compare against raw
        
    Returns:
        go.Figure: Styled Plotly interactive figure
    """
    time_axis = np.linspace(0, len(signal) / sample_rate, num=len(signal))
    fig = go.Figure()

    # Base styling matching dark terminal theme
    dark_bg = "#0B131E"
    paper_bg = "#0B131E"
    grid_color = "#1E2A3A"
    text_color = "#DCEBFB"

    if filtered_signal is not None:
        fig.add_trace(
            go.Scatter(
                x=time_axis, 
                y=signal, 
                mode='lines', 
                name='Raw Signal', 
                line=dict(color='#0088FF', width=1), 
                opacity=0.6
            )
        )
        fig.add_trace(
            go.Scatter(
                x=time_axis, 
                y=filtered_signal, 
                mode='lines', 
                name='Filtered Signal', 
                line=dict(color='#00E5FF', width=1.5)
            )
        )
    else:
        fig.add_trace(
            go.Scatter(
                x=time_axis, 
                y=signal, 
                mode='lines', 
                name='Signal Amplitude', 
                line=dict(color='#00E5FF', width=1.2)
            )
        )

    fig.update_layout(
        title=dict(text=title, font=dict(color=text_color, size=16)),
        xaxis=dict(
            title="Time (seconds)", 
            color=text_color, 
            gridcolor=grid_color, 
            zerolinecolor=grid_color
        ),
        yaxis=dict(
            title="Amplitude", 
            color=text_color, 
            gridcolor=grid_color, 
            zerolinecolor=grid_color
        ),
        paper_bgcolor=paper_bg,
        plot_bgcolor=dark_bg,
        margin=dict(l=40, r=40, t=50, b=40),
        legend=dict(font=dict(color=text_color), orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    return fig


# =====================================================================
# DEV 3 STUB (Maintains agreement without breaking team imports)
# =====================================================================

def plot_spectrum(freqs: np.ndarray, magnitudes: np.ndarray, f_low: int = 0, f_high: int = 0) -> go.Figure:
    """Stub for Dev 3 Frequency Spectrum Plot implementation."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=freqs, y=magnitudes, mode='lines', line=dict(color='#00FF88'), name='Magnitude'))

    # Draw indicator lines if peak frequencies are supplied
    if f_low > 0:
        fig.add_vline(x=f_low, line_dash="dash", line_color="#FF5555", annotation_text=f"Low: {f_low}Hz")
    if f_high > 0:
        fig.add_vline(x=f_high, line_dash="dash", line_color="#FF5555", annotation_text=f"High: {f_high}Hz")

    fig.update_layout(
        title="FREQUENCY SPECTRUM (FFT)",
        paper_bgcolor="#0B131E",
        plot_bgcolor="#0B131E",
        font=dict(color="#DCEBFB")
    )
    return fig