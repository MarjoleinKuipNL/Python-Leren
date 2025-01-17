# Find the greates common denominator of two numbers.
# using Euclid's algorithm

def gcd(a, b):
    while(b != 0):
        t = a
        a = b
        b = t % b
    return a

# Try out the function with a few examples
print(gcd(60, 96)) #should be 12
print(gcd(20, 8)) #should be 4