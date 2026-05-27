import sys

#n=int(input("enter the starting no. to test the collatz conjecture="))
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 27 # Fallback default

while n!=1:

    
    odd=(3*n+1)
    even=(n//2)

    if n%2==0:
        print("n is",n)
        print("current n is even")
        print(even)
        n=even
        print("")
    else:
        print("n is",n)
        print("current n is odd")
        print(odd)
        n=odd
        print("")
        
print("for the n you entered first, it satisfis collatz conjecture function")
