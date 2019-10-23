x,y=1,0
sum = 0
while sum<=4000000:
    if y %2 == 0:
        sum+=y
    # if sum > 4000000:
    #     sum-=y
        # break
    x,y = y,x+y
print('sum = ',sum)

