import numpy as np
import matplotlib.pyplot as plt

# Measured data (replace with actual values from your table)
# For demonstration, we'll create sample data (use your own data here)

current_data = np.array([0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0])  # I (in amps)
frequency_data = np.array([1000, 1200, 1500, 1800, 2000, 2500, 3000, 3500])  # Frequency in Hz
duty_cycle_data = np.array([0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05])  # Duty cycle (0-1)

# Constants
battery_voltage = 12  # Battery voltage in volts
pi = np.pi

# Convert frequency to angular speed (omega) in rad/s
angular_speed = 2 * pi * frequency_data / 60

# Calculate motor voltage (Umotor) using the duty cycle
U_motor = battery_voltage * duty_cycle_data

# Calculate x = I / omega and y = Umotor / omega
x = current_data / angular_speed
y = U_motor / angular_speed

# Perform linear regression using numpy.polyfit to find Ra (slope) and km (intercept)
coefficients = np.polyfit(x, y, 1)
Ra = coefficients[0]  # Ra is the slope
km = coefficients[1]  # km is the intercept

# Predicted y values based on the fit (for plotting)
y_fit = Ra * x + km

# Plotting the results
plt.scatter(x, y, label="Measured Data", marker='o')
plt.plot(x, y_fit, label="Fitted Line", color='red', linestyle='--')
plt.xlabel('I / ω [A/rad/s]')
plt.ylabel('U_motor / ω [V/rad/s]')
plt.title('Linear Regression to Find Ra and Km')
plt.legend()
plt.grid(True)
plt.show()

# Print the results
print(f"Ra (Armature Resistance) = {Ra:.4f} ohms")
print(f"Km (Torque Constant) = {km:.4f} Nm/A")

Ra_theoretical = 1.71  # From question 1c
km_theoretical = 0.00990217  # From question 1d (in Nm/A)

# Calculate percentage differences
Ra_diff_percentage = (abs(Ra - Ra_theoretical) / Ra_theoretical) * 100
km_diff_percentage = (abs(km - km_theoretical) / km_theoretical) * 100

# Print the percentage differences
print(f"Percentage difference in Ra: {Ra_diff_percentage:.2f}%")
print(f"Percentage difference in Km: {km_diff_percentage:.2f}%")

# Explanation if difference is greater than 3%
if Ra_diff_percentage > 3 or km_diff_percentage > 3:
    print("The difference is more than 3%, which could be due to factors like measurement errors, "
          "non-idealities in the components, or simplifications in the model.")
