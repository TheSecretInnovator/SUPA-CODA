# Recursive functions (April 1st)

# Binary to Decimal using recursion

def bintodec(n):
    if n==0:
        return 0
    
    return n%10 + 2*bintodec(n//10)

print(bintodec(int(input())))