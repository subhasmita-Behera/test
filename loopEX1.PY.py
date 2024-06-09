#Program for Generating 1 to n Numbers
# 1 2 3 4 5 6 7 8 9  10
#WhileLoopEx1.py
n=int(input("Enter How Many Numbers u want to Generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    i=1 # InitLization Part
    while(i<=n): # Cond Part
        print("{}".format(i))
        i=i+1 # Updation Part
    else:
        print("I am from else part of while loop")
    print("Other statements of while Loop Statements")
print("Other statements of if..else Statements")

