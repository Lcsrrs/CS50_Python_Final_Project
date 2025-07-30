import matplotlib.pyplot as plt

# Data for multiple lines
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [5, 4, 3, 2, 1]

# Plotting each line
plt.plot(x, y1, label='teste 1', color='blue')
plt.plot(x, y2, label='teste 2', color='red', linestyle='--')
plt.plot(x, y3, label='teste 3', color='green', marker='o')

# Adding labels, title, and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines on One Plot')
plt.legend()

# Display the plot
plt.show()