def fact(N):
    fact = 1 
    while N > 0:
        fact*=N
        N-=1
    return fact
Input = int(input('enter Number : '))
print('Factorial = ',fact(Input))