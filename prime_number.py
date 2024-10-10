a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
count = 2
numbers = [int(a),int(b)]
for number in numbers:
    while count < number:
        if number % count == 0:
            print(f"{number}は素数ではありません")
            break
        count += 1
    if count == number:
        print(f"{number}は素数です")
