# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# corresponding y axis values
y = [1275,1475,1672,1870,2120,2301,2503,2685,2855,3042 ]

# plotting the points 
plt.plot(x, y)

# naming the x axis
plt.xlabel('voltage')
# naming the y axis
plt.ylabel('micro voltage')

# giving a title to my graph
plt.title('Question 15b')

# function to show the plot
plt.show()
