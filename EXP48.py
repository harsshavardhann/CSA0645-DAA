def karatsuba(x, y):
    
    if x < 10 or y < 10:
        return x * y
    
    # Find number of digits
    x_str = str(x)
    y_str = str(y)
    n = max(len(x_str), len(y_str))
    
    # Make both numbers same length by padding with zeros
    x = int(str(x).zfill(n))
    y = int(str(y).zfill(n))
    
    # Divide numbers into two halves
    m = n // 2
    
    # Split numbers
    x1 = x // (10 ** m)
    x0 = x % (10 ** m)
    y1 = y // (10 ** m)
    y0 = y % (10 ** m)
    
    # Recursive calls
    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0
    
    # Combine results
    result = z2 * (10 ** (2 * m)) + z1 * (10 ** m) + z0
    return result

def karatsuba_with_steps(x, y):
    """Karatsuba with step-by-step calculation"""
    print(f"\nKaratsuba Multiplication: {x} × {y}")
    print("=" * 50)
    
    # Base case
    if x < 10 or y < 10:
        result = x * y
        print(f"Base case: {x} × {y} = {result}")
        return result
    
    # Find number of digits
    x_str = str(x)
    y_str = str(y)
    n = max(len(x_str), len(y_str))
    print(f"Number of digits: {n}")
    
    # Make both numbers same length
    x = int(str(x).zfill(n))
    y = int(str(y).zfill(n))
    
    # Divide numbers
    m = n // 2
    print(f"Split position (m): {m}")
    
    x1 = x // (10 ** m)
    x0 = x % (10 ** m)
    y1 = y // (10 ** m)
    y0 = y % (10 ** m)
    
    print(f"x = {x1} × 10^{m} + {x0}")
    print(f"y = {y1} × 10^{m} + {y0}")
    
    # Recursive calls
    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0
    
    print(f"z2 = {x1} × {y1} = {z2}")
    print(f"z0 = {x0} × {y0} = {z0}")
    print(f"z1 = ({x1}+{x0}) × ({y1}+{y0}) - z2 - z0 = {z1}")
    
    # Combine results
    result = z2 * (10 ** (2 * m)) + z1 * (10 ** m) + z0
    print(f"Result = {z2}×10^{2*m} + {z1}×10^{m} + {z0} = {result}")
    
    return result

# Test Case 1
print("=" * 70)
print("Test Case 1:")
x1 = 1234
y1 = 5678
print(f"Input: x = {x1}, y = {y1}")
result1 = karatsuba(x1, y1)
print(f"Output: z = {x1} × {y1} = {result1}")
print(f"Expected: 7016652")
print()

# Test Case with detailed steps
print("=" * 70)
print("Test Case 2 (Detailed Steps):")
x2 = 1234
y2 = 5678
result2 = karatsuba_with_steps(x2, y2)
print(f"\nFinal Result: {result2}")
print("=" * 70)
