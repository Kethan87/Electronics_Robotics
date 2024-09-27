# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# corresponding y axis values
y = [0.434, 0.375,0.331,0.298,0.269,0.246,0.229,0.211,0.197, 0.185 ]

# plotting the points 
plt.plot(x, y)

# naming the x axis
plt.xlabel('voltage')
# naming the y axis
plt.ylabel('ampere')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()