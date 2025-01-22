import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('output.csv')

timesteps = [0, 100, 500, 1000]
for step in timesteps:
    subset = data[data['TimeStep'] == step]
    plt.plot(subset['x'], subset['u_numerical'], label=f'Numerical (t={step})')
    plt.plot(subset['x'], subset['u_analytical'], '--', label=f'Analytical (t={step})')

plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('Solution of 1D Diffusion Equation')
plt.legend()
plt.show()
