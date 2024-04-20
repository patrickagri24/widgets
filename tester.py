import numpy as np

# Parameters for the synthetic signals
num_samples = 1000  # Number of samples
sampling_freq = 1# Sampling frequency in Hz
#cannot break the equation duration = num_samples/sampling_freq or its derivations
duration = num_samples / sampling_freq  # Duration of signal in seconds
#sampling_freq = num_samples/duration

# Parameters for the first sinusoidal tone
amplitude_1 = 1.0  # Amplitude of the first sinusoidal signal
frequency_1 = 50 # Frequency of the first sinusoidal signal in Hz
phase_1 = 0.0  # Phase of the first sinusoidal signal in radians

# Parameters for the second sinusoidal tone
amplitude_2 = 0.5  # Amplitude of the second sinusoidal signal
frequency_2 = 10  # Frequency of the second sinusoidal signal in Hz
phase_2 = np.pi / 4  # Phase of the second sinusoidal signal in radians

# Create time array
time = np.linspace(0, duration, num_samples)

# Create the first sinusoidal signal
signal_1 = amplitude_1 * np.sin(2 * np.pi * frequency_1 * time + phase_1)

# Create the second sinusoidal signal
signal_2 = amplitude_2 * np.sin(2 * np.pi * frequency_2 * time + phase_2)

# Combine the signals into one by adding them
combined_signal = signal_1 + signal_2

# Combine time and combined_signal into a single array
data = np.column_stack((time, combined_signal))

# Save the synthetic signal to a file
# Replace 'synthetic_signal_two_tones.txt' with the desired file path
np.savetxt('synthetic_signal_two_tones.txt', data, fmt='%.6f', header='Time (s)\tSignal')
