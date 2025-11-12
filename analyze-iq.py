#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift

# Parametrlər: ab.py içində istifadə etdiyiniz fs ilə uyğunlaşdırın
fs = 1e6
fname = "signal_with_jam_iq_c64.dat"

data = np.fromfile(fname, dtype=np.complex64)
N = len(data)
print("Samples:", N)

# Average power (dB)
power = 10*np.log10(np.mean(np.abs(data)**2))
print("Avg power (dB):", power)

# FFT (centered)
spec = fftshift(fft(data))
freqs = np.linspace(-fs/2, fs/2, N)

plt.figure(figsize=(8,4))
plt.plot(freqs/1e3, 20*np.log10(np.abs(spec)/np.max(np.abs(spec))))
plt.xlabel("Frequency (kHz)")
plt.ylabel("Relative magnitude (dB)")
plt.title("Centered FFT (relative)")
plt.grid(True)
plt.tight_layout()
plt.savefig("fft_plot.png")
print("Saved fft_plot.png")

# Spectrogram (short-time)
plt.figure(figsize=(8,4))
plt.specgram(data, NFFT=1024, Fs=fs, noverlap=512, scale='dB')
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.title("Spectrogram")
plt.colorbar(label='dB')
plt.tight_layout()
plt.savefig("spectrogram.png")
print("Saved spectrogram.png")
