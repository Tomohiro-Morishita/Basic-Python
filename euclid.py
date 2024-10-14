a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a = int(a)
b = int(b)
if a >= b:
    high = a
    low = b
else :
    high = b
    low = a

while low != 0:
    tmp= low
    low = high % low
    high = tmp
print("%dと%dの最大公約数は%d"%(a, b, high))
