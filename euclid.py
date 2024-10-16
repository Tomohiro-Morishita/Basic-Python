a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

def euclid(a, b):
    a = int(a)
    b = int(b)
    if a >= b:
        high = a
        low = b
    else:
        high = b
        low = a
    while low != 0:
        low, high = high % low, low
    return high

def mutually_prime(a, b):
    return euclid(a, b) == 1

print(euclid(a, b))
print(mutually_prime(a, b))

