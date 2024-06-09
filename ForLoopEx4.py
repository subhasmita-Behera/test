#program from finding   sum of N Natural Numbers Where N is +ve
#forL00pEx4.py
n=int(input("Enter the value for N for finding its sum:"))
if(n<=0):
    print("{} is invalid Number:".format(n))
else:
    s=0 # here initializing the var s=0 is called Additive identity
    for i in range(1,n+1):
        print("\t{}".format(i))
        s=s+i
    else:
        print("sum of {} Numbers={}".format(n,s))
