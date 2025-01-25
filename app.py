import numpy as np
import csv

# Parameters
N = 128  # Number of grid points
L = 1.0  # Length of the domain
T = 0.1  # Total time
dt = 0.00001  # Time step
dx = L / N  # Spatial step
num_steps = int(T / dt)  # Number of time steps

# Initial condition: u(x, 0) = sin(2*pi*x)
u = np.zeros(N)
for i in range(N):
    u[i] = np.sin(2 * np.pi * i * dx)

# Open a CSV file to store the results
with open('diffusion_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(['Time Step', 'x', 'Numerical Solution', 'Exact Solution', 'Error', 'Average Error'])
    
    # Time-stepping loop
    for n in range(num_steps):
        # Create a temporary array for the updated values
        u_new = np.zeros(N)

        # Apply the explicit Euler and central difference scheme
        for i in range(1, N - 1):
            u_new[i] = u[i] + dt * (u[i+1] - 2*u[i] + u[i-1]) / (dx * dx)

        # Periodic boundary conditions
        u_new[0] = u_new[N-2]
        u_new[N-1] = u_new[1]

        # Update the solution for the next time step
        u = u_new

        # Compute the exact solution at this time step
        t = n * dt  # Current time
        u_exact = np.sin(2 * np.pi * np.linspace(0, L, N)) * np.exp(-2 * np.pi**2 * t)

        # Compute the error at each grid point
        error = np.abs(u - u_exact)

        # Compute the average error across the domain
        avg_error = np.mean(error)

        # Output solution and error at selected time steps
        if n == 0 or n == 100 or n == 500 or n == 1000:
            for i in range(N):
                # Write data for each time step
                writer.writerow([n, i * dx, u[i], u_exact[i], error[i], avg_error])

print("Results saved to 'diffusion_results.csv'")
