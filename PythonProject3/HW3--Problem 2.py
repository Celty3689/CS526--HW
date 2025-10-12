def substrings(s):
    unique = set()  #Store all unique substrings in a set.

    def find(i, j):
        #If the current index is within the range of the string
        if i < len(s) and j <= len(s):
            unique.add(s[i:j])  #Add the substring to the set.
            find(i, j+1)
        elif i < len(s)-1:
            find(i+1, i+2)  #Start position +1, end position starts from the start +1.

    find(0, 1)  #Recursively starting from the first character
    #print the result
    print(', '.join(unique))
    print(len(unique))

substrings("abcab")