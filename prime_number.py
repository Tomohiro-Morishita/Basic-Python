a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
numbers = [int(a),int(b)]
for number in numbers:
    count = 2
    if number <= 1:
        print(f"{number}は素数ではありません")
        continue
    while count <= number ** (1 / 2):
        if number % count == 0:
            print(f"{number}は素数ではありません")
            break
        count += 1
    if count > number ** (1 / 2):
        print(f"{number}は素数です")
