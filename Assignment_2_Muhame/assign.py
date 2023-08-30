import numpy as np

print(np.__version__)

import math

def golden_ratio_approximation():
    
    sqrt_5 = math.sqrt(5)
    golden_ratio_approx = (1 + sqrt_5) / 2
    return golden_ratio_approx

golden_ratio_approx = golden_ratio_approximation()
print(golden_ratio_approx)
