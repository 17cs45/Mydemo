# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

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
