# Collatz Conjecture Code that keeps track of the number of steps
# and the largest value reached during the loop.

# "x" is the number to start with.

# "steps" is the frequency of steps you want printed to the terminal.
# i.e. "steps=2" -> every other step.
def collatz(x, steps=1):
    n = 0
    large = 0
    #x = int(eval(input("Enter number: ")))
    number = x
    #steps = int(eval(input("Enter number of steps to print: ")))
    print(x,"\t",n)
    while x != 1:
        if x > large:
            large = x
        if x%2 == 0:
            x = x / 2
            n += 1
            if n%steps == 0:
                print(x,"\t",n)
        else:
            x = 3*x + 1
            n += 1
            if n%steps == 0:
                print(x,"\t",n)
    if (x == 1):
        print("Done\nStarting number: {}\nLargest value = {}\nTotal Steps to 1: {}".format(number,large,n))
