def fibbonacci(maxn):
    a = 0
    b = 1
    x = 0
    for i in range(0, maxn+1):
        yield a
        a,b = b, a+b
        
for num in fibbonacci(999):
    print(num, "\n")
