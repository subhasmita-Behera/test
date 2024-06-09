#Program for generating 1 to n Numbers where n is +ve
#ForLoopEx1.py
n=int(input("Enter How many numbers u want to generate:"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    print("Numbers within {}".format(n))
    for i in range(1,n+1):
        print("\t{}".format(i))
