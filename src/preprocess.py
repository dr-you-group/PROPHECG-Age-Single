import numpy as np
from scipy.signal import butter, filtfilt


def remove_dc_offset(x: np.ndarray) -> np.ndarray:
    """1) DC 오프셋 제거"""
    return x - np.mean(x)


def bandpass_filter(
    x: np.ndarray,
    fs: float = 200.0,
    lowcut: float = 0.5,
    highcut: float = 50.0,
    order: int = 3
) -> np.ndarray:
    """2) 0.5–50 Hz Butterworth bandpass filter"""
    nyq = 0.5 * fs
    low, high = lowcut / nyq, highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, x)


def normalize(x: np.ndarray) -> np.ndarray:
    """3) Min–Max 정규화 (0–1)"""
    mn, mx = x.min(), x.max()
    return (x - mn) / (mx - mn) if mx != mn else np.zeros_like(x)


def preprocess_ecg(x: np.ndarray, fs: float = 200.0) -> np.ndarray:
    """
    ECG 전처리 전체 파이프라인:
    1) DC offset 제거
    2) Bandpass filter
    3) Min–Max normalization
    """
    x1 = remove_dc_offset(x)
    x2 = bandpass_filter(x1, fs=fs)
    x3 = normalize(x2)
    return x3
