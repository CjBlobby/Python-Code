def fibbonacci():
    a = 0
    b = 1
    x = 0
    while b < 4000000:
        yield b
        a,b = b, a+b

total = 0
for num in fibbonacci():
    if num % 2 == 0:
        total += num
print(total)
