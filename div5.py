n=int(input("Enter number div by 5"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("divisible number within {} to 5".format(n))
    n= n%5==0 els