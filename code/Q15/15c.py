# importing the required module
import numpy as np

# x axis values
x = np.array([6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
# corresponding y axis values
y = np.array([1275,1475,1672,1870,2120,2301,2503,2685,2855,3042 ])

result = x / (y / 1000)
    
print(np.mean(result))
