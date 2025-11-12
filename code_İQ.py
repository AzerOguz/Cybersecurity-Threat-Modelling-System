# Bu kod nümunəsi real ötürməni etmir — sadəcə IQ faylı üzərində rəqəmsal müdaxilə yaradır.
import numpy as np

# Parametrlər
fs = 1e6                # nümunə tezliyi (məsələn)
tone_freq = 50e3        # jammer tonal tezliyi (offset)
jammer_amp = 0.5        # jammer gücü nisbəti
input_iq_path = "signal_iq_c64.dat"   # complex64 IQ input (interleaved float32: I,Q)
output_iq_path = "signal_with_jam_iq_c64.dat"

# IQ faylını oxu (complex64)
data = np.fromfile(input_iq_path, dtype=np.complex64)

# vaxt vektoru
t = np.arange(len(data)) / fs

# sinxron tonal jammer (məsələn)
jammer_tone = np.exp(2j * np.pi * tone_freq * t).astype(np.complex64)

# genişzolaqlı ağ səs nümunəsi da əlavə etmək olar:
noise = (np.random.normal(size=len(data)) + 1j*np.random.normal(size=len(data))).astype(np.complex64)

# Birləşdirilmiş jammer
jammer = 0.7 * jammer_tone + 0.3 * noise

# Add jammer to original signal with desired scaling
out = data + (jammer_amp * jammer)

# Yaddaşa yaz
out.astype(np.complex64).tofile(output_iq_path)

print("Yaradıldı:", output_iq_path)

