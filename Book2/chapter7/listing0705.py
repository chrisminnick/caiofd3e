# Import the math module to use the sqrt() function
import math
  
# Define two points as (x, y) tuples
point1 = (3, 4)
point2 = (7, 1)
  
# Calculate the difference between the x values
dx = point2[0] - point1[0]
  
# Calculate the difference between the y values
dy = point2[1] - point1[1]
  
# Apply the Pythagorean theorem:
# distance = @@sq(dx² + dy²)
distance = math.sqrt(dx**2 + dy**2)
  
print(f"The distance between the points is: {distance:.2f}")
