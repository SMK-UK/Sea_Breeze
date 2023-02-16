'''
Spectroscopic Data Analysis
Sean Keenan, PhD Physics
Quantum Memories Group, Heriot-Watt University, Edinburgh
2021
'''

# import relevant modules

import seabreeze as sb
from seabreeze.spectrometers import list_devices, Spectrometer
import matplotlib.pyplot as mp
import numpy as np

# find spectrometer and set to use
spec = Spectrometer.from_first_available()

''' collection parameters & file name'''
dir = 'C:\\Users\\sk88\\Desktop'
folder = 'visible'
file = '188.txt'
path = dir + '\\' + folder + '\\' + file
#integration time (micro seconds)
int_time = 1000
averages = 10

spec.integration_time_micros(int_time)
wavelength = spec.wavelengths()

''' data collection '''

intensities = []

for index in range(averages):
    intensities.append(spec.intensities())

temp = 0
for array in intensities:
    temp += array

intensity = temp / averages

'''check plot '''

fig, ax = mp.subplots()
ax.plot(wavelength, intensity)
ax.set(xlabel = 'wavelengths (nm)', ylabel = 'intensity (a.u)')

''' write to file '''

data = np.stack((wavelength, intensity), axis=1)

with open(path, 'x') as new_file:
    for line in data:
        new_file.write(str(line[0]) + '\t' + str(line[1]) + '\n')