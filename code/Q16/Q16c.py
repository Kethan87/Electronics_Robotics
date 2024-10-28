import numpy as np
import matplotlib.pyplot as plt

I_positive = [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.05, 2.4]
VCS_positive = [1.7, 1.87, 2.03, 2.18, 2.35, 2.5, 2.65, 2.77, 2.9]

I_negative = [0, -0.3, -0.6, -0.9, -1.2, -1.5, -1.8, -2.1, -2.4]
VCS_negative = [1.7, 1.55, 1.39, 1.26, 1.07, 0.91, 0.74, 0.61, 0.45]

I_combined = np.array(I_positive + I_negative)
VCS_combined = np.array(VCS_positive + VCS_negative)

coefficients = np.polyfit(VCS_combined, I_combined, 1)

# Extract c2 and I0 from the coefficients
c2 = coefficients[0] # slope
I0 = coefficients[1]  # intercept


print("I0: ",I0)
print("C2: ", c2)
# Predicted VCS based on the fit
VCS_fit = c2 * I_combined + I0

# Plot the original data and the fitted line
plt.plot(I_positive, VCS_positive, label="Positive I [A]", marker='o')
plt.plot(I_negative, VCS_negative, label="Negative I [A]", marker='o')
plt.plot(I_combined, VCS_fit, label="Fitted Line", linestyle='--')

plt.xlabel('Current (I) [A]')
plt.ylabel('Voltage (VCS) [V]')
plt.title('Current vs Voltage (VCS) with Linear Fit')
plt.legend()
plt.grid(True)
plt.show()

print(f"I0 (intercept) = {I0:.4f} V")
print(f"c2 (slope) = {c2:.4f} V/mA")

R1 = 0.0225  # in ohms
R38 = 10000  # in ohms

# Expected values:
expected_c2 = 1 / R1 * 1000 # Assuming c2 is 1/R1
expected_I0 = 1.7  # Assuming a starting voltage of 1.7 V as in the provided data

c2_diff_percentage = (abs(c2 - expected_c2) / expected_c2) * 100
I0_diff_percentage = (abs(I0 - expected_I0) / expected_I0) * 100

print(f"Percentage difference in c2: {c2_diff_percentage:.2f}%")
print(f"Percentage difference in I0: {I0_diff_percentage:.2f}%")

if c2_diff_percentage > 3 or I0_diff_percentage > 3:
    print("The difference is more than 3%, which could be due to factors like measurement errors, "
          "non-idealities in the components (e.g., resistor tolerances), or simplifications in the model.")
