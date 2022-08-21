import math
import cmath

def quadSolver(a,b,c, tol = 1e-18):
    print('Equation: {0}x**2 + {1}x + {2}'.format(a,b,c))
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        root1 = float(-b + math.sqrt(b**2 - 4 * a * c))/ (2 * a)
        root2 = float(-b - math.sqrt(b**2 - 4 * a * c))/ (2 * a)
        print('Has two roots:')
        print(root1)
        print(root2)
    elif discriminant == 0:
        root1 = float(-b + math.sqrt(b**2 - 4 * a * c))/ (2 * a)
        print('Has a double root:')
        print(root1)
    elif discriminant < 0:
        root1 = (-b + cmath.sqrt(b**2 - 4 * a * c))/ (2 * a)
        root2 = (-b - cmath.sqrt(b**2 - 4 * a * c))/ (2 * a)
        print('Has two complex roots:')
        print(root1)
        print(root2)