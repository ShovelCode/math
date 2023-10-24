import matplotlib.pyplot as plt
import numpy as np

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 400)

# Calculate y values based on x (y = x^2)
y = x**2

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y)

# Add title and labels
plt.title('Parabola Graph: $f(x) = x^2$')
plt.xlabel('x')
plt.ylabel('f(x)')

# Show the plot
plt.show()