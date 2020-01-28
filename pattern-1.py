n=7
for i in range(n//2,-n//2,-1):
    for j in range(n//2,-1,-1):
        if(j>=abs(i)):
            print("*",end='')
    print()