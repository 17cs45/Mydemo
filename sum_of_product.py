#Muliple of 3 and 5 addition 

def sum():
    total = 0
    for i in range(1,1000):
        if i %3 == 0 or i%5 == 0:
            total+=i
    return total
<<<<<<< HEAD
print(f'sum of multiples of 3 and 5 = {sum()}')
=======
print('sum of multiples of 3 and 5 =',sum())
>>>>>>> refs/remotes/origin/master
