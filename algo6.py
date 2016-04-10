#Uses python3

n = int(input())
a = [int(x) for x in input().split()]


max=0

i=0
if(len(a)==n):
    while(i<len(a)):
        for j in range(i+1, len(a)):
            if a[i]*a[j] > max:
                max = a[i]*a[j]
        i+=1
    print(max)
    
else:
    print("Incorrect input")



