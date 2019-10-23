def palidromic(num):
    num = str(num)
    if num == num[-1::-1]:
        return True
    return False
product = 1
temp = 0 
for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        if (palidromic(product) and product > temp):
            temp = product
print(temp)
