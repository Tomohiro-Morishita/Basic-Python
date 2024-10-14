a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
def prime_number(n):
    count = 2
    while count <= n ** (1 / 2):
        if n % count == 0:
            return False   
        count += 1
    if count > n ** (1 / 2):
        return True
    
numbers = [int(a),int(b)]
for number in numbers:
    print(f"{number}:{prime_number(number)}")