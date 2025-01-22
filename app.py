import numpy as np
import math
import csv

PI = math.pi

def initialize(N, dx):
    return np.sin(2 * PI * np.arange(N) * dx)

def update(u, alpha, N):
    u_new = np.zeros_like(u)
    for i in range(N):
        left = N - 1 if i == 0 else i - 1
        right = 0 if i == N - 1 else i + 1
        u_new[i] = u[i] + alpha * (u[right] - 2 * u[i] + u[left])
    return u_new

def compute_error(u, u_analytical):
    return np.mean(np.abs(u - u_analytical))

def analytical_solution(N, dx, t):
    x = np.arange(N) * dx
    return np.sin(2 * PI * x) * np.exp(-4 * PI**2 * t)

def main():
    N = 128                # Number of grid points
    dx = 1.0 / N           # Spatial resolution
    dt = 0.00001           # Time step
    alpha = dt / (dx * dx)
    steps = [0, 100, 500, 1000]

    u = initialize(N, dx)
    u_new = np.zeros_like(u)

    with open("output.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["TimeStep", "x", "u_numerical", "u_analytical", "error"])

        for n in range(1001):
            if n in steps:
                u_analytical = analytical_solution(N, dx, n * dt)
                error = compute_error(u, u_analytical)
                for i in range(N):
                    writer.writerow([n, i * dx, u[i], u_analytical[i], error])
            
            u_new = update(u, alpha, N)
            u = u_new.copy()

    print("Simulation complete. Results saved to output.csv.")

if __name__ == "__main__":
    main()
