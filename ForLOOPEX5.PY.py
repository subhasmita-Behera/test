#Program for finding its squares of N  Natural Numbers Where N is +ve
#forloopEx5.py
n=int(input("enter the value of N for finding its squares sum:"))
if(n<=0):
    print("{} is invalid Number:".format(n))
else:
    s=0 # here initializing the var s=0 is called additive identity
    ss=0
    print("-" * 50)
    print("\tNatNums\t\tSquares")
    print("-" * 50)
    for i in range(1, n + 1):
        print("\t{}\t\t\t\t{}".format(i, i * i))
        s = s + i
        ss = ss + i ** 2
    else:
        print("-" * 50)
        print("\t{}\t\t\t\t{}".format(s, ss))
        print("-" * 50)
