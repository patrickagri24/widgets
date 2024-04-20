import numpy as np
import matplotlib.pyplot as plt

# Load your data from file
# Replace 'your_data_file.txt' with the path to your data file
data = np.loadtxt('your_data_file.txt')

# Extract time and signal from the data
time = data[:, 0]  # assuming time is in the first column
signal = data[:, 1]  # assuming signal is in the second column

# Perform Fourier transform
sampling_freq = 1 / (time[1] - time[0])  # Calculate sampling frequency
freqs = np.fft.fftfreq(len(signal), 1 / sampling_freq)  # Frequency bins
fft_vals = np.fft.fft(signal)  # Compute FFT

# Plot the frequency spectrum
plt.figure(figsize=(10, 5))
plt.plot(freqs, np.abs(fft_vals))
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
