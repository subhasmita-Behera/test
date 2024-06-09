#Program for generating n to 1  Numbers where n is +ve
#ForLoopEx2.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("{} is Invalid".format(n))
else:
    print("-" * 50)
    print("Numbers within {}".format(n))
    print("-" * 50)
    for i in range(n,0,-1):
        print("\t{}".format(i))
    else:
        print("-"*50)

