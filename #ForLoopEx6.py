
#Program for Finding Sum of Cubes of N Natural Numbers where N Is +Ve
#ForLoopEx6.py
n=int(input("Enter the Value of N for Finding Its Cubes Sum:"))
if(n<=0):
    print("{} is Invalid Number:".format(n))
else:
    s=0 # here Initlizing the var s=0 is called Additive Identity
    ss=0
    cs=0
    print("-" * 50)
    print("\tNatNums\t\tSquares\t\tCubes")
    print("-" * 50)
    for i in range(1,n+1):
        print("\t{}\t\t\t\t{}\t\t\t{}".format(i,i*i,i*i*i))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("-"*50)
        print("\t{}\t\t\t\t{}\t\t\t{}".format(s,ss,cs))
        print("-" * 50)

