#Program for Generating Even Numbers within n in Decresing Order
#WhileLoopEx3.py
n=int(input("Enter How Many Even Number u want to generate within range:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    print("-"*50)
    print("Even  Numbers within {} to 2".format(n))
    print("-" * 50)
    n= n if(n%2==0) else n-1
    while(n>=2):
        print("\t{}".format(n))
        n=n-2
    else:
        print("-" * 50)
