#Program for generating Mul Table for a given Number
#WhileLoopEx4.py
n=int(input("Enter a Number for Generating Mul Table:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("="*50)
    print("Mul Table for :{}".format(n))
    print("=" * 50)
    i=1 # Initlization Part
    while(i<=10): # Cond Part
        print("\t{} x {}={}".format(n,i,n*i))
        i=i+1 # Updation Part
    else:
        print("=" * 50)
