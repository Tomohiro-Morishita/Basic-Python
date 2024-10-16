a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
def prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            return False   
    return True
    
numbers = [int(a),int(b)]
for number in numbers:
    print(f"{number}:{prime_number(number)}")