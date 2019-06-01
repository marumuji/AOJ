input_val = input('').split()
x = int(input_val[0])
y = int(input_val[1])

def gcd(x, y):
    if x < y:
        x, y = y, x
    
    while y > 0:
        r = x % y
        x = y
        y = r
    
    return x

print(gcd(x, y))
