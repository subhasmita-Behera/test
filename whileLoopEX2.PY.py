#program for generating n to 1 number
#whileloopEx2.py
n=int(input("Enter How many number u want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("Numbers within {} to 1".format(n))
    i=n
    while(i>=1):
        print("\t\t".format(n))
        i=i-1
    else:
        print("-" * 50)