import numpy as np
import matplotlib.pyplot as plt

# ---------------- AM MODULATION ---------------- #

fs = 1000
t = np.arange(0, 1, 1/fs)

fm = 5
fc = 50
Am = 1
Ac = 2

m = Am * np.sin(2*np.pi*fm*t)
c = Ac * np.sin(2*np.pi*fc*t)
s = (Ac + m) * np.sin(2*np.pi*fc*t)

plt.figure(figsize=(10,6))

plt.subplot(3,1,1)
plt.plot(t, m)
plt.title("Message Signal")

plt.subplot(3,1,2)
plt.plot(t, c)
plt.title("Carrier Signal")

plt.subplot(3,1,3)
plt.plot(t, s)
plt.title("AM Modulated Signal")

plt.tight_layout()
plt.show()


# ---------------- BPSK WITH BER ---------------- #

N = 1000
bits = np.random.randint(0, 2, N)

bpsk_signal = 2*bits - 1

snr_db_range = range(0, 11)
ber_values = []

for snr_db in snr_db_range:
    snr = 10**(snr_db/10)
    noise = np.random.normal(0, 1, N)
    received = bpsk_signal + noise/np.sqrt(snr)
    detected_bits = np.where(received > 0, 1, 0)
    errors = np.sum(bits != detected_bits)
    ber = errors / N
    ber_values.append(ber)

plt.figure()
plt.plot(snr_db_range, ber_values)
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.title("BER vs SNR for BPSK")
plt.grid()
plt.show()