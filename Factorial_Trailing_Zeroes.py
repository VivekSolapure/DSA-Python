cal,power,sum,n=1,1,1,5
while cal!=0:
    # print("cal",cal)
    cal=n//pow(5,power)
    sum+=cal
    power+=1
    # print(sum)
print(sum-1)