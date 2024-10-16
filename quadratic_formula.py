num_a = [ 1, 1, 8, 1]
num_b = [-6, 2, -6, 0]
num_c = [9, -8, -35, 1]

# TODO
for a, b, c in zip(num_a, num_b, num_c):
    x1 = (-b + (((b ** 2) - (4 * a * c)) ** (1 / 2))) / (2 * a)
    x2 = (-b - (((b ** 2) - (4 * a * c)) ** (1 / 2))) / (2 * a)
    print(f"解は{x1},{x2}\n")