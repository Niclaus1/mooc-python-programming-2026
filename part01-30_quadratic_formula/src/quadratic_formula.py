# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
valueA = float(input('Values of a:'))
valueB = float(input('Values of b:'))
valueC = float(input('Values of c:'))


valueNeg = ((valueB * -1) - sqrt((valueB * valueB) - (4 * valueA * valueC))) / (2 * valueA)
ValuePos = ((valueB * -1) + sqrt((valueB * valueB) - (4 * valueA * valueC))) / (2 * valueA)

print(f'The roots are {ValuePos} and {valueNeg}')