import math
import matplotlib.pyplot as plt
import numpy as np
from cmath import atan

# Constants (would be changed depend on real case)
D = 15
time_iter = 0.001
accuracy = int((1 / time_iter)/10)

# First signal
time_start_1 = 0  # time when signal start
time_stop_1 = 5  # time when signal stops
signal_1_time = []  # argument of function
f1 = 3  # coef on x in equation
signal_1 = []  # list of values of function
real_signal_1 = []  # list to create the plot

# Second signal
time_start_2 = 4
time_stop_2 = 8
signal_2_time = []
f2 = 6
signal_2 = []
real_signal_2 = []

# Sum of both functions
signals = []
signals_time = []  # argument of function
ModuleS = []  # module of complex number

# Phase params
period = 0
Phase = []


def F(t, f):
    t = f * (17.5 * 10**6 + (((22.5-17.5) * t * 10**6)/(250 * 10**(-6))))
    return t


def St(t, f):
    s = D * (complex(math.cos(F(t, f)), math.sin(F(t, f))))
    return s


def phase(real, imag):
    return (atan(imag / real)).real


def make_real(x):
    return x.real


def make_imaginary(x):
    return x.imag

case_1 = False  # case, when first signal ends before signal 2 starts
case_2 = False  # case, when first signal ends after signal 2 starts
if time_stop_1 <= time_start_2:
    case_1 = True
else:
    case_2 = True

Time = 0

while Time <= time_stop_2:
    if Time >= time_start_1 and Time <= time_stop_1:
        signal_1.append(St(Time, f1))
        signal_1_time.append(Time)
    else:
        signal_1.append(0)
        signal_1_time.append(Time)
    if Time >= time_start_2 and Time <= time_stop_2:
        signal_2.append(St(Time, f2))
        signal_2_time.append(Time)
    else:
        signal_2.append(0)
        signal_2_time.append(Time)
    if case_1 == True and Time <= time_stop_1:  # signals calculation
        signals.append(St(Time, f1) + 0)
        signals_time.append(Time)
    elif case_1 == True and Time >= time_stop_1 and Time <= time_start_2:
        signals.append(0)
        signals_time.append(Time)
    elif case_1 == True and Time >= time_start_2:
        signals.append(0 + St(Time, f2))
        signals_time.append(Time)
    elif case_2 == True and Time <= time_start_2:
        signals.append(St(Time, f1) + 0)
        signals_time.append(Time)
    elif case_2 == True and Time >= time_start_2 and Time <= time_stop_1:
        signals.append(St(Time, f1)+St(Time, f2))
        signals_time.append(Time)
    elif case_2 == True and Time >= time_stop_1:
        signals.append(0 + St(Time, f2))
        signals_time.append(Time)
    Time += time_iter
    Time = round(Time, accuracy)

for number in range(len(signals)):
    # phase calculation
    if phase(signals[number].real, signals[number].imag) < math.pi / 2:
        period += 1
        Phase.append(round(phase(
            signals[number].real, signals[number].imag) + (math.pi / 2 * period), accuracy))
    else:
        Phase.append(
            round(phase(signals[number].real, signals[number].imag), accuracy))
    # module calculation
    ModuleS.append(
        round(math.sqrt((signals[number].real**2)+(signals[number].imag**2)), accuracy))
    # making our functions values real
    real_signal_1.append(signal_1[number].real)
    real_signal_2.append(signal_2[number].real)

# retyping our lists to arrays to work with plots
ModuleS = np.asarray(ModuleS)
Phase = np.asarray(Phase)
signals_time = np.asarray(signals_time)
signal_1_time = np.asarray(signal_1_time)
signal_2_time = np.asarray(signal_2_time)
signal_1 = np.asarray(signal_1)
signal_2 = np.asarray(signal_2)
signals = np.asarray(signals)

# creating 4 subplots
signal, ax = plt.subplots(4)

axs = [ax[i] for i in range(4)]
for plot in range(4):
    if plot == 0:
        axs[plot].plot(signals_time, ModuleS)
    if plot == 1:
        axs[plot].plot(signal_1_time, signal_1)
    if plot == 2:
        axs[plot].plot(signal_2_time, signal_2)
    if plot == 3:
        axs[plot].plot(signals_time, Phase)
plt.grid(True)

plt.show()

pass
