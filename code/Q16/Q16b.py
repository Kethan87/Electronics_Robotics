import matplotlib.pyplot as plt

I_positive = [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.05, 2.4]
VCS_positive = [1.7, 1.87, 2.03, 2.18, 2.35, 2.5, 2.65, 2.77, 2.9]

I_negative = [0, -0.3, -0.6, -0.9, -1.2, -1.5, -1.8, -2.1, -2.4]
VCS_negative = [1.7, 1.55, 1.39, 1.26, 1.07, 0.91, 0.74, 0.61, 0.45]

plt.plot(I_positive, VCS_positive, label="Positive I [mA]", marker='o')
plt.plot(I_negative, VCS_negative, label="Negative I [mA]", marker='o')

plt.xlabel('Current (I) [mA]')
plt.ylabel('Voltage (VCS) [V]')
plt.title('Current vs Voltage (VCS)')
plt.legend()
plt.grid(True)
plt.show()
