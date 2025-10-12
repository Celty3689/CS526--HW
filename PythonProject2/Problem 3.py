#Problem 3: Implement the function and output doIt(1), doIt(3), doIt(6)

def doIt(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return doIt(n-1) + doIt(n-2) - doIt(n-3)

#Calculate and print out the result
print(f"doIt(1) = {doIt(1)}")
print(f"doIt(3) = {doIt(3)}")
print(f"doIt(6) = {doIt(6)}")