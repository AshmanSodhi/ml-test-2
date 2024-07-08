import matplotlib.pyplot as plt
import random

# Generate 6 random values for x and y
x = [random.randint(1, 10) for _ in range(6)]
y = [random.randint(1, 10) for _ in range(6)]

# Plotting the points
plt.plot(x, y, marker='o')  # Adding markers to visualize the points clearly

# Naming the x axis
plt.xlabel('x - axis')
# Naming the y axis
plt.ylabel('y - axis')

# Giving a title to my graph
plt.title('My first graph with random values!')

# Save the plot as an image file
plt.savefig('page/books_read.png')

# Display the plot
plt.show()
