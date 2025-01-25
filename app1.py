import numpy as np
import matplotlib.pyplot as plt
import csv

# Define dt here
dt = 0.00001

# Load the data from the CSV file
x_vals = []
numerical_vals = []
exact_vals = []
errors = []
avg_errors = []
time_steps = []

with open('diffusion_results.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        time_steps.append(int(row[0]))
        x_vals.append(float(row[1]))
        numerical_vals.append(float(row[2]))
        exact_vals.append(float(row[3]))
        errors.append(float(row[4]))
        avg_errors.append(float(row[5]))

# Convert to numpy arrays for easier manipulation
x_vals = np.array(x_vals)
numerical_vals = np.array(numerical_vals)
exact_vals = np.array(exact_vals)
errors = np.array(errors)
avg_errors = np.array(avg_errors)

# Plot the numerical solution, exact solution, and error for a specific time step
for t in [0, 100, 500, 1000]:
    indices = np.array(time_steps) == t
    plt.plot(x_vals[indices], numerical_vals[indices], label=f'Numerical (t={t*dt:.5f})')
    plt.plot(x_vals[indices], exact_vals[indices], label=f'Exact (t={t*dt:.5f})')

plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('Numerical vs Exact Solution')
plt.legend()
plt.show()

# Plot the error
for t in [0, 100, 500, 1000]:
    indices = np.array(time_steps) == t
    plt.plot(x_vals[indices], errors[indices], label=f'Error (t={t})')

plt.xlabel('x')
plt.ylabel('Error')
plt.title('Error in Numerical Solution')
plt.legend()
plt.show()

# Plot the average error vs time step
unique_time_steps = np.unique(time_steps)
avg_errors_per_time_step = [np.mean(avg_errors[np.array(time_steps) == t]) for t in unique_time_steps]

plt.plot(unique_time_steps * dt, avg_errors_per_time_step, label='Average Error')
plt.xlabel('Time')
plt.ylabel('Average Error')
plt.title('Average Error vs Time')
plt.legend()
plt.show()
