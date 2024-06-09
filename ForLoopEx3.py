
#Program for generating Mul Table for a given Number
#ForloopEx3.py
n=int(input("Enter a number for generating mul Table:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("mul Table for :{}".format(n))
    for i in range(1,11):
        print("\t\t{} x {}={}".format(n,i,n*i))