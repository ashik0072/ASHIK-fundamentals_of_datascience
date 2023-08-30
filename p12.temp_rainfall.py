import matplotlib.pyplot as plt

# Sample data: Replace with your actual data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [20, 22, 25, 28, 30, 32, 32, 31, 29, 27, 24, 21]
rainfall = [50, 40, 60, 80, 100, 120, 150, 140, 120, 100, 80, 60]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# 1. Line plot of monthly temperature data
ax1.plot(months, temperature, marker='o', linestyle='-', color='b')
ax1.set_title('Monthly Temperature Data')
ax1.set_xlabel('Months')
ax1.set_ylabel('Temperature (°C)')
ax1.grid(True)

# 2. Scatter plot of monthly rainfall data
ax2.scatter(months, rainfall, color='r', marker='o')
ax2.set_title('Monthly Rainfall Data')
ax2.set_xlabel('Months')
ax2.set_ylabel('Rainfall (mm)')
ax2.grid(True)

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
