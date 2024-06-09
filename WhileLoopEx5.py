#Program for Generating a chars from word or line of Text
#WhileLoopEx6.py
word=input("Enter a word OR Line of Text:")
print("Given Word={}".format(word))
i=0
while(i<len(word)):
    print("\t{}".format(word[i]))
    i=i+1
print("-------------OR---------------")
i=len(word)-1
while(i>=0):
    print("\t{}".format(word[i]))
    i=i-1
print("-------------OR---------------")
i=0
word=word[::-1]
while(i<len(word)):
    print("\t{}".format(word[i]))
    i=i+1
print("-------------OR---------------")
word=word[::-1]
i=-1
while(i>=(-len(word))):
    print("\t{}".format(word[i]))
    i=i-1
print("-------------OR---------------")
i=-len(word)
while(i<=-1):
    print("\t{}".format(word[i]))
    i=i+1


